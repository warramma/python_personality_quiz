#6/26/2024

#import Question class
from Question import Question

#create array of questions
questions = [
    'On an ideal weekend, would you prefer: \n a) cozy day home doing hobbies, chilling, etc \nb) Fun day out with friends, time outside', 
    'In parties, are you usually: \na) Staying mostly in one spot, talking mostly to close friends, might be having fun but also wanting to go home \nb) Meeting as many people as possible, making new friends, having a blast'
]
#print(questions)

#create question objects in dictionary
quiz = {
    '1' : Question(questions[0], 'a', 'b'),
    '2' : Question(questions[1], 'a', 'b')
}

#create score variables
a_score = 0
b_score = 0

#loop through questions and ask which you prefer, keeping score in the right variable
for question in quiz:
    quiz[question].display_question