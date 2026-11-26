from abc import ABC, abstractmethod

class AcademicTask(ABC):
    def __init__(self, title, max_points):
        self.title = title
        self.max_points = max_points
        self.is_graded = False

    @abstractmethod
    def submit_work(self):
        pass

    @abstractmethod
    def grade_work(self): 
        pass

    @abstractmethod
    def get_details(self):
        pass


class Quiz(AcademicTask):
    def __init__(self, title, max_points, total_questions):
        super().__init__(title, max_points)
        self.__total_questions = total_questions
        self.correct_answers = 0

    def submit_work(self,correct_answers):
        self.correct_answers = correct_answers
        print(f"Quiz submitted: {self.title}")

    def grade_work(self):
        self.is_graded = True
        return (self.correct_answers / self.__total_questions) * self.max_points
        
        

    def get_details(self):
        print(f"[QUIZ] {self.title} - Max Points: {self.max_points}")

quiz1 = Quiz("Math Quiz", 100, 10)

quiz1.submit_work(8)
print("Grade:", quiz1.grade_work())
quiz1.grade_work()
quiz1.get_details()
print("Graded:", quiz1.is_graded)
