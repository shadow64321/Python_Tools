import os, json, random

def Print_Menu():
    print('1) Run Choice De-paralyser')
    print('2) Edit Catagories')
    print('3) Edit Choices')

def Randomise(file):
    f = open(file, 'r')
    x = f.readline()
    counter = 0
    for i in x:
        if ',' in i:
            counter = counter + 1
    y = random.randint(0, counter - 1)
    temp_string = ''
    empty_string = ''
    temp_list = []

    for i in x:
        if ',' not in i:
            temp_string = str(temp_string) + str(i)
            temp_string.strip()
        else:
            temp_list.append(temp_string)
            temp_string = empty_string
    print('You should do: ' + temp_list[y].replace('"', ''))
    f.close()

def Setup():
    if os.path.isfile('Choices.json'):
        Choices_File = open('Choices.json', 'a')
        Usr_Input = input('What Choices Would You like to add? ')
        x = json.dumps(Usr_Input, separators=(','))
        Choices_File.write(x)
        Choices.File.close()
        
    else:    
        Choices_File = open('Choices.json', 'w')
        Usr_Input = input('Please enter all catagories of things you may wish to do (Able to be changed later)(Must be seperated by ", "): ')
        x = json.dumps(Usr_Input, separators=(', '))
        Choices_File.write(x)
        Choices_File.close()
    

def Edit_Choices(file):
   f_read = open(file, 'r')
   y = f_read.readline().replace(',', '')
   z = y.replace('"', '')
   print(z)
   f_read.close()
   New_Choices = str(input('What choices do you wish to add? '))
   dump_str = New_Choices + ','
   x = json.dumps(dump_str, separators=(', '))
   f = open(file, 'a')
   f.write(x)
   f.close()


# Main
Print_Menu()
Answer = int(input('Select an operation: '))
if 1 == Answer:
    if os.path.isfile('Choices.json'):
        Choices_File = open('Choices.json', 'r')
        Choices = Choices_File.readline().replace(',', '')
        a = Choices.replace('"', '')
        print('Your Choices are: ')
        print(a)
        Usr_Input = input('What sounds interesting? ')
        if Usr_Input in Choices:
            #Search for file with same name
            File_Name = Usr_Input + '.json'
            if os.path.isfile(File_Name):
                Rel_File = open(File_Name, 'r')
                Randomise(File_Name)
                Rel_File.close()
            else:
                # if it doesn't exist make it
                Rel_File = open(File_Name, 'w')
                Rel_Input = input(f'What choices would you like to put into {Usr_Input}? ')
                temp_dump_string = Rel_Input + ','
                x = json.dumps(Rel_Input, separators=(', '))
                Rel_File.write(x)
                Rel_File.close()
        else:
            print('Invalid Input')
    else:
        Setup()
elif 2 == Answer:
    Setup()

elif 3 == Answer:
    Choices_File = open('Choices.json', 'r')
    x = Choices_File.readline().replace(',', '')
    a = x.replace('"', '')
    print(a)
    Usr_Input = input('Which catagory do you wish to edit? ')
    File = str(Usr_Input) + '.json'
    Edit_Choices(File)
