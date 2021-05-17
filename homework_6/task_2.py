"""
В этом задании будем улучшать нашу систему классов из задания прошлой
лекции (Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное
задание и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -
    выкинуть подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при
do_homework, а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late'
вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью
наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда
    поподают все HomeworkResult после успешного прохождения
    check_homework (нужно гаранитровать остутствие повторяющихся
    результатов по каждому заданию), группировать по экземплярам
    Homework. Общий для всех учителей. Вариант ипользования смотри
    в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает
    True если ответ студента больше 5 символов, так же при успешной
    проверке добавить в homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпляр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не
    передавать, то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить
ответственно - давать логичные подходящие имена.
"""

from collections import defaultdict
from datetime import datetime, timedelta


class DeadlineError(Exception):
    """Exception that raises if deadline is exceeded."""

    pass


class Human:
    """Class that stores first and last name of a human.

    Attributes:
        last_name: human last name.
        first_name: human first name.

    Args:
        last_name: human last name.
        first_name: human first name.
    """

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Homework:
    """Homework text and due date.

    Attributes:
        text: text of the homework task.
        available_time: the time available for task completing.
        created: exact time of instance creation.

    Args:
        text: text of the homework task.
        deadline: the number of days available for task completing.
    """

    def __init__(self, text: str, deadline: int):
        self.text = text
        self.available_time = timedelta(days=deadline)
        self.created = datetime.now()

    def is_active(self) -> bool:
        """Check if the time since object creation
        does not exceed 'deadline'.

        Returns:
            True if time does not exceed the deadline else False.
        """
        return datetime.now() - self.created < self.available_time


class Student(Human):
    """Information about student."""

    def do_homework(self, homework: Homework, solution: str) -> "HomeworkResult":
        """Returns 'HomeworkResult' object if homework deadline
        is not exeeded.

        Args:
            homework: student homework.
            solution: homework solution.

        Raises:
            DeadlineError: if homework deadline is exceeded.

        Returns:
            Created HomeworkResult object.
        """
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        raise DeadlineError("You are late")


class HomeworkResult:
    """Result of the student's homework.

    Attributes:
        author: homework author.
        homework: student homework.
        solution: homework solution.
        created: exact time of instance creation.

    Args:
        author: homework author.
        homework: student homework.
        solution: homework solution.
    """

    def __init__(self, author: Student, homework: Homework, solution: str):
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")

        self.homework = homework
        self.author = author
        self.solution = solution
        self.created: datetime = datetime.now()


class Teacher(Human):
    """Information about teacher."""

    homework_done = defaultdict(list)

    @staticmethod
    def create_homework(text: str, deadline: int) -> Homework:
        """Create a 'Homework' object.

        args:
            text: homework text.
            deadline: the number of days available for task completing.
        """
        return Homework(text, deadline)

    @classmethod
    def check_homework(cls, homework_result: HomeworkResult) -> bool:
        """Returns True and adds 'homework_result' in 'homework_done'
        attribute if 'homework_result' solution is longer than
        5 symbols. Returns False otherwise.

        Args:
            homework_result: student homework result.

        Returns:
            True if student's solution passes checking
            and False otherwise.
        """
        if len(homework_result.solution) > 5:
            cls.homework_done[homework_result.homework].append(homework_result)
            return True
        return False

    @classmethod
    def reset_results(cls, homework: Homework = None):
        """Delete 'homework' from 'homework_done' if 'homework'
        is passed. Else completely reset 'homework_done'.

        Args:
            homework: a homework to delete from 'homework_done'.
        """
        if homework is not None:
            del cls.homework_done[homework]
            return
        cls.homework_done = defaultdict(list)


if __name__ == "__main__":
    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

    lazy_student = Student("Roman", "Petrov")
    good_student = Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    result_3 = lazy_student.do_homework(docs_hw, "done")
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print("There was an exception here")  # noqa
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2  # noqa

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])  # noqa
    Teacher.reset_results()
