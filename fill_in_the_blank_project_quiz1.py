print "Welcome to Random Trivia"
print " "
#    behavior print displays a message to the user
#    input no input by user require
#    output is the message the user receives
blanks = ["___1___", "___2___", "___3___", "___4___"]
easy_quiz = '''The largest state in the USA is ___1___.  The smallest state in the USA is ___2___.
The state with the largest population is ___3___.  The state with the smallest population is
___4___.'''

easy_answers = ["alaska", "rhode island", "california", "wyoming"]

medium_quiz = '''___1___ is the longest running animated series on network televsion.
___2___ is the longest running network televsion show of all time.  It has been
on for ______years!  ___3___ was the longest running soap opera on
television.  ___4___ is the longest running drama currently on television.  '''

medium_answers = ["the simpsons", "meet the press", "guiding light", "law & order"]

hard_quiz = '''___1___ holds the NBA record for most points scored with 38,387.  ___2___ holds the record
for scoring the most points in a single game.  ___3___ also holds the record for most rebounds in the
NBA.  ___4___ has the most championships from his time with the Boston Celtics.'''

hard_answers = ["kareem abdul-jabbar", "wilt chamberlain", "wilt chamberlain", "bill walton"]

answers = [easy_answers, medium_answers, hard_answers]

paragraph = [easy_quiz, medium_quiz, hard_quiz]
#   behavior the code above identifies the 3 levels of quizes as well as the answers
#   input the code also includes the references the blanks which help enable the
#   output answers to fill in the blanks when the questions are repeated.
def choose_level():
#    behavior def choose_level asks the user to choose the difficulty level of the quiz
#    input based on which difficulty level the user chooses
#    output the quiz with that level of difficulty is returned
    user_level = raw_input("Please enter a difficulty level. Easy, medium or hard?")
    print "\nYou've chose " + str(user_level) + ".  Good luck!\n"
    easy_level = 0
    if user_level == "easy":
        return easy_level
    elif user_level == "medium":
        return medium_level
    elif user_level == "hard":
        return hard_level
    else:
        print "I'm sorry but an error occurred.\n"
        return choose_level()
    return level
#    behavior if, elif and else lets the quiz identify which level to present
#    input is based on the users selection
#    output quiz level is returned based on what the user selected 
print " "
def determine_attempts():
#    behavior defines the number of attempts the user gets to answer the quiz question correctly
#    input the user inputs the number of attempts they would like
#    output the quiz gives the user x many chances to answer correctly
    attempts = raw_input("How many attempts do you want to answer before answer is provided?")
    print " "
    counter = 0
    while attempts < 1:
        print "try again"
        determine_attempts
        counter = counter + 1
        if counter == number_displayed:
            break
        else:
            print "Please read quiz and provide the answer to fill in.  You will be given " + str(attempts) + "."
            return attempts
#    while identifies how many attempts to give user to get the correct answer

#def paragraph_level():
#    paragraph[level]= paragraph[level].replace(blanks[chances-1], response)

def quiz(level, attempts):
    replaced = []
    print "Here is your question:" + str(paragraph[level])
#    behavior this is the function that reads the answer and allows the user to move to the next question if correct
#    input user provides answer to question
#    output the quiz will congratulate or tell that answer is wrong
    chances = 1
    max_blanks = 5
    while chances < max_blanks:
        response = raw_input("What is the answer" + str(chances) + "?\n").lower()
        if response == answers[level][chances-1]:
            print "You are correct!\n" 
            paragraph[level] =(paragraph[level]).replace(blanks[chances-1], response)
            print str(paragraph[level])
            chances = chances + 1
        else:
            wrong_answers = 2
            while response != answers[level][chances - 1]:
                print "please try again\n"
                print str(paragraph[level]).replace("blanks", "response")
                response = raw_input("What is answer " + str(chances) + "?\n").lower()
                wrong_answers = wrong_answers + 1
                if wrong_answers > attempts:
                    print "the correct answer is " + str(answers[level][chances-1])
                    response = answers[level][chances-1]
                    paragraph[level] = paragraph[level].replace(blanks[chances-1], response)
                    print str(paragraph[level])
            chances = chances + 1
#    behavior the while loop advances to the next question when the correct answer is provided
#    input quiz taker provides answer and quiz either allows advancement or gives another chance
#    output the user is either congratulated and sees the question with correct answer or tries again
def go():
    quiz(choose_level(), determine_attempts())
#    behavior starts the quiz
#    input none required
#    output quiz begins
print go()
    
