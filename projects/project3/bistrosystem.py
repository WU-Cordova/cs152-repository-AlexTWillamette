from .drink import Drink
from .orderitem import OrderItem
from .customerorder import CustomerOrder
from datastructures.hashmap import HashMap
from datastructures.linkedlist import LinkedList
from datastructures.bag import Bag
from copy import deepcopy

class BistroSystem():
    """
    DOCSTRING YOSELF
    """
    def __init__(self) -> None:
        """
        DOCSTRING YOSELF
        """
        self._menu = HashMap()
        
        self._drinks = ("Hot Choco", "London Fog", "Italian Soda", "Latte", "Mocha")
        self._prices = (4.00, 5.25, 4.00, 5.00, 5.00)
        for i in range(len(self._drinks)):
            self._menu[self._drinks[i].upper()] = Drink(name = self._drinks[i], size = "Medium", price = self._prices[i])
        
        self._open_orders_queue = LinkedList(data_type = CustomerOrder)

        self._sales = Bag()
        self._total_revenue = 0.00

    
    def start(self) -> None:
        """
        DOCSTRING YOSELF
        """
        print("Welcome to the Bearcat Bistro!")
        print()
        running = True
        self._display_commands()
        while running:
            print()
            response = input().upper()
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
                    running = False
                case "H" | "HELP":
                    self._display_commands()
                case _:
                    print('Enter "help" or "h" for help.')
    
    def _display_commands(self) -> None:
        print("1. Display Menu")
        print("2. Take New Order")
        print("3. View Open Orders")
        print("4. Mark Next Order as Complete")
        print("5. View End-of-Day Report")
        print("6. Exit")

    def _display_menu(self) -> None:
        print(f"Item{" "*15}Price")
        print(f"{"-" * 24}")
        for i in range(len(self._drinks)):
            drink = self._drinks[i]
            price = f"{self._prices[i]:.2f}"
            numspaces = 24 - len(drink) - len(price)
            print(f"{drink}{" " * numspaces}{price}")
    
    def _take_new_order(self) -> None:
        customer_name = input("Customer's Name: ")
        order = CustomerOrder(name = customer_name)
        print("Leave Drink Empty to Complete Order")

        while True:
            drink = input("Enter Drink: ").upper()
            if drink == "" or drink == "DONE":
                break
            elif drink not in self._menu: # O(1)! Thanks, hashmap!
                pass
            else:
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
                                    return # No implementation for revising an order, it'll   
                                           # just need to be remade
                                case "y":
                                    self._open_orders_queue.append(order)
                                    return
                                case _:
                                    pass
                    case _:
                        pass
            self._open_orders_queue.append(order)
            
    def _view_open_orders(self) -> None:
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
        if len(self._open_orders_queue) == 0:
            print("No orders in queue to complete.")
        else:
            complete = self._open_orders_queue.pop_front()
            print("Order Completed:")
            complete.repeat_order()
            for drink in complete.drinks():
                self._sales.add(drink)
            self._total_revenue += complete.get_total_price()

    def _view_report(self) -> None:
        print(f"Total Drink Sales: {len(self._sales)}")
        print(f"Total Revenue: {self._total_revenue:.2f}")
        print("Sales per Drink:")
        for drink in self._drinks:
            sales = self._sales.count(drink)
            numspaces = 20 - len(drink) - len(str(sales))
            print(f"{drink}:{" " * numspaces}{sales}")
