import random
from random import choice, randint

#Get the word from the Nato_Dict regardless of cap
def GetWord(c):
    return Nato_Dict[c.capitalize()]

#Convert the final string to Leet Speak
def LeetSpeak(s):
    leet_s = []
    s1 = ''
    for i in range(len(s)):
        if i % 2 == 1 and i != 0 and s[i].capitalize() in Leet_Dict:
            letter = Leet_Dict[s[i].capitalize()]
            leet_s.append(letter)
        else:
            leet_s.append(s[i])
    return s1.join(leet_s)

#Construct the final string
def Construct(s1, s2, s3):
    final = []
    tmp = ''
    final.append(s1)
    sep_count = randint(1, 3)
    for i in range(sep_count):
        final.append(random.choice(seperators))
    final.append(s2)
    name_value = sum(bytearray(s3, 'utf8'))
    final.append(str(name_value))

    return tmp.join(final)

#Array of a few seperators between first and second words and different types of Y/N
seperators = ['-', '_', '=', '~']
yesses = ['Y' , 'y', 'yes', 'YES']
nos = ['N', 'n', 'no', 'NO']

Nato_Dict = {
    'A':'Alpha', 
    'B':'Bravo',
    'C':'Charlie', 
    'D':'Delta', 
    'E':'Echo', 
    'F':'Foxtrot', 
    'H':'Hotel',
    'G':'Golf', 
    'I':'India', 
    'J':'Juliet', 
    'K':'Kilo', 
    'L':'Lima', 
    'M':'Mike', 
    'N':'November', 
    'O':'Oscar', 
    'P':'Papa', 
    'Q':'Quebec', 
    'R':'Romeo', 
    'S':'Sierra', 
    'T':'Tango', 
    'U':'Uniform', 
    'V':'Victor', 
    'W':'Whiskey', 
    'X':'Xray', 
    'Y':'Yankee', 
    'Z':'Zulu'
    }

Leet_Dict = {
    'A':'@', 
    'B':'13',
    'C':'(', 
    'D':')', 
    'E':'&', 
    'F':'/=', 
    'G':'6', 
    'H':'|-|',
    'I':'!', 
    'J':'J', 
    'K':'|<', 
    'L':'L', 
    'M':'|Y|', 
    'N':'/\/', 
    'O':'0', 
    'P':'|>', 
    'Q':'Q', 
    'R':'R', 
    'S':'5', 
    'T':'7', 
    'U':'[_]', 
    'V':'\/', 
    'W':'\^/', 
    'X':'X', 
    'Y':'y', 
    'Z':'2',
    '0':'0',
    '1':'1',
    '2':'2',
    '3':'3',
    '4':'4',
    '5':'5',
    '6':'6',
    '7':'7',
    '8':'8',
    '9':'9',
    '-':'-'
    }


while True:
    #Get the Names
    website = str(input("Website Name: "))
    name = str(input("First OR Last Name: "))

    #Create whats passed to constructor
    first = GetWord(website[0])
    second = GetWord(website[randint(1, len(website) - 1)])

    #Create the final password
    fin = Construct(first, second, name)
    print("Your Decrypted Password is: " + fin)
    print("Your Encrypted Password is: " + LeetSpeak(fin))

    #Loop as many as the user would like
    rep = input("Would you like to construct another password(Y/N)?: ")
    if rep in yesses:
        continue
    if rep in nos:
        break
       
