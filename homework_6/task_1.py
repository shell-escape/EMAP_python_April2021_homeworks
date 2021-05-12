"""
Написать декоратор instances_counter, который применяется к любому
классу и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых
экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""

from typing import Type


def instances_counter(cls: Type):
    """Decorator that adds instances counter to a class.

    Adds two methods:
    - get_created_instances: returns the number of
    created class instances.
    - reset_instances_counter: resets the instances counter,
    returns the number of instances before reset.

    Returns:
        Class with added methods.
    """

    class InstancesCounter(cls):
        """Class that counts instances, inherited from cls."""

        _counter = 0

        def __init__(self, *args, **kwargs):
            InstancesCounter._counter += 1
            super().__init__(*args, **kwargs)

        @classmethod
        def get_created_instances(cls) -> int:
            return InstancesCounter._counter

        @classmethod
        def reset_instances_counter(cls) -> int:
            _counter_before_reset = InstancesCounter._counter
            InstancesCounter._counter = 0
            return _counter_before_reset  # noqa

    return InstancesCounter


@instances_counter
class User:
    pass


if __name__ == "__main__":

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
