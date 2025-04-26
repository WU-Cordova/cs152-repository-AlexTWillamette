from .drink import Drink
from .orderitem import OrderItem
from .customerorder import CustomerOrder
from datastructures.hashmap import HashMap
from datastructures.linkedlist import LinkedList
from datastructures.bag import Bag
from copy import deepcopy

class BistroSystem():
    """
    Class to handle overarching bistro system functionality.
    Handles user interface and inputs.
    Uses helper classes for the menu, order qeueue, orders, order items, and drinks.
    """
    def __init__(self) -> None:
        """
        Initializes the bistro system.
        Creates the menu, a queue for orders, and the trackers for the end of day summary.
        """

        # Hardcoded menu items, that are available at the bistro as of 4/25/2025
        # Current implementation supports adding or removing menu items with no
        # adjustment needed elsewhere in code.
        drinks = ("Hot Choco", "London Fog", "Italian Soda", "Latte", "Mocha")
        prices = (4.00, 5.25, 4.00, 5.00, 5.00)

        self._menu = HashMap()
        for i in range(len(drinks)):
            self._menu[drinks[i].upper()] = Drink(name = drinks[i], size = "Medium", price = prices[i])
        
        self._open_orders_queue = LinkedList(data_type = CustomerOrder)

        # Keeps track of sales with their number sold rather than
        # storing all data about previous sales.
        # Uses a bag as a tally counter, essentially. 
        self._sales = Bag()

    
    def start(self) -> None:
        """
        Main loop for running the bistro system.
        Takes input from a main menu, and each input option
        implements a helper function which carries out the task.
        """
        print("Welcome to the Bearcat Bistro!")
        print()
        running = True
        self._display_commands()
        while running:
            print()
            response = input("Main Menu Select: ").upper()
            print()
            match response:
                case "1":
                    self._display_menu()
                case "2":
                    self._take_new_order()
                case "3":
                    self._view_open_orders()
                case "4":
                    self._mark_order_complete()
                case "5":
                    self._view_report()
                case "6":
                    print("Goodbye!")
                    running = False
                case "H" | "HELP":
                    self._display_commands()
                case _:
                    print('Enter "help" or "h" for help.')
    
    def _display_commands(self) -> None:
        """
        Helper function to display commands in the main menu.
        """
        print("1. Display Menu")
        print("2. Take New Order")
        print("3. View Open Orders")
        print("4. Mark Next Order as Complete")
        print("5. View End-of-Day Report")
        print("6. Exit")

    def _display_menu(self) -> None:
        """
        Helper function to display the menu items.
        """
        print(f"Item{" "*15}Price")
        print(f"{"-" * 24}")
        for drinkobject in self._menu.values():
            drink = drinkobject.name
            price = f"{drinkobject.price:.2f}"
            numspaces = 24 - len(drink) - len(price)
            print(f"{drink}{" " * numspaces}{price}")
    
    def _take_new_order(self) -> None:
        """
        Helper function to take an order.
        Uses a name to make an order, and then iteratively asks for order items,
        which are then added to the order. After all items are added, confirmation is
        requested. If the order is accepted, it is added to the open orders queue.

        If the order is not accepted, it will simply close the function, and the order
        will need to be remade from scratch.

        Drinks are entered with their name.

        I totally read the "allow" in the project specifications as an optional thing,
        where you ask the customer if they want the order read back to them or not, so
        that's what I implemented. 
        """

        customer_name = input("Customer's Name: ")
        order = CustomerOrder(name = customer_name)
        print("To complete the order hit enter with no drink")

        while True:
            drink = input("Enter Drink: ").upper()
            if drink == "" or drink == "DONE": # to finish entering drinks
                break
            elif drink not in self._menu: # O(1)! Thanks, hashmap!
                pass
            else: # valid drink, creating order item
                customization = input("Enter Customization: ")
                drinkobject = deepcopy(self._menu[drink])
                item = OrderItem(drink = drinkobject, customization = customization)
                order.add_item(item = item)
        if len(order) != 0:
            while True:
                ask_for_confirmation = input("Confirmation requested? (y/n): ")
                match ask_for_confirmation:
                    case "n":
                        break
                    case "y":
                        order.repeat_order()
                        while True:
                            confirmation = input("Confirm Order? y/n: ")
                            match confirmation:
                                case "n":
                                    print("Order aborted!")
                                    return # No implementation for revising an order, it'll   
                                           # just need to be remade
                                case "y":
                                    self._open_orders_queue.append(order) # confirmed order
                                    print("Order placed!")
                                    return
                                case _:
                                    pass
                    case _:
                        pass
            self._open_orders_queue.append(order)
            print("Order placed!") # if confirmation was not requested by customer
        else:
            print("Order aborted!") # if the order has no items/drinks
            
    def _view_open_orders(self) -> None:
        """
        Helper function to view the open orders.
        Prints last to first, so in the terminal the first order
        is the closest one to the bottom/input.
        """
        print("Orders:")
        print(f"{"-"*30}")
        pos = len(self._open_orders_queue)
        if len(self._open_orders_queue) == 0:
            print("No open orders.")
        else:
            for order in reversed(self._open_orders_queue):
                print(f"In position {pos}:")
                order.repeat_order()
                print(f"{"-"*30}")
                pos -= 1

    def _mark_order_complete(self) -> None:
        """
        Helper function to complete an order.
        Remove the order from the queue, and reads off the order.
        Uses the order's information to add to the end of day report tallies.
        """
        if len(self._open_orders_queue) == 0:
            print("No orders in queue to complete.")
        else:
            complete = self._open_orders_queue.pop_front()
            print("Order Completed:")
            complete.repeat_order()
            for drink in complete.drinks():
                self._sales.add(drink)

    def _view_report(self) -> None:
        """
        Helper function to view the end of day sales report.
        """
        print("End-of-Day Report:")
        print(f"{"-" * 41}")
        print("Drink Name         Qty Sold   Total Sales")
        totaldrinks = len(self._sales)
        totalrevenue = 0.00
        for drink in self._menu.values():
            sales = self._sales.count(drink.name)
            revenue = sales * drink.price
            spaces1 = 19 - len(drink.name)
            spaces2 = 11 - len(str(sales))
            totalrevenue += revenue
            print(f"{drink.name}{" "*spaces1}{sales}{" "*spaces2}${revenue:.2f}")
        space3 = 11 - len(str(totaldrinks))
        print()
        print(f"Total:{" "*13}{totaldrinks}{" "*space3}${totalrevenue:.2f}")
