#CTF ENKRIPSI (SIMPLE AJA)

flag = "CTF{INI_FLAG_NGUAWOR_1abasjaj91928103091ajkkj1181301839}"


def encrypt(number):
    return (number**4) +  (2*number**3) + (3*number**2) + (4*number) + 5


enc = []
n = 1
for data in flag:
    a = ord(data)
    enx =  encrypt(a)
    enc.append(enx)
    n = n+ 1
print(enc)
    
def solve(array):
    flag = ""
    for data in array:
        for i in range (0,127,+1):
            idk = encrypt(i)
            if idk == data :
                flag += chr(i)
            else :
                None
    print(flag)
solve(enc)
