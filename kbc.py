from questions import QUESTIONS
 
 
def isAnswerCorrect(i, answer):
    return True if QUESTIONS[i]['answer'] == answer else False
    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''
 
    #return True if answer == 2 else False      #remove this
 
 
def lifeLine(i):
    from random import choice
    print(f'\tQuestion {i+1}: {QUESTIONS[i]["name"]}' )
    print(f'\t\tOptions:')
    correct=QUESTIONS[i]['answer']
    l=[1,2,3,4]
    l.remove(correct)
    x=choice(l)
    if correct>x:
        print(f"\t\t\tOption {x}: {QUESTIONS[i]['option'+str(x)]}")
        print(f"\t\t\tOption {correct}: {QUESTIONS[i]['option'+str(correct)]}")
    else:
        print(f"\t\t\tOption {correct}: {QUESTIONS[i]['option'+str(correct)]}")
        print(f"\t\t\tOption {x}: {QUESTIONS[i]['option'+str(x)]}")      
    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
 
 
def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''
 
    #  Display a welcome message only once to the user at the start of the game.
    welcome=False
    if not welcome:
        print('Welcome to Kaun Banega Devsnest Champion Season 1')
        welcome=True
    
    #  For each question, display the prize won until now and available life line.
    lifeline_valid=True
    
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    game_play=True
    i=0
    while game_play:
        print('Lifelines left:',lifeline_valid)
        print(f'\tQuestion {i+1}: {QUESTIONS[i]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')
        if ans.lower()=='quit':
            if (i-1)<0:
                print('Amount won is 0')
            else:
                print(f"Total amount won is, {QUESTIONS[i-1]['money']}")
            game_play=False
            return
        elif ans.lower()=='lifeline' and lifeline_valid and i!=14:
            lifeLine(i)
            lifeline_valid=False
            ans=input('Your choice ( 1-4 ) : ')
            if ans.lower()=='quit':
                game_play=False
        elif ans.lower()=='lifeline' and lifeline_valid==False and i!=14:
            print('Your lifeline has been already used.')
        # check for the input validations
 
        if isAnswerCorrect(i, int(ans) ):
            # print the total money won.
            print('Total amount won is',QUESTIONS[i]['money'])
            # See if the user has crossed a level, print that if yes
            print('\nCorrect !')
            i+=1
        else:
            # end the game now.
            # also print the correct answer
            print('\nIncorrect !')
            print(f"The correct answer was, {QUESTIONS[i]['answer']}")
            if i<6:
                print('You won Rs. 0')
            elif i<10:
                print('You won Rs. 10,000')
            else:
                print('You won Rs. 3,20,000')
            game_play=False
        # print the total money won in the end.
 
 
kbc()
