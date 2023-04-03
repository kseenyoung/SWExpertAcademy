T = int(input())
table = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
for test in range(1, T+1):
    print("#"+str(test), end=' ')
    string = input()
    zinsu = []

    for s in string:
        binary = bin(table.index(s))[2:]
        zinsu.append(binary if len(binary) == 6 else (6-len(binary))*'0'+binary)
    zinsu = ''.join(zinsu)

    for i in range(0, len(zinsu), 8):
        print(chr(int(zinsu[i:i+8], 2)), end='')
    print()