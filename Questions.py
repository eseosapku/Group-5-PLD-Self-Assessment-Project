from optparse import Values


questions = dict() #empty dict

num = input("How many questions do you want to record  \n" ) #user tells the range(optional)

#iterating till user's range is reached
for i in range(int(num)): 
    n = input("Enter a  question: \n")#asking for input of 1 value
    p = input("Enter the answer to the question: \n")#asking for input of 1 value
    questions[n]=p#adding that value to the list


print("*************Here are your listed questions and Answers****************: ")
for key, values in questions.items():
    print(key, " = ", values)




