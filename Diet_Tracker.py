import os

BMR = 1619

def Calculate_Cal_Per_Serve():
    Serves = float(input('How many serves? '))
    Cal = int(input('How many calories per serve? '))
    print(Cal * Serves)

def Calculate_Cal_Remaining():
    Usr_Input = int(input('How many calories in your last meal? '))
    Usr_BMR = BMR - Usr_Input
    print('Total daily calories: ' + str(BMR))
    print('Remaining calories: ' + str(Usr_BMR))

print('1) Calculate calories per serve')
print('2) Calculate calories remaining')
print('3) Exit')

Selection = input('Enter the corresponding number: ')
if '1' in Selection:
    Calculate_Cal_Per_Serve()
elif '2' in Selection:
    Calculate_Cal_Remaining()
elif '3' in Selection:
    exit
else:
    print('Error: Input Incorrect')

