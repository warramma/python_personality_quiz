class Question:
    a_score = 0
    b_score = 0

    def __init__ (self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
    
    def display_question(self):
        print(self)

    def calculate_result(self):
        if(self.answer.lower() == 'a'):
            a_score+=1
        elif(self.answer.lower()=='b'):
            b_score+=1
        else:
            print('\ninvalid input...')
        if(a_score > b_score):
            print('Black cat!')
        elif(a_score < b_score):
            print('Golden retriever!')
        else:
            print('You\'re a perfect mix!')