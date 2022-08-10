from bdb import effective
from optparse import Values
from Bio import name
from Bio import S
questions = dict() #empty dict
Subject = dict()

num = input("How many questions do you want to record  \n" ) #user tells the range(optional)
dig = int(num) - 1

    

for i in range(int(num)):
    n = input("Enter a  question: \n")#asking for input of 1 value
    p = input("Enter the answer to the question: \n")#asking for input of 1 value
    questions[n]=p#adding that value to the list




print(" \n \n*************Here are your listed questions and Answers****************")
for i in range(int(num)):
        fin = int(num) - int(dig)
        dig = int(dig) - 1
        for key, values in questions.items(): 
            print(f"Que{fin}) {key}= \nAns{fin}) {values} \n")
            break;

Subject[S]=questions
     

Add_que = input('**********Would you like to add more questions*********** \n SELECT Yes OR No \n')
if Add_que == 'No':
    for key, values in Subject.items():
        print(f" \n***********The Subject: {str.capitalize(key)}**************" )
        for key, values in questions.items():
           print(f"Que) {key}-- \nAns) {values} \n")
        
