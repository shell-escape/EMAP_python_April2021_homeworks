from homework_11.task_2 import Order


def test_order_with_discount_program():
    """Testing 'Order' with different discounts."""

    def morning_discount():
        return 0.5

    def elder_discount():
        return 0.9

    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 50

    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10
