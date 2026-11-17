# Q5 - Functions, Parameters and Scope

def add_item_buggy(item, order=[]):
    order.append(item)
    return order

def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order

def calculate_bill(amount, gst_rate=0.05):
    gst = amount * gst_rate
    total = amount + gst
    return total, gst  # Python returns both values as a tuple.

# Local, global and nonlocal scope demonstrations.
global_count = 10

def change_global():
    global global_count
    global_count += 1

def outer_function():
    message = "Outer value"
    def inner_function():
        nonlocal message
        message = "Changed by inner function"
    inner_function()
    return message

def make_order():
    """Closure alternative: each call creates an independent order."""
    order = []
    def add(item):
        order.append(item)
        return order.copy()
    return add

if __name__ == "__main__":
    print("Buggy shared default:")
    print(add_item_buggy("Tea"), add_item_buggy("Vada"))
    print("Buggy defaults:", add_item_buggy.__defaults__)

    print("\\nCorrect independent lists:")
    print(add_item("Tea"), add_item("Vada"))

    # Three customers, each with a separate list.
    customer1 = add_item("Meals", [])
    customer2 = add_item("Tea", [])
    customer3 = add_item("Juice", [])
    print("Customer 1:", customer1)
    print("Customer 2:", customer2)
    print("Customer 3:", customer3)

    # Positional, keyword and default arguments.
    print("\\nBill:", calculate_bill(100))
    total, gst = calculate_bill(amount=200, gst_rate=0.05)
    print("Total:", total, "GST:", gst)

    local_example = "I am local to main"
    print(local_example)
    print("Before global change:", global_count)
    change_global()
    print("After global change:", global_count)
    print("Nonlocal result:", outer_function())

    order_for_customer = make_order()
    print("Closure order:", order_for_customer("Sandwich"))
    print("Closure order:", order_for_customer("Coffee"))

# A default list is created once when the function is defined, so calls share
# it. None avoids this: a new list is made for each call. Append is O(1)
# amortised; storage is O(m) for m items in one customer's order.
