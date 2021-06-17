from datetime import timedelta

from django.utils import timezone
from task.models import Homework, HomeworkResult, Student, Teacher


class DeadlineError(Exception):
    """Exception that raises if deadline is exceeded."""

    pass


def is_active(homework: Homework) -> bool:
    """Check if the time since object creation
    does not exceed 'deadline'.

    Returns:
        True if time does not exceed the deadline else False.
    """
    return timezone.now() - homework.created < homework.available_time


def do_homework(
    student: Student, homework: Homework, solution: str
) -> "HomeworkResult":
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
    if is_active(homework):
        return HomeworkResult(author=student, homework=homework, solution=solution)
    raise DeadlineError("You are late")


def create_homework(teacher: Teacher, text: str, deadline: int) -> Homework:
    """Create a 'Homework' object.

    args:
        teacher: homework author.
        text: homework text.
        deadline: the number of days available for task completing.
    """
    return Homework(author=teacher, text=text, available_time=timedelta(days=deadline))


def check_solution(solution: str) -> bool:
    """Homework solution check.

    Args:
        solution: homework solution.

    Returns:
        Whether the solution passed checking.
    """
    return len(solution) > 5


def check_homework_result(homework_result: HomeworkResult):
    """Fill the 'done' field in HomeworkResult object.

    Args:
        homework_result: student homework result.
    """
    homework_result.done = check_solution(homework_result.solution)
