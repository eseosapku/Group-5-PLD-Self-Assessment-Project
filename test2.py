user_data = {}

name = input('Welcome to Assessment-Buddy. \nThis app is aimed to help students who face difficulties with self-assessment and do not know how to perform precise and accurate evaluation of their work as self-directed learners. \nplease type down your name to begin \n'  )
S = input(f' What subject would you like to self assess on today {name} \n')


def get_questions():
    num = int(input("How many questions do want to record: \n"))
    questions ={}

    for i in range(num):
        q = input("Enter the question: ")
        a = input("Enter the answer: ")
        print("\n")
        questions[q]=a


    print("Here are the question and the answers")
    nu = 1 
    for key,value in questions.items():
        print(f'{nu} : Question:{key} : Answer:{value} \n')
        nu +=1 

    return questions


def get_subjects():
    num = int(input("How many subjects do you wish to self asess on today: "))
    subjects = []

    for i in range(num):
        s = input("Enter subject: \n")
        subjects.append(s)


    return subjects

def get_user_input():
    subjects = get_subjects()
    
    
    for i in subjects:
        question_answer = get_questions()
        user_data[i]=question_answer


get_user_input()


'''.

this is the end result of the code 
user_data = {
    subject:{
        question:answer,
        question:answer,    
    }
}
'''