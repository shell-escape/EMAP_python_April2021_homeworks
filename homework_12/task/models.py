from django.db import models


class Human(models.Model):
    """Class that stores first and last name of a human.

    Attributes:
        last_name: human last name.
        first_name: human first name.
    """

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Student(Human):
    """Information about student."""


class Teacher(Human):
    """Information about teacher."""


class Homework(models.Model):
    """Homework text and due date.

    Attributes:
        text: text of the homework task.
        available_time: the time available for task completing.
        created: exact time of instance creation.
        author: homework author.
    """

    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    text = models.TextField()
    available_time = models.DurationField()
    created = models.DateTimeField(auto_now_add=True)


class HomeworkResult(models.Model):
    """Result of the student's homework.

    Attributes:
        author: solution author.
        homework: student homework.
        solution: homework solution.
        created: exact time of instance creation.
        done: whether the solution passed checking.
    """

    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField()
