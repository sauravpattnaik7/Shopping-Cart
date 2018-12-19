import module
from IPython.display import clear_output

shopping_list = []
def main():
    print("Welcome to the store! Please get started by following the instructions below.", end="\n" * 2)
    module.instructions()

    # Keep on asking user the question
    # while statement keeps looping:
    #ask user to type item

    while True:

        query = input("What would you like to do? ")
        module.instructions()

        #if user types 'ADD':
        #add item to list
        if(query.upper() == 'ADD'):
            clear_output()
            item_add = input("What item would you like to add? ")

        #Check if user wants to add an item that has already been added.
#             i = 0
#             while i < len(shopping_list):
#                 if shopping_list[i] == item_add:
#                     repeat_query = input("This item is already in your cart. Would you like to add one more? ")
#                     if repeat_query.lower() == 'y':
#                         shopping_list[i] == shopping_list[i] + 'x2'

            module.add_to_cart(item_add)
            clear_output()
            module.instructions()
            continue

        #if user types 'REMOVE':
        #remove item to list
        if(query.upper() == 'REMOVE'):
            clear_output()
            item_remove = input("What item would you like to remove? ")
            if item_remove in shopping_list:
                module.remove_from_cart(item_remove)
                clear_output()
                module.instructions()
                continue
            else:
                clear_output()
                print(
                    "That item is not in your shopping list. Please choose another option.", end="\n" * 2)
                module.instructions()
                continue

        #if user types 'SHOW':
        #print instructions
        if(query.upper() == 'SHOW'):
            clear_output()
            print("These are the items in your shopping cart: ")
            module.show_items()
            print(" ", end="\n")
            module.instructions()
            continue

        #if user types 'DONE':
        #exits program by making while statement evaluate to False
        if(query.upper() == 'DONE'):
            clear_output()
            print(
                "Thank you! You're all done. These are the items in your shopping cart: ")
            module.show_items()
            break

        #If user types invalid command:
        #Repeat the question
    return False


main()
