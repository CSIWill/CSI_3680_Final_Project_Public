from random import randint, getrandbits
from math import gcd
import os
from pypdf import PdfReader,PdfWriter

# primality test
# using Miller-Rabin primality test because we need large prime numbers quickly
# will do 100 iterations of the test to improve accuracy

def primality_test(generateNumber):
    #  prime numbers are greater than 1
    if generateNumber == 1:
        return False
    # 2 is prime
    elif generateNumber == 2:
        return True
    # 3 is prime 
    elif generateNumber == 3:
        return True
    # all other even numbers are not prime
    elif generateNumber % 2 == 0:
        return False
    else:
        # q is our odd number such that primeNumber - 1 = 2^s * q
        q = generateNumber - 1
        # find largest power of 2 that divides primeNumber - 1
        s = 0
        while q % 2 == 0:
            s += 1
            q = q // 2
        # 100 Iterations of Miller-Rabin primality test
        for i in range(100):
            a = randint(2, generateNumber - 2)
            # a^q mod primeNumber = 1 or primeNumber - 1, not composite, check next a value
            check = pow(a, q, generateNumber)
            if check == 1 or check == generateNumber - 1:
                continue
            # check for each s value for composite trait where a^((2^s)*q) mod primeNumber = primeNumber - 1
            for j in range(s - 1):
                check = pow(check, 2, generateNumber)
                # if mod -1 returns composite
                if check == generateNumber - 1:
                    return False
            else:
                return False
        return True

# randomly generate prime numbers (1024 bits to ensure modulus will be at least 1024 bits)
def generate_prime_number():
    primeNumber = getrandbits(1024)
    # check random numbers are prime
    while not primality_test(primeNumber):
        primeNumber = getrandbits(1024)
        if primality_test(primeNumber):
            return primeNumber

def generate_key(e):
    # print("Please input a number for e, or press enter to use the default value 65537")
    try:
        # e = input("Enter a number: ")
        if e=="":
            e = 65537
        elif e=="0":
            e = generate_prime_number()
        else:
            e = int(e)
    except:
        print("Error: invalid input")
        exit()
    try:
        p = generate_prime_number()
        q = generate_prime_number()
        n = p * q
        z = (p-1)*(q-1)
        d = pow(e, -1, z)
    except:
        print("Error: failed to generate prime numbers")
        exit()

    try:
        while gcd(e, (p-1)*(q-1)) != 1:
            while n < 2**1024:
                p = generate_prime_number()
                q = generate_prime_number()
                n = p * q
                z = (p-1)*(q-1)
                d = pow(e, -1, z)
    except:
        print("Error: gcd(e, (p-1)*(q-1)) != 1")
        exit()

    publicKey = [e, n]
    privateKey = [d, n]
    writer = PdfWriter()
    # page = writer.addPage()
    file1 = open("publicKey.txt", "w")
    for i in publicKey:
        file1.write(str(i) + "\n")
    file2 = open("privateKey.txt", "w")
    for i in privateKey:
        file2.write(str(i) + "\n")
    file3 = open("key.pdf", "w")
    file3.write("p: {}\n".format(p))
    file3.write("q: {}\n".format(q))
    file3.write("n: {}\n".format(n))
    file3.write("z: {}\n".format(z))
    file3.write("e: {}\n".format(e))
    file3.write("d: {}\n".format(d))
    file3.write("Public Key: {}\n".format(publicKey))
    file3.write("Private Key: {}\n".format(privateKey)) 
    file1.close()
    file2.close()
    file3.close()
    # writer.write("Key.pdf")
    print("Keys have been generated, encrypt with your private key and send you public key")

def encrypt(e, n, message):
    # e, n = publicKey
    messageNum = []
    for i in range(len(message)):
        # convert each character to its ascii value
        messageNum.append(ord(message[i]))
    encryptedMessage = []
    for i in range(len(messageNum)):
        # encrypt each ascii value
        encryptedMessage.append(pow(messageNum[i], e, n))

    return encryptedMessage

def decrypt(d, n, encryptedMessage):
    # d, n = privateKey
    decryptedMessage = []  
    for i in range(len(encryptedMessage)):
        # decrypt each ascii value
        decryptedMessage.append(pow(encryptedMessage[i], d, n))
    decryptedMessageChar = []
    for i in range(len(decryptedMessage)):
        # convert each ascii value to its character
        decryptedMessageChar.append(chr(decryptedMessage[i]))
    return "".join(decryptedMessageChar)

# encrypt with private key to send to another user
def encrypt_file(toEncryptPath, encryptionKey):    
    try:
        toEncrypt = os.path.split(toEncryptPath)
        eKey = os.path.split(encryptionKey)
        os.chdir(eKey[0])
        if os.path.splitext(toEncrypt[1])[1] == ".txt":
            encryptWith = open(eKey[1], "r")
            e, n = encryptWith.readlines()
            e = int(e)
            n = int(n)
            os.chdir(toEncrypt[0])
            file = open(toEncrypt[1], "r")
            message = file.read()
            encryptedMessage = encrypt(e, n, message)
            file.close()
            file_1 = open("Encrypted - " + toEncrypt[1], "w")
            for i in encryptedMessage:
                file_1.write(str(i) + "\n")
            file_1.close()
        else:
            encryptWith = open(eKey[1], "r")
            e, n = encryptWith.readlines()
            e = int(e)
            n = int(n)
            os.chdir(toEncrypt[0])
            reader = PdfReader(toEncrypt[1])
            page = reader.pages[0]
            print(page.extract_text())
            message = page.extract_text()
            encryptedMessage = encrypt(e, n, message)
            file_1 = open("Encrypted - " + toEncrypt[1].rstrip(".pdf") + ".txt", "w")
            for i in encryptedMessage:
                file_1.write(str(i) + "\n")
            file_1.close()
    except:
        print("Error: invalid input")
        exit()

def decrypt_file(toDecryptPath, decryptionKey):
    try:
        toDecrypt = os.path.split(toDecryptPath)
        dKey = os.path.split(decryptionKey)
        os.chdir(dKey[0])
        decryptWith = open(dKey[1], "r")
        d, n = decryptWith.readlines()
        d = int(d)
        n = int(n)
        os.chdir(toDecrypt[0])
        file_1 = open(toDecrypt[1], "r")
        file_2 = open("Decrypted - " + toDecrypt[1], "w")
        encryptToDecrypt = file_1.readlines()
        for i in range(len(encryptToDecrypt)):
            encryptToDecrypt[i] = int(encryptToDecrypt[i])
        decryptedMessage = decrypt(d, n, encryptToDecrypt)
        file_2.write(decryptedMessage)
        file_2.close()
        file_1.close()
    except:
        print("Error: invalid input")
        exit()
