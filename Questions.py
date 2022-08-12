from bdb import effective
from optparse import Values
from Bio import name
from Bio import S
ans = dict()
questions = dict() #empty dict
Subject = dict()

num = input("How many questions do you want to record  \n" ) #user tells the range(optional)
dig = int(num) - 1

    

for i in range(int(num)):
    n = input("Enter a  question: \n")#asking for input of 1 value
    p = input("Enter the answer to the question: \n")#asking for input of 1 value
    k = input('Enter the keywords the system would use to check your answer to the question \n')
    questions[n]=p#adding that value to the list
    ans[k]=n



print(" \n \n*************Here are your listed questions and Answers****************")
fin = 1
for key, values in questions.items(): 
    print(f"Que{fin}) {key}= \nAns{fin}) {values} \n")
    fin += 1

Subject[S]=questions
   

Add_que = input('**********Would you like to add more questions*********** \n SELECT Yes OR No \n')
if Add_que == 'No' or 'no':
    for key, values in Subject.items():
        print(f" \n***********The Subject: {str.capitalize(key)}**************" )
        for key, values in questions.items():
           print(f"Que) {key}-- \nAns) {values} \n")
        

print('Let us begin the self assessment')

for key, values in questions.items(): 
    print(f"Que) {key}= \n")
    answer = input('Type the answer \n')
    if answer in ans:
        print('correct')
    else:
        print('Incorrect')
        print(f'correct answer is {values}')
