"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   Easier to reuse.
   Easier to maintain. The data organized into smaller bits, so figuring out what
   it does is more clear. More structured.
   Harder to break a program when changing it.

2. What is a class?
    A class is kind of like a main category with sub categories under it.  As far
    as I understand one of the main uses is to keep related data and functions
    together so that you can have certain attributes and functionsfor all data higher in
    the heiarchy and keep the data more specific to certain instances only where they will apply.

3. What is an instance attribute?
    An instance attribute is information stored in a class. An instance attribute
    in the parent class have certain values, but can be overridden in a child class.

4. What is a method?
    A method is a function inside a class.

5. What is an instance in object orientation?
    An instance is like an offshoot of a class. A particular variation of a class but
    not the main class itself.

6. How is a class attribute different than an instance attribute?
    A class attribute holds information that will be true for all instances of
    that class.

    An instance attribute is unique to that particular occurance of the class.

    If you had a class for for example chess pieces you could put the attributes
    of the material they're all made from as a class attribute. The specific
    movement restrictions of each piece would be held as an instance attribute.

"""


class StudentInfo(object):
    """A class that can store data in a certain format.

    Desired format example:
    {'first_name': 'Jasmine',
    'last_name': 'Debugger',
    'address': '0101 Computer Street'}

    {'first_name': 'Jaqui',
    'last_name': 'Console',
    'address': '888 Binary Ave'}
    """

    def __init__(self, first_name, last_name, address):
        """Initialize Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class QuestionAnswer(object):
    """A class that can store data in a certain way.

    For example:
    {'question': 'What is the capital of Alberta?',
    'correct_answer': 'Edmonton'}

    {'question': 'Who is the author of Python?',
    'correct_answer': 'Guido Van Rossum'}
    """
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        user_answer = raw_input(self.question)
        if user_answer == self.correct_answer:
            return True
        else:
            return False


class Exam(object):
    """Adding question and answer areas to then append
    """
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        question = QuestionAnswer(question, correct_answer)
        self.questions.append(question)

    def administer(self):
        score = 0
        for question_answer in self.questions:
            is_correct = question_answer.ask_and_evaluate()
            if is_correct:
                score += 1
                #print "was correct!"
        return_questions = float(score) / len(self.questions)
        #percentage of answers right
        return return_questions


class Quiz(Exam):
    """Pass or fail depending on if person gets half or more of questions right
    """
    def administer(self):
        score = 0
        for question_answer in self.questions:
            is_correct = question_answer.ask_and_evaluate()
            if is_correct:
                score += 1
                #print "was correct!"
        return_questions = float(score) / len(self.questions)
        if return_questions >= 0.5:
            return True
        else:
            return False


def take_test(exam, student):
    student.score = exam.administer()
    print student.score


def example():
    exam = Exam("test exam")
    exam.add_question("What does the fox say?", "Blop")
    exam.add_question("What's up?", "The sky")
    student = StudentInfo("Firstnamez", "Lastnamezz", "666 Someaddress")
    take_test(exam, student)

example()


