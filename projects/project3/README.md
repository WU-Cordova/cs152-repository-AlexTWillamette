Data Structures:

Menu - Hashmap of drink objects made from hardcoded tuples. I wanted to use drink names directly to get drink objects. I didn't want to label drinks with a number for inputting (which would be applicable if I used an Array, which would probably save a little memory and a little time by not hashing), especially as that would likely need to be adjusted whenever the menu gets changed. This way, the menu can be changed freely and nothing else needs to be changed. Using the drink name in the hashmap like menu(drink) gives the object, for use in adding to an order and such. The lookup for the drink is O(1), thanks to hashing used in the hashmap. Iterating over the menu is O(n), which is the minimum for iteration, so that's fine. The hashmap is also variable size, so no adjustments needed if the menu was made larger. There is probably some speed cost in hashing to get the objects inside, but I made that tradeoff as I prefer the simplicity it allows in retrieving drink objects from the menu.

Drink - Dataclass with some attributes. Attributes for a name as a string, a size as a string, and a price as a float. A drink doesn't have any more information, and all that is needed from it is to get that information, so its a dataclass as such. O(1) retrieval of information (assuming python handles classes/dataclasses in a not dumb way).

OrderItem - Class with two instance variables, a drink object and a customization. One part of a customer's order, with the drink they want and the customization for that drink. Customization is a string. Provides functionality to directly get the drink properties for ease of implementation, and to turn the order into a string for display. O(1) data retrieval. Mostly just a class to hold data to fit in with how data needs to be held.

Customer Order - Class with two instance variables, a string for a name, and a linkedlist of OrderItems. Represents a customer's order. Provides functionality for repeating (/printing out) the order, getting the drink names and total value, and adding as many drinks as are ordered. Linkedlists helps with this as it is variable size, and it's not like we're ever picking out a particular order from the list, so we don't indexing (like with an array). We're only ever iterating over the linkedlist (repeating the order, tallying price, returning all the drinks), which are all O(n), which is as good as iterating gets. We're also getting the length of the order (which is the length of the linkedlist) which is O(1) thanks to the linkedlists keeping track of its length with a count. 

All of the previous classes provide a clean way to handle the data involved in a kind of hierarchy, and each class has functions which help implementation, especially by having the class be able to do functions involving the data it has access to.

Order confirmation - Effectively just a boolean. The customer order class has the functionality to repeat the order (which is O(n), as it iterates over the items in the order). Whether or not the order is confirmed is just a yes or no, and so it is stored in a string with "y" or "n" for easy input, and its value is used to confirm or abort an order. Don't need anything more than a bool, or a string acting as a bool.

Open Orders Queue - Linkedlists of Customer Orders. Lets me add orders to the back and remove them from the front, which is what we want from a queue. We also print out everything in the queue, which is why I did not use a circularqueue (which also has the issue of being fixed size, and we don't know how many items might end up in the queue) or a deque, as those data structures do not have an iter, which is useful for accessing and therefore printing all the elements inside (without having to take the queue apart and put it back together). O(1) appending and popping, O(n) iterating (to print) (best we can do for iterating).

Completed Orders - A bag! We don't need to keep track of the whole orders, just how many of each kind. We can then use those tallies for the report, and use them and their price in the menu to get the sales/revenue. I used a bag to tally, as it can be used by just throwing in the drink name every time its part of an order, and I can ask how many of that drink are in it. It seemed like a simple object that did exactly the task I wanted, which felt easy to implement. Picked it primarily for simplicity. Because it uses a dictionary, which is just python's hashmap, my adding items in and getting their count is all O(1). 

Overall I made data structure choices because they fit the needs of the project, helped me organize my data better and provide functionality around how the data was structured, and made decisions prioritizing simplicity and flexibility (in menu size/changes, and in order sizes/length) over a small cost in speed and memory. (But hey, our computers are pretty powerful nowadays).





Instructions:

Start the program by opening the repository, going to "run and debug" on the left, selecting Project 3 from the dropdown in the topleft, and clicking the green arrow.

The interface and input is found in the terminal. The program greets you with the main menu instructions, from which you can enter one of the 6 commands by typing a number 1 through 6 and clicking enter to perform the action as described by the instruction. "h" or "help" can also be input to bring up the instructions again. After completing any of the following functions, the program returns to the main menu.

Entering "1" displays the menu.

Entering "2" creates a new order. Enter the customer's name as prompted. Then, add drinks to the order. Drinks are added by entering the name of drink, followed by entering any customization. To finish adding drinks to the order, hit enter with no input text when prompted for the next drink. If the order has no drinks when this is done, the order is aborted. Then, use y or n to indicate if the customer wants their order repeated back to them. If not, the order will be added to the queue. If yes, the order will be displayed to be read back, and y and n can then be used to indicate their confirmation. If no, the order is aborted. If yes, the order is added to the queue.

Entering "3" displays the open order queue. Starting from the bottom at first priority (closest to where you are entering inputs into the terminal), the orders are listed with their names, drinks, and customizations, and goes up, going down in priority.

Entering "4" marks the next order in the queue complete. This removes it from the queue, prints out the order, and adds it to the end of day tally.

Entering "5" prints out the end of day tally, which summarizes the sales and revenue of each drink and totals.

Entering "6" closes the program.





Bugs/Limitations:

No known bugs.

Limitations: Mostly just in the form of functionality I didn't give it that could be implemented. If an order is not confirmed, it has to be made from scratch. Can't fix a single item as such. Can't remove someone's order from the queue if it was say, refunded or cancelled. Only one size (medium) implemented.

What I'd add if I had more time:

(Just fix those limitations, so:)
- Sizes w/ variable pricing.
- Fixing orders if order is not confirmed.
- Removing orders from the queue if they're cancelled/refunded.
- Add some pretty emoji in the printout.





Sample Runs (Pasted Output):

1: Viewing the Menu and Taking an Order

Welcome to the Bearcat Bistro!

1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. View End-of-Day Report
6. Exit

Main Menu Select: 1

Item               Price
------------------------
Hot Choco           4.00
Latte               5.00
Mocha               5.00
London Fog          5.25
Italian Soda        4.00

Main Menu Select: 2

Customer's Name: Alex
To complete the order hit enter with no drink
Enter Drink: mocha
Enter Customization: none
Enter Drink: hot choco
Enter Customization: Extra Whipped Cream
Enter Drink: 
Confirmation requested? (y/n): y

Alex

Mocha, Medium, $5.00.
 none

Hot Choco, Medium, $4.00.
 Extra Whipped Cream

Confirm Order? y/n: y
Order placed!








2: Viewing Open Orders and Completing One:

Main Menu Select: 3

Orders:
------------------------------
In position 1:

Alex

Mocha, Medium, $5.00.
 none

Hot Choco, Medium, $4.00.
 Extra Whipped Cream

------------------------------

Main Menu Select: 4

Order Completed:

Alex

Mocha, Medium, $5.00. 
 none

Hot Choco, Medium, $4.00. 
 Extra Whipped Cream


Main Menu Select: 3

Orders:
------------------------------
No open orders.






Sample Run 3: End-of-Day Report

Main Menu Select: 5

End-of-Day Report:
-----------------------------------------
Drink Name         Qty Sold   Total Sales
Hot Choco          1          $4.00
Latte              0          $0.00
Mocha              1          $5.00
London Fog         0          $0.00
Italian Soda       0          $0.00

Total:             2          $9.00

Main Menu Select:








4: 2 More orders, showing that everything scales.

Main Menu Select: 2

Customer's Name: Nathan
To complete the order hit enter with no drink
Enter Drink: Latte
Enter Customization: watered down
Enter Drink: 
Confirmation requested? (y/n): n
Order placed!

Main Menu Select: 2

Customer's Name: Cole
To complete the order hit enter with no drink
Enter Drink: mocha 
Enter Customization: extra spicy
Enter Drink: london fog
Enter Customization: 
Enter Drink: 
Confirmation requested? (y/n): y

Cole

Mocha, Medium, $5.00.
 extra spicy

London Fog, Medium, $5.25.


Confirm Order? y/n: y
Order placed!

Main Menu Select: 3

Orders:
------------------------------
In position 2:

Cole

Mocha, Medium, $5.00.
 extra spicy

London Fog, Medium, $5.25.


------------------------------
In position 1:

Nathan

Latte, Medium, $5.00.
 watered down

------------------------------

Main Menu Select: 4

Order Completed:

Nathan

Latte, Medium, $5.00.
 watered down


Main Menu Select: 3

Orders:
------------------------------
In position 1:

Cole

Mocha, Medium, $5.00.
 extra spicy

London Fog, Medium, $5.25.


------------------------------

Main Menu Select: 5

End-of-Day Report:
-----------------------------------------
Drink Name         Qty Sold   Total Sales
Hot Choco          1          $4.00
Latte              1          $5.00
Mocha              1          $5.00
London Fog         0          $0.00
Italian Soda       0          $0.00

Total:             3          $14.00

Main Menu Select: 4

Order Completed:

Cole

Mocha, Medium, $5.00.
 extra spicy

London Fog, Medium, $5.25.



Main Menu Select: 4

No orders in queue to complete.

Main Menu Select: 5

End-of-Day Report:
-----------------------------------------
Drink Name         Qty Sold   Total Sales
Hot Choco          1          $4.00
Latte              1          $5.00
Mocha              2          $10.00
London Fog         1          $5.25
Italian Soda       0          $0.00

Total:             5          $24.25

Main Menu Select:

