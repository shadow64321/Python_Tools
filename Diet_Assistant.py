import os, json

# BMR = 1619

def Check_BMR():
    if os.path.isfile('BMR.json'):
        f = open('BMR.json', 'r')
        y = f.readline()
        f.close()                               
        print('You have ' + y + ' calories remaining')
    else:
        print('Error: Log file corrupted or removed')
        exit

def Reset_Daily_BMR():                                          
    if os.path.isfile('BMR.json') & os.path.isfile('Goal.json'):
        f_BMR = open('BMR.json', 'w')
        f_Goal = open('Goal.json', 'r')
        Goal = f_Goal.readline()
        f_BMR.write(json.dumps(int(Goal)))
        f_BMR.close()
        f_Goal.close()
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
    f.close()
    print(x)
    Calculate_Cal_Remaining(x)
    
    
def Change_Goal(y):
    f = open('Goal.json', 'w')
    f.write(json.dumps(int(y)))
    f.close()

def First_Time_Setup():
    Goal = int(input('What would you like your daily calorie goal to be? '))
    Change_Goal(Goal)
    if os.path.isfile('Goal.json'):
        f_BMR = open('BMR.json', 'w')
        f_Goal = open('Goal.json', 'r')
        Goal = f_Goal.readline()
        f_BMR.write(json.dumps(int(Goal)))
        f_BMR.close()
        f_Goal.close()

def Calculate_Cal_Per_Serve():
    Serves = float(input('How many serves? '))
    Cal = int(input('How many calories per serve? '))
    print(Cal * Serves)

def Calculate_Cal_Remaining(data):
    Usr_Input = int(input('How many calories in your last meal? '))
    Usr_BMR = data - Usr_Input
    
    print('Total daily calories: ' + str(Read_Data()))
    print('Remaining calories: ' + str(Usr_BMR))
    Write_Data(Usr_BMR)


# Main
print('1) Calculate calories per serve')
print('2) Calculate calories remaining')
print('3) Reset daily calore count')
print('4) Check how many calories you have left')
print('5) Fisrt time setup')
print('6) Exit')

Selection = input('Enter the corresponding number: ')
if '1' in Selection:
    Calculate_Cal_Per_Serve()
elif '2' in Selection:
    if os.path.isfile('BMR.json'):
        Read_Data()
    else:
        Write_Data(Read_Data())
elif '3' in Selection:
    Reset_Daily_BMR()
elif '4' in Selection:
    Check_BMR()
elif '5' in Selection:
    First_Time_Setup()
elif '6' in Selection:
    exit
else:
    print('Error: Input Incorrect')
