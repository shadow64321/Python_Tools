from sys import argv
import base64, os

def Encrypt(x):
    Encoded_Bytes = base64.b64encode(x.encode())
    f = open('Output.txt', 'w')
    f.write(Encoded_Bytes)
    f.close

def Decrypt(x):
    if os.isfile('Output.txt'):
        f = open('Output.txt', 'r')
        Encrypted_Str = f.read()
        Decoded_Str = base64.b64decode(Encrypted_Str.decode())
    else:
        print('No output file detected')
        exit


Usr_Input = argv[1]
Opt = argv[2]
if Opt == 'EnC':
    Encrypt()
elif Opt == 'DeC':
    Decrypt()
else:
    print('"Arg 2" is not recongnised - Can only be: EnC: Encode, or DeC: Decode')
    exit