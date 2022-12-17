def Chem_Add_Ques():
    with open('Chem.txt','a') as c:  # Opening text file with the with statement ensures it gets closed when we are done with the code within it i.e we don't need to close the code externally with statement takes care of it itself. That's why there's no closing statement when all the codes have been executed within the open fucntion
        for add_ques in range(11,20):  # Running a loop in a specified range as there wouldn't be addition of huge amount of questions
            c.write('\n')  # Writing a backslah n so that a new line is started when before we begin adding question to it
            ques_no = input('enter ques no. '.title())  # Question number before the question
            new_ques = input('type the question to add to the questionnaire: '.title())  # The question to be added
            op1 = input('provide the 1st option: '.title())  # options
            op2 = input('provide the 2nd option: '.title())
            op3 = input('provide the 3rd option: '.title())
            op4 = input('provide the correct option: '.title())  # a, b, c as the correct answer not 1, 2, 3
            c.write('Q' + ques_no + ':' + ' ' + new_ques + '\na) ' + op1 + '\nb) ' + op2 + '\nc) ' + op3 + '\n' + op4)  # Writing it all back into the text file opened and adding the question and answers with backslash ns so that each option alongwith the correct option is in a new line
            print()
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^PROCEEDING^^^^^^^^^^^^^^^^^^^^^^^^^^')
            print('question added'.title())
            print()
            print('press enter to add more questions'.title())
            print(
                'press n to terminate the program'.title())  # To break the loop when the admin doesn't want to add more questions
            askin = input('do you wish to add more questions?  '.title().lower())
            if askin == '':
                print()  # Starts the loop again with a space
            elif askin == 'n':
                break
def Bio_Add_Ques():
    with open('Bio.txt','a') as b:  # Opening text file with the with statement ensures it gets closed when we are done with the code within it i.e we don't need to close the code externally with statement takes care of it itself. That's why there's no closing statement when all the codes have been executed within the open fucntion
        for add_ques in range(11,20):  # Running a loop in a specified range as there wouldn't be addition of huge amount of questions
            b.write('\n')  # Writing a backslah n so that a new line is started when before we begin adding question to it
            ques_no = input('enter ques no.'.title())
            new_ques = input('type the question to add to the questionnaire: '.title())
            op1 = input('provide the 1st option: '.title())
            op2 = input('provide the 2nd option: '.title())
            op3 = input('provide the 3rd option: '.title())
            op4 = input('provide the correct option: '.title())  # a, b, c as the correct answer not 1, 2, 3
            b.write('Q' + ques_no + ':' + ' ' + new_ques + '\na) ' + op1 + '\nb) ' + op2 + '\nc) ' + op3 + '\n' + op4)
            print()
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^PROCEEDING^^^^^^^^^^^^^^^^^^^^^^^^^^')
            print('question added'.title())
            print()
            print('press enter to add more question'.title())
            print('press n to close the program'.title())
            askin = input('Do you wish to add more questions?')
            if askin == '':
                print()  # Starts the loop again with a space
            elif askin == 'n':
                break
def Bio_Quiz():
    score=0
    y = [line.rstrip() for line in open('Bio.txt')]  # List Comprehension; opens the file in default read mode, strips(\n or any other spaces e.g \t etc.) from the right, loops the string within the file and finally storing it  in the list ###
    List_OfQues = [y[i:i + 5] for i in range(0, len(y),5)]  # Using List Comprehension to create sublists in the major list y. It is carried out to separate individual question, its' options and the right answer of the question in a single sublist which is different for every question #for ques_ans in List_OfQues: # running a loop on major list y to get questions, options and its' right answer
    for ques_ans in List_OfQues:  # Running a loop on major list y to get questions, options and its' right answer
        for options in range(0,len(ques_ans) - 1):  # Running a loop on sublists to separately present questions and its' options neatly. Omitting the right answer to be printed  by setting the range accordingly
            print(ques_ans[options])
        ans = input('Select option (a,b or c):\n')  # Taking an input from the user everytime reaches the end of each sublist
        if ques_ans[4] == ans:  # Comparing the user provided answer to the right answer
            score += 1  # Incrementing everytime the user gets the answer right #
            print('Correct!')
            print(score, 'out of 10')
        else:
            print('Wrong!')
    return 'your score in biology quiz is '.title(), score
def Chem_Quiz():
    score=0
    y = [line.rstrip() for line in open('Chem.txt')]
    List_OfQues = [y[i:i + 5] for i in range(0, len(y),5)]  # Using List Comprehension to create sublists in the major list y. It is carried out to separate individual question, its' options and the right answer of the question in a single sublist which is different for every question #for ques_ans in List_OfQues: # running a loop on major list y to get questions, options and its' right answer
    for ques_ans in List_OfQues:  # Running a loop to present sublists which are  also iterable
        for options in range(0,len(ques_ans) - 1):  # Running a loop on major list y to get questions, options and its' right answer
            print(ques_ans[options])
        ans = input('Select option (a,b or c):\n')  # Taking input to check if their answer is correct or incorrect by comparing it to the right option
        if ques_ans[4] == ans:
            score += 1  # Incrementing everytime the user gets the answer right
            print('Correct!')
            print(score, 'out of 10')
        else:
            print('Wrong!')
    return 'your score in chemistry quiz is '.title(), score
def Ques_Bank():                                                                                            # Defining a function that asks for the subject you want to view the questions of
    print('Enter the section you want to see the question bank of')
    a=input('For Bio enter \'b\'\nfor Chemistry press \'c\' '.title())                                      # An input to ask the user/admin for the subject initials so that it can open the relevant question bank
    a.lower()
    if a=='b':                                                                                              # Passing the condition to which opens Biology quiz question bank which shows the question, options and the option that is the right answer
        lines=[line.rstrip() for line in open('Bio.txt')]                                                   # Using a complex list comprehension to in which the relevant question bank text file opens up and a loop is run. Ultimately, showing all the questions
        questiona=[]                                                                                        # Initializing a list i.e setting an empty list beforehand, that later on appends each line from the text file into it
        for i in range(0,len(lines),5):                                                                     # A loop that runs till the 5th line, pauses, appends to the list and starts again. This loop is run in such a manner to ensure each question alongwith the options and answer is in a separate sublist from other questions
            questiona.append(lines[i:i+5])
        for ques_ans in questiona:                                                                          # running a loop on major list y to get questions, options and its' right answer
            for options in range(0,len(ques_ans)):                                                          # Running a loop on sublists to separately present questions and its' options neatly
                print(ques_ans[options])                                                                    # Printing each iterable from the sublist which are, in this case, question, it's three options and the right option
    elif a=='c':                                                                                            # Passing the condition to which opens Chemistry quiz question bank which shows the question, options and the option that is the right answer
        lines=[line.rstrip() for line in open('Chem.txt')]                                                  # Using a complex list comprehension to in which the relevant question bank text file opens up and a loop is run. Ultimately, showing all the questions
        questiona=[]                                                                                        # Setting an empty list that later on appends each line from the text file into it
        for i in range(0,len(lines),5):                                                                     # Printing each iterable from the sublist which are, in this case, question, it's three options and the right option
            questiona.append(lines[i:i+5])
        for ques_ans in questiona:                                                                          # running a loop on major list 'questiona' to get questions, options and its' right answer presented
            for options in range(0,len(ques_ans)):                                                          # Running a loop on sublists to separately present questions and its' options neatly.
                    print(ques_ans[options])                                                                # Printing each iterable from the sublist which are, in this case, question, it's three options and the right option
    return 'Hit Enter to terminate the program'.title()