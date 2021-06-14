from collections import defaultdict
from datetime import timedelta

from django.db import models
from django.utils import timezone


class DeadlineError(Exception):
    """Exception that raises if deadline is exceeded."""

    pass


class Human(models.Model):
    """Class that stores first and last name of a human.

    Attributes:
        last_name: human last name.
        first_name: human first name.

    Args:
        last_name: human last name.
        first_name: human first name.
    """

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Homework(models.Model):
    """Homework text and due date.

    Attributes:
        text: text of the homework task.
        available_time: the time available for task completing.
        created: exact time of instance creation.

    Args:
        text: text of the homework task.
        deadline: the number of days available for task completing.
    """

    text = models.CharField(max_length=255)
    available_time = models.DurationField()
    created = models.DateTimeField(auto_now_add=True)

    def is_active(self) -> bool:
        """Check if the time since object creation
        does not exceed 'deadline'.

        Returns:
            True if time does not exceed the deadline else False.
        """
        return timezone.now() - self.created < self.available_time


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
            return HomeworkResult(author=self, homework=homework, solution=solution)
        raise DeadlineError("You are late")


class HomeworkResult(models.Model):
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

    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)


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
        return Homework(text=text, available_time=timedelta(days=deadline))

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
