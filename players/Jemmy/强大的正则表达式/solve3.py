from typing import Set, List
import re
import libscrc
import random
from tqdm import tqdm

class rex:
    def epsilon():
        return special_rex(is_epsilon=True)
    def none():
        return special_rex(is_epsilon=False)
    
    def star(self):
        if self.is_none or self.is_epsilon:
            return self
        return rex_star(self)
    
    def simplify(self):
        if isinstance(self, special_rex):
            return self
        if isinstance(self, simple_rex):
            return self
        if isinstance(self, rex_star):
            return rex_star(simple_rex(str(self.value.simplify())))
        if isinstance(self, rex_chain):
            ss = ''
            for rex in self.chains:
                s = str(rex)
                if isinstance(rex, rex_star) or len(s) == 1:
                    ss += s
                else:
                    ss += f'({s})'
            return simple_rex(ss)
        if isinstance(self, rex_or):
            ss = ''
            l = set(map(str, self.values))
            for s in l:
                if len(s) == 1:
                    ss += s
                else:
                    ss += f'({s})'
                ss += '|'
            return simple_rex(ss[:-1])
        return self
    
    def __or__(self, other):
        if self.is_none:
            return other.copy()
        if self.is_epsilon:
            if other.is_none or other.is_epsilon:
                return self.copy()
            return other
        if other.is_none:
            return self.copy()
        if other.is_epsilon:
            return other.copy()
        
        if isinstance(self, rex_or):
            values = self.values.copy()
            if isinstance(other, rex_or):
                values |= other.values
            else:
                values.add(other.simplify())
            return rex_or(values)
        elif isinstance(other, rex_or):
            values = other.values.copy()
            values.add(self.simplify())
            return rex_or(values)
        
        return rex_or({self.simplify(), other.simplify()})

    def __add__(self, other):
        if self.is_none or other.is_none:
            return rex.none()
        if self.is_epsilon:
            return other.copy()
        if other.is_epsilon:
            return self.copy()
        
        if isinstance(self, rex_chain):
            chains = self.chains.copy()
            if isinstance(other, rex_chain):
                chains += other.chains
            else:
                chains.append(other.simplify())
            return rex_chain(chains)
        elif isinstance(other, rex_chain):
            chains = [self.simplify()]
            chains += other.chains
            return rex_chain(chains)
        else:
            return rex_chain([self.simplify(), other.simplify()])

class simple_rex(rex):
    def __init__(self, value: str):
        self.is_epsilon = False
        self.is_none = False
        self.is_star = False
        self.value = value
    
    def __repr__(self) -> str:
        return self.value
    
    def copy(self):
        return simple_rex(self.value)

class special_rex(rex):
    def __init__(self, is_epsilon: bool = False):
        self.is_epsilon = is_epsilon
        self.is_none = not is_epsilon
        self.is_star = False
    
    def __repr__(self) -> str:
        return 'ε' if self.is_epsilon else '$'
    
    def copy(self):
        return special_rex(self.is_epsilon)

class rex_chain(rex):
    def __init__(self, chains = List[rex]):
        self.chains = chains
        self.is_none = False
        self.is_epsilon = False
        self.is_star = False

    def __repr__(self) -> str:
        return str(self.simplify())
    
    def copy(self):
        return rex_chain([chain.copy() for chain in self.chains])

class rex_or(rex):
    def __init__(self, values = Set[rex]):
        self.values = values
        self.is_none = False
        self.is_epsilon = False
        self.is_star = False

        ss = set()
        vals = []
        for value in values:
            s = str(value.simplify())
            if s not in ss:
                ss.add(s)
                vals.append(value)
        self.values = set(vals)
    
    def __repr__(self) -> str:
        return str(self.simplify())
    
    def copy(self):
        return rex_or(self.values.copy())

class rex_star(rex):
    def __init__(self, value: rex):
        self.value = value
        self.is_none = False
        self.is_epsilon = False
        self.is_star = True

        assert not isinstance(value, rex_star)
    
    def all_in_parentheses(s):
        if s[0] != '(':
            return False
        if s[-1] != ')':
            return False
        layer = 1
        for c in s[1:-1]:
            if c == '(':
                layer += 1
            elif c == ')':
                layer -= 1
            if layer == 0:
                return False
    
    def __repr__(self) -> str:
        s = str(self.value)
        if len(s) == 1 or rex_star.all_in_parentheses(s):
            return f'{s}*'
        return f'({self.value})*'
    
    def copy(self):
        return rex_star(self.value)

class FSM:
    alphabet: set
    states: set
    initial: int
    finals: Set[int]
    transitions: dict

    def __init__(self, alphabet, states, initial, finals, transitions):
        self.alphabet = alphabet
        self.states = states
        self.initial = initial
        self.finals = finals
        self.transitions = transitions

        self.init_graph()
    
    def init_graph(self):
        M = [[rex.none() for _ in range(len(self.states))] for _ in range(len(self.states))]

        for state in range(len(self.states)):
            M[state][state] = rex.epsilon()

            for (t, s) in self.transitions[state].items():
                M[state][s] |= simple_rex(t)

        self.M = M
    
    def remove(self, k):
        for i in range(len(self.states)):
            for j in range(len(self.states)):
                i = self.states[i]
                j = self.states[j]
                k = self.states[k]
                if i == k or j == k:
                    continue
                self.M[i][i] |= self.M[i][k] + self.M[k][k].star() + self.M[k][i]
                self.M[i][j] |= self.M[i][k] + self.M[k][k].star() + self.M[k][j]
        for i in range(len(self.states)):
            self.M[i][k] = rex.none()
            self.M[k][i] = rex.none()

S = list(range(8))
C = list(map(str, range(10)))
machine = FSM(alphabet=C, states=S, initial=S[0], finals={S[7]}, 
              transitions={
                  0: {'0': 3, '1': 0, '2': 5, '3': 6, '4': 4, '5': 7, '6': 2, '7': 1, '8': 6, '9': 5}, 
                  1: {'0': 1, '1': 2, '2': 7, '3': 4, '4': 6, '5': 5, '6': 0, '7': 3, '8': 4, '9': 7}, 
                  2: {'0': 7, '1': 4, '2': 1, '3': 2, '4': 0, '5': 3, '6': 6, '7': 5, '8': 2, '9': 1}, 
                  3: {'0': 5, '1': 6, '2': 3, '3': 0, '4': 2, '5': 1, '6': 4, '7': 7, '8': 0, '9': 3}, 
                  4: {'0': 0, '1': 3, '2': 6, '3': 5, '4': 7, '5': 4, '6': 1, '7': 2, '8': 5, '9': 6}, 
                  5: {'0': 2, '1': 1, '2': 4, '3': 7, '4': 5, '5': 6, '6': 3, '7': 0, '8': 7, '9': 4}, 
                  6: {'0': 4, '1': 7, '2': 2, '3': 1, '4': 3, '5': 0, '6': 5, '7': 6, '8': 1, '9': 2}, 
                  7: {'0': 6, '1': 5, '2': 0, '3': 3, '4': 1, '5': 2, '6': 7, '7': 4, '8': 3, '9': 0}})

print(machine.M)

for i in range(1, 7):
    print(f'Removing {i}')
    machine.remove(i)
    print(machine.M)

print()
# sss = str(machine.M[0][0].simplify().star())
# sss = (machine.M[0][0] | (machine.M[0][7] + machine.M[7][7].star() + machine.M[7][0] )).star()
S00 = (machine.M[0][0] | (machine.M[0][7] + machine.M[7][7].star() + machine.M[7][0]))
S77 = (machine.M[7][7] | (machine.M[7][0] + machine.M[0][0].star() + machine.M[0][7]))
sss = S00.star() + machine.M[0][7] + S77.star()
sss = str(sss.simplify())
print(sss)
print('Length:', len(str(sss)))

regex = re.compile(sss)

for _ in tqdm(range(300)):
    s = str(random.randint(0, 2**64))
    assert bool(regex.fullmatch(s)) == (libscrc.gsm3(s.encode()) == 0)

with open('regex.txt', 'w') as f:
    f.write(str(sss))
print(sss)


from pwn import *

io = remote('202.38.93.141', 30303)
io.recvuntil(b'Please input your token: \n')
io.sendline(b'1411:MEQCIAplFMrlOcSGiuyvXbD2viXkZel+YtLmOBzUXj48+rzXAiBrX2C/xRLIxhAn+TJYUsQtGEDzpleulEFWzyijebwTXA==')
io.recvuntil(b'Enter difficulty level (1~3): ')
io.sendline(b'3')
io.recvuntil(b'Enter your regex: ')
io.sendline(sss)
print(io.recvall())