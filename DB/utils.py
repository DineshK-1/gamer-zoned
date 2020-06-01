import random
import string
from Orders.models import Orders

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_order_id_generator():
    order_new_id= random_string_generator()
    qs_exists= Orders.objects.filter(Order_id= order_new_id).exists()
    if qs_exists:
        return unique_order_id_generator()
    return order_new_id
