from homework_4.task_3_get_print_output import my_precious_logger


def test_stdout(capsys):
    my_precious_logger("OK")
    out, err = capsys.readouterr()
    assert (out, err) == ("OK", "")


def test_stderr(capsys):
    my_precious_logger("error: file not found")
    out, err = capsys.readouterr()
    assert (out, err) == ("", "error: file not found")


def test_empty_case(capsys):
    my_precious_logger("")
    out, err = capsys.readouterr()
    assert (out, err) == ("", "")
