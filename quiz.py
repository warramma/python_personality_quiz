#6/26/2024

from Question import Question

#create array of questions
questions = [
    'On an ideal weekend, would you prefer: \na) cozy day home 🏠 doing hobbies, chilling 💤, etc \nb) Fun day out with friends 🎉, time outside ☀️😎', 
    'In parties 🥳, are you usually: \na) Staying mostly in one spot 😵‍💫, talking mostly to close friends 🥰, might be having fun but also wanting to go home 🏡 \nb) Meeting as many people 🫂 as possible, making new friends, having a blast 🚀',
    'Are you: \na) a night owl 🌉 \nb) a morning person 🌅 ',
    'Would you rather be: \na) the smartest 😎 \nb) the friendliest in the room 🥰 ',
    'favorite seasons? \na) spring 🌸 and winter ❄️ \nb) summer ☀️ and fall 🍁'
]
#print(questions) (just testing hehe)

#create question objects in dictionary
quiz = {
    '1' : Question('#1 ' + questions[0], 'a', 'b'),
    '2' : Question('\n#2 '+questions[1], 'a', 'b'),
    '3' : Question('\n#3 '+questions[2], 'a', 'b'),
    '4' : Question('\n#4 '+questions[3], 'a', 'b'),
    '5' : Question('\n#2 '+questions[4], 'a', 'b'),
}

#create score variables
a_score = 0
b_score = 0
def results(a_score, b_score):
    print('Your scores:\nBlack cat: ' + str(a_score) + '\nGolden Retriever: ' + str(b_score) + '\n--------------')
    if(a_score > b_score):
        print('You are a black cat! 🐈‍⬛\nYou are introverted and deeply mysterious, but deeply affectionate around those you love! \nYou love to stay in and cuddle, read books, and have plenty of alone time!\nYou safeguard your energy dearly because it gets easily depleted!\nYou dislike suprises and loud noises and welcome routine!\nWelcome to the club!!')
    elif(b_score > a_score):
        print('You are a golden retriever!\nExtroverted and very friendly, you really get around!\nYou are always making new friends!\nYou are a great listener and get along with everyone!\nYou love spending time with loved ones and being active! 🐕')
    else:
        print('You are equal parts black cat 🐈‍⬛ and golden retriever 🐕!! Way to forge your own path :)')
        print('You straddle the line between introversion and extroversion. Although you love people, you also love you time! \nYou are passionate about your hobbies and love making news friends and experiencing new things!')

#------------------------------------QUIZ BELOW ⬇️
#welcome user + disclaimer
print('Welcome to Black Cat vs Golden Retriever personality test!\nDisclaimer: this test is just for run and is not necessarily an accurate depiction of who you actually are :)\nLet\'s get started!\n')

#loop through questions and ask which you prefer, keeping score in the right variable
for question in quiz:
    answer = str(quiz[question].ask_question())
    #print('You answered ' + str(answer) + '! Woohoo!')
    if(answer.lower() == quiz[question].black_cat):
        a_score +=1
    elif(answer.lower() == quiz[question].golden_retriever):
        b_score +=1
    else:
        print('invalid input...')

print('calculating your results......\n...............................\n......................')
results(a_score,b_score)


