from abc import abstractmethod

class Test:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

class Question:
    def __init__(self, question):
        self.question = question

    @abstractmethod
    def returnJson(self):
        pass

class QuestionsWithVariants(Question):
    def __init__(self, question, variants, rightAnswer):
        super().__init__(question)
        self.variants = variants
        self.rightAnswer = rightAnswer

    def returnJson(self):
        json = {}
        json['question'] = self.question
        json['variants'] = self.variants
        json['rightAnswer'] = self.rightAnswer
        return json

if __name__ == "__main__":
    q = QuestionsWithVariants('сколько лет живут черепахи', ['100','200','300'], 0)
    print(q.returnJson())







