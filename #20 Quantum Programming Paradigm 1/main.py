import numpy as np
import random

n = 4
test_instructions = [
    "NOT 4",
    "HAD 1","HAD 2","HAD 3","HAD 4",
    "CNOT 2 4",
    "HAD 1","HAD 2","HAD 3","HAD 4",
]

class QuantumSimulator:
    def __init__(self, n):
        self.n = n
        self.statevector = np.zeros(2 ** self.n, dtype = int)
        self.statevector[0] = 1
        self.const_times = 0
    def NOT (self, i):
        pos = self.n - i
        for state in range(1 << self.n):
            if not (state & (1 << pos)): # 这一位是0 This digit is zero
                target_state = state | (1 << pos) # 这里其实用异或比较好 XOR is better here
                temp = self.statevector[target_state]
                self.statevector[target_state] = self.statevector[state]
                self.statevector[state] = temp

    def CNOT (self, ic, i):
        pos = self.n - i
        pos_ic = self.n - ic
        for state in range(1 << self.n):
            if (not (state & (1 << pos))) and (state & (1 << pos_ic)):
                target_state = state | (1 << pos)
                temp = self.statevector[target_state]
                self.statevector[target_state] = self.statevector[state]
                self.statevector[state] = temp

    def CCNOT (self, ic1 ,ic2, i):
        pos = self.n - i
        pos_ic1 = self.n - ic1
        pos_ic2 = self.n - ic2
        for state in range(1 << self.n):
            if (not (state & (1 << pos))) and (state & (1 << pos_ic1)) and (state & (1 << pos_ic2)):
                target_state = state | (1 << pos)
                temp = self.statevector[target_state]
                self.statevector[target_state] = self.statevector[state]
                self.statevector[state] = temp

    def HAD (self, i): #不加上二分之根号二，之后补上 we consider the 1/2 separatly
        pos = self.n - i
        oldstate = self.statevector.copy()
        self.const_times +=1
        for state in range(1 << self.n):
            target_state = state ^ (1 << pos)
            if not (state & (1 << pos)):
                self.statevector[state] += oldstate[target_state]
            else:
                self.statevector[state] -= oldstate[target_state]
                self.statevector[state] *= -1

    def READALL(self):
        print(f"const:(1/2)^{self.const_times}")
        for state in range(1 << self.n):
            idx = f"{state:0{self.n}b}"
            amplitude_val = self.statevector[state]

            # 为了美观，我们只打印非零的振幅
            if amplitude_val != 0:
                print(f"|{idx}> : {amplitude_val.real ** 2}")

def run_sim (instructions, n):
    sim = QuantumSimulator(n)
    for line in instructions:
        parts = line.split() # These are quite new to me lol
        cmd = parts[0]
        args = [int(x) for x in parts[1:]]
        if cmd == "HAD":
            sim.HAD(args[0])
        elif cmd == "CNOT":
            sim.CNOT(args[0], args[1])
        elif cmd == "NOT":
            sim.NOT(args[0])
        elif cmd == "CCNOT":
            sim.CCNOT(args[0], args[1], args[2])
    sim.READALL()

run_sim(test_instructions, n)


"""
    不能这么写 不然会覆盖掉 CANNOT write like this
    def HAD (self, i): #不加上二分之根号二，之后补上
        pos = self.n - i
        self.const_times +=1
        for state in range(1 << self.n):
        target_state = state ^ (1 << pos)
        if not (state & (1 << pos)):
            self.statevector[state] += self.statevector[target_state]
        else:
            self.statevector[state] -= self.statevector[target_state]
    
    def READALL (self):
        for state in range(1 << self.n):
            idx = f"n;0{state}b"
            print("|" + idx + "> : (1/sqrt(2))^%d * &d" %(self.const_times, self.statevector[state]))
"""



