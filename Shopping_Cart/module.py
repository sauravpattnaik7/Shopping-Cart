import os
from IPython.display import clear_output

shopping_list = []

def instructions():
    print("""Type 'ADD' to add item to cart.
Type 'REMOVE' to remove item from cart.
Type 'SHOW' to show items in your cart.
Type 'HELP' to show instructions.
Type 'CLEAR' to delete all contents in your cart.
Type 'DONE' to quit""")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    clear_output()


def add_to_cart(item):
    shopping_list.append(item)


def show_items():
    for i in shopping_list:
        print(i)


def remove_from_cart(item):
    shopping_list.remove(item)
