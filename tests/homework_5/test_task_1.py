from homework_5.task_1 import Homework, Student, Teacher


def test_homework_is_active_positive_case():
    """Testing that 'Homework' is_active() method returns True
    if deadline is not exeeded"""
    homework = Homework("Learn functions", 1)

    assert homework.is_active() is True


def test_homework_is_active_negative_case():
    """Testing that 'Homework' 'is_active()' method returns False
    if deadline is exeeded"""
    homework = Homework("Task text", 0)

    assert homework.is_active() is False


def test_student_do_homework_positive_case():
    """Testing that 'Student' 'do_homework()' method returns 'Homework'
    object itself if the deadline is not exeeded"""
    homework = Homework("Task text", 1)

    assert Student.do_homework(homework) is homework


def test_student_do_homework_negative_case(capsys):
    """Testing that 'Student' 'do_homework()' method returns None
    and prints "You are late" if the deadline is exeeded"""
    homework = Homework("Task text", 0)
    student_homework = Student.do_homework(homework)
    out, _ = capsys.readouterr()

    assert student_homework is None
    assert out == "You are late"


def test_teacher_create_homework_works_right():
    """Testing that 'Teacher' 'create_homework()' method works right"""
    homework = Teacher.create_homework("Task text", 0)

    assert isinstance(homework, Homework)
