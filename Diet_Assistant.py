import os
import json

BMR = 1619

def Check_BMR():
    if os.path.isfile('BMR.json'):
        f = open('BMR.json', 'r')
        y = f.readline()                               
        print('You have ' + y + ' calories remaining')
    else:
        print('Error: Log file corrupted or removed')
        exit

def Reset_Daily_BMR():                                          
    if os.path.isfile('BMR.json'):                              
        Write_Data(BMR)
        print('Calories Reset')                                 
        print('GOOD LUCK TODAY! : )')
    else:
        print('Error: Log file corrupted or removed')
        exit

def Write_Data(x):
        f = open('BMR.json', 'w')
        f.write(json.dumps(x))
        f.close()

def Read_Data():
    f = open('BMR.json', 'r')
    x = int(f.readline())
    print(x)
    Calculate_Cal_Remaining(x)



def Calculate_Cal_Per_Serve():
    Serves = float(input('How many serves? '))
    Cal = int(input('How many calories per serve? '))
    print(Cal * Serves)

def Calculate_Cal_Remaining(data):
    Usr_Input = int(input('How many calories in your last meal? '))
    if data != 0:
        Usr_BMR = data - Usr_Input
    else:
        Usr_BMR = BMR - Usr_Input
    print('Total daily calories: ' + str(BMR))
    print('Remaining calories: ' + str(Usr_BMR))
    Write_Data(Usr_BMR)


# Main
print('1) Calculate calories per serve')
print('2) Calculate calories remaining')
print('3) Reset daily calore count')
print('4) Check how many calories you have left')
print('5) Exit')

Selection = input('Enter the corresponding number: ')
if '1' in Selection:
    Calculate_Cal_Per_Serve()
elif '2' in Selection:
    if os.path.isfile('BMR.json'):
    	Read_Data()
    else:
        Write_Data(BMR)
elif '3' in Selection:
    Reset_Daily_BMR()
elif '4' in Selection:
    Check_BMR()
elif '5' in Selection:
    exit
else:
    print('Error: Input Incorrect')
