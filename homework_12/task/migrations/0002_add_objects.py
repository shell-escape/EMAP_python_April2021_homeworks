from django.db import migrations
from task.models import Student, Teacher
from task.services import check_homework_result, create_homework, do_homework


def create_objects(apps, schema_editor):
    student1 = Student(first_name="StudentName1", last_name="StudentSurname1")
    student1.save()
    student2 = Student(first_name="StudentName2", last_name="StudentSurname2")
    student2.save()

    teacher1 = Teacher(first_name="TeacherName1", last_name="TeacherSurname1")
    teacher1.save()
    teacher2 = Teacher(first_name="TeacherName2", last_name="TeacherSurname2")
    teacher2.save()

    homework1 = create_homework(teacher=teacher1, text="text1", deadline=1)
    homework1.save()
    homework2 = create_homework(teacher=teacher2, text="text2", deadline=2)
    homework2.save()

    student_1_hw_1_result = do_homework(student1, homework1, "right_solution")
    student_1_hw_2_result = do_homework(student1, homework2, "right_solution")

    student_2_hw_1_result = do_homework(student2, homework1, "right_solution")
    student_2_hw_2_result = do_homework(student2, homework2, "right_solution")

    list(
        map(
            check_homework_result,
            [
                student_1_hw_1_result,
                student_1_hw_2_result,
                student_2_hw_1_result,
                student_2_hw_2_result,
            ],
        )
    )

    student_1_hw_1_result.save()
    student_1_hw_2_result.save()
    student_2_hw_1_result.save()
    student_2_hw_2_result.save()


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_objects),
    ]
