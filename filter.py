print("Wellcome to quiz game !!")
#print('NOTE: if your spelling is incorrect then it is considered as wrong answer')
score = 0
question_no = 0
playing = input('Do you want to play ? ').lower()
if playing == 'yes':
    question_no += 1
    ques = input(f'\n{question_no}. what does CPU stand for? ').lower()
    if ques == 'central processing unit':
        score += 1
        print('correct! you got 1 point')

    else:
        print('Incorrect!')
        print(f'current answer is --> central processing unit')

    ques = input(f'\n{question_no}. what does GPU stand for? ').lower()
    if ques == 'graphic processing unit':
        score += 1
        print('correct! you got 1 point')

    else:
        print('Incorrect!')
        print(f'current answer is --> central processing unit')
else:
    print("your anrwer is wrong")








