questions = list() #empty list

num = input("How many questions do you want to record") #user tells the range(optional)

#iterating till user's range is reached
for i in range(int(num)): 
    n = input("Enter a  question: ")#asking for input of 1 value 
    questions.append(n)#adding that value to the list

print("Here are your listed questions: ")
print(*questions, sep='\n')