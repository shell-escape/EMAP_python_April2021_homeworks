from homework_11.task_2 import Order


def test_order_with_discount_program():
    """Testing 'Order' class with different discounts."""

    def morning_discount(order):
        return order.price - order.price * 0.5

    def elder_discount(order):
        return order.price - order.price * 0.9

    order = Order(100, morning_discount)
    assert order.final_price() == 50

    order.discount_program = elder_discount
    assert order.final_price() == 10
