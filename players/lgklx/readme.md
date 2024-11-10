###### 玩家：lgklx ######
###### 时间：2024.11.10 ######
# 图灵完备的浮点数减法 #

**肝了三天三夜写出来的代码，凑合着看吧。**

**然而11/9当天12：00前debug没有完成导致错失USTC校内一血（亏麻！）**

想法是这样的，在下面这个程序里，最重要的函数其实只有两个，一个是XOR一个是DIV。你可以用这两个函数造出AND这样的函数出来。为了便于控制，在对32-bit数据进行操作的时候我们都进行了所谓的加head的处理，也就是说，在IEEE 754标准下，我们用fraction部分的前32个bit存入数据，指数部分控制在E=32，以及剩余的20个bit位填充0。

输入的是机器码，为了方便编程，我们需要写一个简单的编译器和一套编程语言来编译代码。程序的开始我们要存入一些要用到的常数作为常量。我们打包了一些短的机器码组成的序列为函数。此外，我们配备了一个名为EIP的寄存器来存储上一条指令运行结束后的位置。这样的话我们可以正确地访问内存。一般的变量也是用类似的手段实现，记住内存位置然后调用函数进行操作。

## 代码实现部分（编译器） ##
```python
#我们来为这个图灵机写一套汇编，并且写一个编译器来输出对应的机器码。

#用PRT打印机器码。一个PRT占用mem中一个比特空间。
def PRT(char):
    global EIP
    global file
    file.write('p.sendline(b"{}")\n'.format(char))
    EIP=EIP+1
    return
#EIP为全局变量，标志当前mem最后一项的位置。

def SUB(A,B):
    global EIP
    #作减法。运行完之后占用1个比特空间。
    PRT('{} {}'.format(A,B))
    return
        
def ADD(A,B):
    global EIP
    #取出A和B两个地址里的元素相加。运行完之后占用2个比特空间。
    PRT('32 {}'.format(B))
    PRT('{} {}'.format(A,EIP))
    return

def LOAD(A,B,C,D):
    global EIP
    #取出A和B和C和D里的4个8位数据，按照顺序合并装入一个浮点数的尾数部分（实际上是一个整数）。
    ADD(A,A)
    ADD(EIP,EIP)
    ADD(EIP,EIP)
    ADD(EIP,EIP)
    ADD(EIP,EIP)
    ADD(EIP,EIP)
    ADD(EIP,EIP)
    ADD(EIP,EIP)
    ADD(EIP,B)
    ADD(EIP,EIP)
    ADD(EIP,EIP)
    ADD(EIP,EIP)
    ADD(EIP,EIP)
    ADD(EIP,EIP)
    ADD(EIP,EIP)
    ADD(EIP,EIP)
    ADD(EIP,EIP)
    ADD(EIP,C)
    ADD(EIP,EIP)
    ADD(EIP,EIP)
    ADD(EIP,EIP)
    ADD(EIP,EIP)
    ADD(EIP,EIP)
    ADD(EIP,EIP)
    ADD(EIP,EIP)
    ADD(EIP,EIP)
    ADD(EIP,D)
    SUB(EIP,M+1)
    return

def TRU(A,n):
    global EIP
    #剪切A的(2^n)及其以前的数位。占用3个比特空间。
    #此处解释一下I+n的位置为什么要存2的幂次外要减去一个0.125，这是由于舍入规则有陷阱。如果有尾数最后一位之外还有小数0.5，那么并不是完全的所谓0舍1入，而是遵循0优先原则，还要取决于尾数最后一位。因此n较小的时候可能会导致函数处理不正确。
    SUB(A,I+n)
    SUB(EIP,K+n)
    SUB(EIP,L+n)
    return

def XOR(A,B):
    global EIP
    #返回XOR的结果。按位求异或后2^32这个头部会被丢掉（小心！）
    PRT('0.0')
    AX=EIP
    for i in range (0,32):
        TRU(A,i)
        TRU(B,i)
        ADD(EIP-3,EIP)
        TRU(EIP,i+1)
        SUB(EIP,EIP-3)
        SUB(AX,EIP)
        AX=EIP
    SUB(EIP,M+1)
    return

def AND(A,B):
    #返回AND的结果。由于AND的直接结果被左移一位了，需要用DIV2把指数降回去。
    XOR(A,B)
    SUB(EIP,M+2)
    ADD(A,B)
    SUB(EIP,EIP-2)
    DIV2(EIP)
    return

def DIV2(A):
    global EIP
    #在AND中，A如果达到2^33作为head会引发问题，这个用来给它除以2。我们照抄下面DIV的代码就可以了，注意头部的偏移使得你要选的常数都增大了。
    PRT('0.0')
    AX=EIP
    for j in range(1,33):
        TRU(A,j+1)
        SUB(A,EIP)
        SUB(EIP,N+1+j)
        SUB(EIP-1,EIP)
        SUB(AX,EIP)
        AX=EIP
    SUB(M+5,AX)
    for i in range(0,52):
        ADD(EIP,EIP)
    return

def DIV(A,n):
    global EIP
    PRT('0.0')
    AX=EIP
    #将A中数据整体除以2^(n)。A必须是有32位有效位且有head为2^32的数字。n必须要小于等于52. 与XAND类似，我们同样要小心舍入问题。
    for j in range(0,32):
        TRU(A,j+1)
        SUB(A,EIP)
        SUB(EIP,N+1+j)
        SUB(EIP-1,EIP)
        SUB(AX,EIP)
        AX=EIP
    SUB(M+4,AX)
    for i in range(0,53-n):
        ADD(EIP,EIP)
    return

def NOT(A):
    #输出A经过非运算之后的结果。
    SUB(M+3,A)
    return

def ROTR(A,n):
    global EIP
    #SHA-256算法中必需函数。
    TRU(A,n)
    AX=EIP
    SUB(A,EIP)
    for i in range(0,32-n):
        ADD(EIP,EIP)
    BX=EIP
    DIV(AX,n)
    ADD(EIP,BX)
    SUB(EIP,J+33-n)
    SUB(EIP,M+1)
    return

def SHR(A,n):
    global EIP
    #SHA-256算法中必需函数。
    TRU(A,n)
    DIV(EIP,n)
    SUB(EIP,J+33-n)
    SUB(EIP,M+1)
    return
    
def MOD(A,B):
    global EIP
    #模2^32加法。
    ADD(A,B)
    TRU(EIP,32)
    SUB(EIP-3,EIP)
    SUB(EIP,M+1)
    return

def Ch(x,y,z):
    AND(x,y)
    AX=EIP
    NOT(x)
    AND(EIP,z)
    BX=EIP
    XOR(AX,BX)
    return

def Maj(x,y,z):
    AND(x,y)
    AX=EIP
    AND(x,z)
    BX=EIP
    AND(y,z)
    CX=EIP
    XOR(AX,CX)
    XOR(EIP,BX)
    return

def Sigma0(x):
    ROTR(x,2)
    AX=EIP
    ROTR(x,13)
    BX=EIP
    ROTR(x,22)
    CX=EIP
    XOR(AX,BX)
    XOR(EIP,CX)
    return

def Sigma1(x):
    ROTR(x,6)
    AX=EIP
    ROTR(x,11)
    BX=EIP
    ROTR(x,25)
    CX=EIP
    XOR(AX,BX)
    XOR(EIP,CX)
    return
        
def sigma0(x):
    ROTR(x,18)
    AX=EIP
    ROTR(x,7)
    BX=EIP
    SHR(x,3)
    CX=EIP
    XOR(AX,BX)
    XOR(EIP,CX)
    return

def sigma1(x):
    ROTR(x,17)
    AX=EIP
    ROTR(x,19)
    BX=EIP
    SHR(x,10)
    CX=EIP
    XOR(AX,BX)
    XOR(EIP,CX)
    return

def DUMP(Z):
    global EIP
    #Z是32位的信息，但我们希望分成四段来输出。
    ROTR(Z,24)
    WH=EIP
    TRU(WH,8)
    SUB(WH,EIP)
    AX=EIP
    ROTR(Z,16)
    AI=EIP
    TRU(AI,8)
    SUB(AI,EIP)
    BX=EIP
    ROTR(Z,8)
    WO=EIP
    TRU(WO,8)
    SUB(WO,EIP)
    CX=EIP
    TRU(Z,8)
    SUB(Z,EIP)
    DX=EIP
    return ([AX,BX,CX,DX])

def OUTPUT(H):
    for i in range(0,8):
        for j in range(0,4):
            SUB(H[i][j],32)
    return

def sha256_float():
    #最终程序！
    #Hash值初始化
    h=[]
    PRT('6074000999')
    RAX=EIP
    h.append(RAX)
    PRT('7439101573')
    RBX=EIP
    h.append(RBX)
    PRT('5308871538')
    RCX=EIP
    h.append(RCX)
    PRT('7068448058')
    RDX=EIP
    h.append(RDX)
    PRT('5654860415')
    REX=EIP
    h.append(REX)
    PRT('6895790220')
    RFX=EIP
    h.append(RFX)
    PRT('4823701931')
    RGX=EIP
    h.append(RGX)
    PRT('5836426521')
    RHX=EIP
    h.append(RHX)
    #加载words
    w=[]
    LOAD(0,1,2,3)
    w.append(EIP)
    LOAD(4,5,6,7)
    w.append(EIP)
    LOAD(8,9,10,11)
    w.append(EIP)
    LOAD(12,13,14,15)
    w.append(EIP)
    LOAD(16,17,18,19)
    w.append(EIP)
    LOAD(20,21,22,23)
    w.append(EIP)
    LOAD(24,25,26,27)
    w.append(EIP)
    LOAD(28,29,30,31)
    w.append(EIP)
    PRT('6442450944')
    w.append(EIP)
    PRT('4294967296')
    w.append(EIP)
    PRT('4294967296')
    w.append(EIP)
    PRT('4294967296')
    w.append(EIP)
    PRT('4294967296')
    w.append(EIP)
    PRT('4294967296')
    w.append(EIP)
    PRT('4294967296')
    w.append(EIP)
    PRT('4294967552')
    w.append(EIP)
    #大洗牌！
    for t in range (16,64):
        sigma1(w[t-2])
        ESP=EIP
        sigma0(w[t-15])
        MOD(ESP,EIP)
        MOD(EIP,w[t-7])
        MOD(EIP,w[t-16])
        w.append(EIP)
    for t in range (0,64):
        Sigma1(REX)
        RSP=EIP
        Ch(REX,RFX,RGX)
        MOD(RSP,EIP)
        MOD(RHX,EIP)
        MOD(w[t],EIP)
        MOD(EIP,Q+t)
        T1=EIP
        Sigma0(RAX)
        RSP=EIP
        Maj(RAX,RBX,RCX)
        MOD(RSP,EIP)
        T2=EIP
        RHX=RGX
        RGX=RFX
        RFX=REX
        MOD(RDX,T1)
        REX=EIP
        RDX=RCX
        RCX=RBX
        RBX=RAX
        MOD(T1,T2)
        RAX=EIP
    H=[]
    MOD(RAX,h[0])
    H.append(EIP)
    MOD(RBX,h[1])
    H.append(EIP)
    MOD(RCX,h[2])
    H.append(EIP)
    MOD(RDX,h[3])
    H.append(EIP)
    MOD(REX,h[4])
    H.append(EIP)
    MOD(RFX,h[5])
    H.append(EIP)
    MOD(RGX,h[6])
    H.append(EIP)
    MOD(RHX,h[7])
    H.append(EIP)
    OUTPUT([DUMP(H[0]),DUMP(H[1]),DUMP(H[2]),DUMP(H[3]),DUMP(H[4]),DUMP(H[5]),DUMP(H[6]),DUMP(H[7])])
    return
with open('lgklx_input.py','w') as file:

    file.write("from pwn import *\n")
    '''file.write("import subprocess\n")
    file.write("p=process(['python','lgklx_testing.py'])\n")'''
    file.write('p = remote("202.38.93.141", 10094)\n')
    file.write('p.recvuntil(b"token:")\n')
    file.write('p.sendline(b"1:MEYCIQDPvuDMCIJsufFjqavyJZ3ooYVVMyl9VTWO8e6VENQU6wIhALodATitRMxAaj1h4I2eU4VLQRlaGOXk41ZZ97P3+JIK")\n')
    file.write('p.recvuntil(b"Your program:")\n')
    #常量数据段
    EIP=31
    PRT('0')
    I=EIP+1
    PRT('0.375')
    PRT('0.875')
    PRT('1.875')
    PRT('3.875')
    PRT('7.875')
    PRT('15.875')
    PRT('31.875')
    PRT('63.875')
    PRT('127.875')
    PRT('255.875')
    PRT('511.875')
    PRT('1023.875')
    PRT('2047.875')
    PRT('4095.875')
    PRT('8191.875')
    PRT('16383.875')
    PRT('32767.875')
    PRT('65535.875')
    PRT('131071.875')
    PRT('262143.875')
    PRT('524287.875')
    PRT('1048575.875')
    PRT('2097151.875')
    PRT('4194303.875')
    PRT('8388607.875')
    PRT('16777215.875')
    PRT('33554431.875')
    PRT('67108863.875')
    PRT('134217727.875')
    PRT('268435455.875')
    PRT('536870911.875')
    PRT('1073741823.875')
    PRT('2147483647.875')
    PRT('4294967295.875')
    PRT('8589934591.875')
    PRT('8589934591.875')
    PRT('17179869183.875')
    PRT('34359738367.875')
    PRT('68719476735.875')
    PRT('137438953471.875')
    PRT('274877906943.875')
    PRT('549755813887.875')
    PRT('1099511627775.875')
    PRT('2199023255551.875')
    PRT('4398046511103.875')
    PRT('8796093022207.875')
    PRT('17592186044415.875')
    PRT('35184372088831.875')
    PRT('70368744177663.875')
    PRT('140737488355327.88')
    PRT('281474976710655.88')
    PRT('562949953421311.9')
    PRT('1125899906842623.9')
    PRT('2251799813685248.0')
    PRT('4503599627370496.0')
    J=EIP
    PRT('1')
    PRT('2')
    PRT('4')
    PRT('8')
    PRT('16')
    PRT('32')
    PRT('64')
    PRT('128')
    PRT('256')
    PRT('512')
    PRT('1024')
    PRT('2048')
    PRT('4096')
    PRT('8192')
    PRT('16384')
    PRT('32768')
    PRT('65536')
    PRT('131072')
    PRT('262144')
    PRT('524288')
    PRT('1048576')
    PRT('2097152')
    PRT('4194304')
    PRT('8388608')
    PRT('16777216')
    PRT('33554432')
    PRT('67108864')
    PRT('134217728')
    PRT('268435456')
    PRT('536870912')
    PRT('1073741824')
    PRT('2147483648')
    K=EIP+1
    PRT('-4503599627370496')
    PRT('-9007199254740992')
    PRT('-18014398509481984')
    PRT('-36028797018963968')
    PRT('-72057594037927936')
    PRT('-144115188075855872')
    PRT('-288230376151711744')
    PRT('-576460752303423488')
    PRT('-1152921504606846976')
    PRT('-2305843009213693952')
    PRT('-4611686018427387904')
    PRT('-9223372036854775808')
    PRT('-18446744073709551616')
    PRT('-36893488147419103232')
    PRT('-73786976294838206464')
    PRT('-147573952589676412928')
    PRT('-295147905179352825856')
    PRT('-590295810358705651712')
    PRT('-1180591620717411303424')
    PRT('-2361183241434822606848')
    PRT('-4722366482869645213696')
    PRT('-9444732965739290427392')
    PRT('-18889465931478580854784')
    PRT('-37778931862957161709568')
    PRT('-75557863725914323419136')
    PRT('-151115727451828646838272')
    PRT('-302231454903657293676544')
    PRT('-604462909807314587353088')
    PRT('-1208925819614629174706176')
    PRT('-2417851639229258349412352')
    PRT('-4835703278458516698824704')
    PRT('-9671406556917033397649408')
    PRT('-19342813113834066795298816')
    PRT('-38685626227668133590597632')
    L=EIP+1
    PRT('4503599627370496')
    PRT('9007199254740992')
    PRT('18014398509481984')
    PRT('36028797018963968')
    PRT('72057594037927936')
    PRT('144115188075855872')
    PRT('288230376151711744')
    PRT('576460752303423488')
    PRT('1152921504606846976')
    PRT('2305843009213693952')
    PRT('4611686018427387904')
    PRT('9223372036854775808')
    PRT('18446744073709551616')
    PRT('36893488147419103232')
    PRT('73786976294838206464')
    PRT('147573952589676412928')
    PRT('295147905179352825856')
    PRT('590295810358705651712')
    PRT('1180591620717411303424')
    PRT('2361183241434822606848')
    PRT('4722366482869645213696')
    PRT('9444732965739290427392')
    PRT('18889465931478580854784')
    PRT('37778931862957161709568')
    PRT('75557863725914323419136')
    PRT('151115727451828646838272')
    PRT('302231454903657293676544')
    PRT('604462909807314587353088')
    PRT('1208925819614629174706176')
    PRT('2417851639229258349412352')
    PRT('4835703278458516698824704')
    PRT('9671406556917033397649408')
    PRT('19342813113834066795298816')
    PRT('38685626227668133590597632')
    M=EIP
    PRT('-4294967296.0')
    PRT('4294967296.0')
    PRT('12884901887.0')
    PRT('9.536743162952277e-07')
    PRT('1.9073486325904554e-06')
    N=EIP
    PRT('-1.1102230246251565e-16')
    PRT('-2.220446049250313e-16')
    PRT('-4.440892098500626e-16')
    PRT('-8.881784197001252e-16')
    PRT('-1.7763568394002505e-15')
    PRT('-3.552713678800501e-15')
    PRT('-7.105427357601002e-15')
    PRT('-1.4210854715202004e-14')
    PRT('-2.842170943040401e-14')
    PRT('-5.684341886080802e-14')
    PRT('-1.1368683772161603e-13')
    PRT('-2.2737367544323206e-13')
    PRT('-4.547473508864641e-13')
    PRT('-9.094947017729282e-13')
    PRT('-1.8189894035458565e-12')
    PRT('-3.637978807091713e-12')
    PRT('-7.275957614183426e-12')
    PRT('-1.4551915228366852e-11')
    PRT('-2.9103830456733704e-11')
    PRT('-5.820766091346741e-11')
    PRT('-1.1641532182693481e-10')
    PRT('-2.3283064365386963e-10')
    PRT('-4.656612873077393e-10')
    PRT('-9.313225746154785e-10')
    PRT('-1.862645149230957e-09')
    PRT('-3.725290298461914e-09')
    PRT('-7.450580596923828e-09')
    PRT('-1.4901161193847656e-08')
    PRT('-2.9802322387695312e-08')
    PRT('-5.960464477539063e-08')
    PRT('-1.1920928955078125e-07')
    PRT('-2.384185791015625e-07')
    PRT('-4.76837158203125e-07')
    PRT('-9.5367431640625e-07')    
    Q=EIP+1
    LIST=[5411319704, 6194414737, 7344290767, 8215976869, 5256954459, 5803938289, 6748603044, 7165730517, 7919348376, 4605565697, 4902192574, 5721849283, 6220045684, 6457045502, 6909855399, 7543189876, 8130357697, 8317192070, 4559314374, 4899774924, 5065223279, 5544117418, 5850048988, 6291032282, 6849188178, 7116801645, 7247964104, 7505280967, 7631539187, 7879496007, 4408894289, 4633209191, 4961274501, 5068497208, 5589724668, 5691149587, 5990150996, 6281628347, 6471993646, 6751923333, 7025453217, 7115269707, 7554698096, 7640732067, 7811033113, 7895320100, 8389539205, 4570390640, 4725195030, 4801915912, 4954027852, 5178965173, 5253106867, 5617789514, 5831969359, 6042841075, 6250529518, 6319072111, 6522697748, 6656819720, 6723403770, 7051701483, 7498998775, 7624292594]
    for i in LIST:
        PRT('{}'.format(i))

    #写好的程序放这里呀！
    sha256_float()    
    PRT('EOF')
    file.write("p.interactive()")
print("COMPILED!")

```
