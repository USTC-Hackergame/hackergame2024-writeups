import subprocess

p = subprocess.run(["nm"], stdout=subprocess.PIPE)

leq_exit_true = {}
leq_exit_false = {}
with open("offsets.py", "w") as f:
    f.write("from collections import defaultdict\n")
    f.write("offset_leq_exit_true = defaultdict(int)\n")
    f.write("offset_leq_exit_false = defaultdict(int)\n")
    for line in p.stdout.decode().splitlines():
        if line.startswith(" " * 8):
            continue
        offset, t, name = line.split()
        if t == "t" and name.startswith('_'):
            if name.startswith("_leq_exit_true"):
                leq_exit_true[int(name[len("_leq_exit_true_"):])] = '0x' + offset
            elif name.startswith("_leq_exit_false"):
                leq_exit_false[int(name[len("_leq_exit_false_"):])] = '0x' + offset
            else:
                f.write(f"offset{name} = 0x{offset}\n")

    f.write(f'offset_leq_exit_true = {leq_exit_true}\n')
    f.write(f'offset_leq_exit_false = {leq_exit_false}\n')
        