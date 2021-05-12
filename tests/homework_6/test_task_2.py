import pytest

from homework_6.task_2 import DeadlineError, Homework, HomeworkResult, Student, Teacher


def test_homework_is_active_positive_case():
    """Testing that 'Homework' 'is_active()' method returns True
    if deadline is not exeeded."""
    homework = Homework("Learn functions", 1)

    assert homework.is_active() is True


def test_homework_is_active_negative_case():
    """Testing that 'Homework' 'is_active()' method returns False
    if deadline is exeeded."""
    homework = Homework("Task text", 0)

    assert homework.is_active() is False


def test_student_do_homework_positive_case():
    """Testing that 'Student' 'do_homework()' method returns 'Homework'
    object itself if the deadline is not exeeded."""
    homework = Homework("Task text", 1)
    student = Student("Name", "Surname")
    homework_result = student.do_homework(homework, "Solution")

    assert isinstance(homework_result, HomeworkResult)


def test_student_do_homework_negative_case():
    """Testing that 'Student' 'do_homework()' method returns None
    and prints "You are late" if the deadline is exeeded."""
    homework = Homework("Task text", 0)
    student = Student("Name", "Surname")

    with pytest.raises(DeadlineError, match="You are late"):
        student.do_homework(homework, "Solution")


def test_teacher_create_homework():
    """Testing that 'Teacher' 'create_homework()' method
    works right."""
    teacher = Teacher("Name", "Surname")
    homework = teacher.create_homework("Task text", 0)

    assert isinstance(homework, Homework)


def test_case_when_homework_result_gets_non_homework_instance():
    """Testing that 'HomeworkResult' constructor will raise TypeError
    if a non-Homework instance is passed."""
    student = Student("Name", "Surname")

    with pytest.raises(TypeError, match="You gave a not Homework object"):
        HomeworkResult(student, "non-Homework instance", "Solution")


def test_teacher_check_homework_negative_case():
    """Testing that 'Teacher' 'check_homework()' method returns False
    and does not add HomeworkResult instance to 'homework_done'
    attribute when solution is not passed checking."""
    teacher = Teacher("Name", "Surname")
    student = Student("Name", "Surname")
    homework = teacher.create_homework("Homework_task", 1)
    homework_wrong_result = student.do_homework(homework, "Wrong")

    assert teacher.check_homework(homework_wrong_result) is False
    assert len(Teacher.homework_done) == 0


def test_teacher_check_homework_positive_case_and_reset_results():
    """Testing that 'Teacher' 'check_homework()' method returns True
    and adds HomeworkResult instance to 'homework_done' attribute
    when solution is passed checking. Also testing that
    'reset_result()' method works right"""
    teacher = Teacher("Name", "Surname")
    student = Student("Name", "Surname")
    homework = teacher.create_homework("Homework_task", 1)
    homework_right_result = student.do_homework(homework, "Right solution, len > 5")

    assert teacher.check_homework(homework_right_result) is True
    assert Teacher.homework_done[homework][0] is homework_right_result

    len_before_reset = len(Teacher.homework_done)
    assert len_before_reset == 1

    Teacher.reset_results()

    len_after_reset = len(Teacher.homework_done)
    assert len_after_reset == 0
