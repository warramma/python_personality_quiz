class Question:
    a_score = 0
    b_score = 0

    def __init__ (self, prompt, black_cat, golden_retriever):
        self.prompt = prompt
        self.black_cat = black_cat
        self.golden_retriever = golden_retriever
    
    def display_question(self):
        return print(self.prompt)
    