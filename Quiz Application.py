import random

class Quiz:
    def __init__(self):
        self.questions = {
            'General Knowledge': [
                {'question': 'What is the capital of France?', 'options': ['Paris', 'Berlin', 'London'], 'correct_answer': 'Paris'},
                {'question': 'Which planet is known as the Red Planet?', 'options': ['Mars', 'Venus', 'Jupiter'], 'correct_answer': 'Mars'},
            ],
            'Programming': [
                {'question': 'What language does Django framework use?', 'options': ['Python', 'Java', 'Ruby'], 'correct_answer': 'Python'},
                {'question': 'What does HTML stand for?', 'options': ['Hyper Text Markup Language', 'High Tech Multi Language', 'Hyper Transfer Markup Language'], 'correct_answer': 'Hyper Text Markup Language'},
            ],
        }
        self.score = 0

    def get_category(self):
        # Choose a random category from available categories
        return random.choice(list(self.questions.keys()))

    def display_question(self, question_data):
        print(question_data['question'])
        for i, option in enumerate(question_data['options'], start=1):
            print(f"{i}. {option}")

    def run_quiz(self):
        print("Welcome to the Quiz!\n")

        for _ in range(5):  # Total 5 questions
            category = self.get_category()
            question_data = random.choice(self.questions[category])

            self.display_question(question_data)

            user_answer = input("Your answer (enter the number): ")
            correct_answer = question_data['options'].index(question_data['correct_answer']) + 1

            if user_answer.isdigit() and 1 <= int(user_answer) <= len(question_data['options']):
                if int(user_answer) == correct_answer:
                    print("Correct!\n")
                    self.score += 1
                else:
                    print(f"Wrong! The correct answer is {correct_answer}. \n")

        print(f"Quiz completed! Your score: {self.score}/5")

if __name__ == "__main__":
    quiz = Quiz()
    quiz.run_quiz()
