user_data = {}


def get_questions():
    num = int(input("how many question: "))
    questions ={}

    for i in range(num):
        q = input("Enter question: ")
        a = input("Enter answer: ")
        print("\n")
        questions[q]=a


    print("Here are the question and the answers")
    nu = 1 
    for key,value in questions.items():
        print(f'{nu} : Question:{key} : Answer:{value}')
        nu +=1 

    return questions

def get_subjects():
    num = int(input("how many subjects do you do today: "))
    subjects = []

    for i in range(num):
        s = input("Enter subject: ")
        subjects.append(s)


    return subjects

def get_user_input():
    subjects = get_subjects()
    
    
    for i in subjects:
        quesion_answer = get_questions()
        user_data[i]=quesion_answer


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