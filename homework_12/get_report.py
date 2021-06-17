import os  # isort:skip
import django  # isort:skip

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "homework_12.settings")
django.setup()

from djqscsv import write_csv  # noqa
from task.models import HomeworkResult  # noqa


def get_report():
    """Generates a csv file that stores student name, creation date of
    homework result and teacher name who created homework for all
    completed homeworks.
    """

    qs = HomeworkResult.objects.filter(done=True).values(
        "author__first_name", "created", "homework__author__first_name"
    )

    headers = {
        "author__first_name": "Student_name",
        "created": "Creation_date",
        "homework__author__first_name": "Teacher_name",
    }

    with open("report.csv", "wb") as csv_file:
        write_csv(qs, csv_file, field_header_map=headers)


get_report()
