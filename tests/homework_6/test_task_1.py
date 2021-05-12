from homework_6.task_1 import User


def test_instances_counter():
    """Testing that methods added by instances_counter decorator
    work right"""
    no_instances = User.get_created_instances()
    assert no_instances == 0

    _ = User()
    one_instance = User.get_created_instances()
    assert one_instance == 1

    before_reset = User.reset_instances_counter()
    assert before_reset == 1

    after_reset = User.get_created_instances()
    assert after_reset == 0
