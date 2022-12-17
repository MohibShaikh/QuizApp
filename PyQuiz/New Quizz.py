from functions import *
print('Welcome to the quiz app!'.upper())
print()
print('\tHit enter to access the quiz as User'.title())
print('\tEnter password to access administrator priviliges '.title())
print()
AdmOrUser=input('Choose: '.title())                                                                         # Taking an input from user to check if they want to enter as admin or as user                                                                                               # Setting a score variable to zero to increment it and show how much dd the user score throughout the chosen quiz
if AdmOrUser=='1234':                                                                                       # If the user enters 1234, the admin tools come up i.e the view of questions straight out of the question bank and
    print()
    print('You can either view the questions or add questions')
    print('For addition of question press \'2\' and hit enter, if you want to view questions only, hit enter')
    print()
    ViewOr_Not=input('Choose: ')
    print()
    if ViewOr_Not=='2':
        print('\t1. Chemistry Quiz')
        print('\t2. Biology Quiz')
        Choice=input('Choose the number prior to the respective subject to add question to: '.title())
        if Choice=='1':
            print(Chem_Add_Ques())                                                                               # Breaks out of the loop and the program terminates
        elif Choice=='2':
            print(Bio_Add_Ques())                                                                             # Breaks out of the loop and the program terminates
    if ViewOr_Not=='':
        print(Ques_Bank())                                                                                   # Returns the question bank of the desired part of the quiz
elif AdmOrUser=='':
    print()
    print('We have two quizzes:')
    print('\t1. Biology')
    print('\t2. Chemistry')
    Chem_OrBio=input('Select the number prior to the subject you want to take the quiz on: '.title())
    print()
    if Chem_OrBio =='1':
        print(Bio_Quiz())
    elif Chem_OrBio=='2':
        print(Chem_Quiz())                                            # Printing the final score
input('Enter any key to exit the program')