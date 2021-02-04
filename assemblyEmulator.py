#Memory

RAM1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
RAM2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
RAM3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
RAM4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

splitar = []
result = []
inp = input()

def intParse(x):
    parsed = []
    x = int(x)
    while (x != 1):
        parsed.insert(0, x % 2)
        x = int(x / 2)
    parsed.insert(0, 1)
    while len(parsed) < 4:
        parsed.insert(0, 0)
    print(parsed)
    return parsed

def encoder(inp):
    global out
    out = ""
    if inp[:3] == "ADD":
        out += "1010"
        inp = inp.replace("ADD_", "")
    elif inp[:3] == "SUB":
        out += "1011"
        inp = inp.replace("SUB_", "")
    elif inp[:3] == "MUL":
        out += "1100"
        inp = inp.replace("MUL_", "")
    elif inp[:3] == "DIV":
        out += "1111"
        inp = inp.replace("DIV_", "")
    elif inp[:3] == "AND":
        out += "0001"
        inp = inp.replace("AND_", "")
    elif inp[:2] == "OR":
        out += "0010"
        inp = inp.replace("OR_", "")

    splitar = inp.split('_')
    print(out)
    print(splitar)
    splitOut = []
    for i in range(3):
        splitOut.append(intParse(splitar[i]))

    return splitOut

#ADD_03_02_07
#03_04_07
#03 "_" 04 "_" 07
#03 -> 0011, 04 -> 0100, 

print(encoder(inp))

#Logic gates

def AND(A,B):
    return (A == B) & (A != 0)

def OR(A,B):
    return A == 1 or B == 1

def XOR(A,B):
    return A != B and (A == 1 or B == 1)

def NAND(A,B):
    return A != 1 and B != 1

def NOT(A):
    if(A == 1 or A == True):
        return False
    else:
        return True

def NOR(A,B):
    return A == 0 and B == 0

def XNOR(A,B):
    return A == B


def adder(A,B,C):
    out2 = XOR( XOR(A,B), C)
    C = OR(AND(C, XOR(A,B) ), AND(A,B) )
    if (out2):
        out2 = 1
    else:
        out2 = 0
    result.insert(0, out2)

def excecuteAdder():
    C = 0
    output = encoder(inp)
    i = 3
    while i > 0:
        adder(output[0][i], output[1][i], C)
        i -= 1
    if (i == 0):
        result.insert(0, C)
    print("\nADDER RESULT: " + str(result))

def subtractor(A,B,Bo):
    out2 = XOR(XOR(A, B), Bo)
    Bo = OR(AND(NOT(XOR(A,B)), Bo), AND(NOT(A), B) )
    if (out2):
        out2 = 1
    else:
        out2 = 0
    result.append(out2)

def excecuteSubtractor():
    Bo = 0
    output = encoder(inp)
    i = 0
    while i < 3:
        subtractor(output[0][i], output[1][i], Bo)
        i += 1
    if (i == 3):
        result.append(Bo)


if (out == "1010"):
    excecuteAdder()
elif(out == "1011"):
    excecuteSubtractor()