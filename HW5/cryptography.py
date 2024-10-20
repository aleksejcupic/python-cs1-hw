# description: A program to encrypt and decrypt a code using the Vigenere cipher
# name: Cupic, Aleksej
# date: 10.02.19

# functions (1 for cleanup, 2 for encryption, 3 for decryption)
def cleanup(msg):
    msg=msg.upper()
    cleanmsg=''
    for i in range(len(msg)):
        if ord(msg[i])>=65 and ord(msg[i])<=90:
            cleanmsg=cleanmsg+msg[i]
    print('The cleaned message is: ',cleanmsg)
    return(cleanmsg)

def encrypt(cleanmsg):
    encrypt=''
    for j in range(len(cleanmsg)):
        encrypt=encrypt+chr((ord(cleanmsg[j])+ord(key[j]))%26+65)
    print('The encrypted message is: ',encrypt)
    return(encrypt)

def decrypt(encrypt):
    decrypt=''
    for k in range(len(encrypt)):
        decrypt=decrypt+chr((ord(encrypt[k])-ord(key[k])+26)%26+65)
    print('The decrypted message is: ',decrypt)

# main

print('A program to encrypt and decrypt a code using the Vigenere cipher')
msg=str(input('Enter a message to be encrypted and then decrypted: '))
key=str(input('Enter the encryption key: '))
cleanmsg=cleanup(msg)
key=key*(len(cleanmsg))
encrypt=encrypt(cleanmsg)
decrypt(encrypt)
print('Encryption/Decryption complete')

# end
