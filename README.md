# Good Boy Ice Cream

##### Project Overview:
    This program is about making a receipt from user's ice cream order.

##### Feature:
    - Receive order (flavor, size, topping, container) of ice cream
      from user input
    - Add/Remove/Update/Display stock with appropriate amount
    - Record every order that is given
    - Search order by order number
    - Calculate price and change from the order and paid amount
    - Print receipt

##### Required libraries and tools:
    Python 3.10.8 with json library

##### Program Design:
    > Stock : This class is for stock interaction, such as adding, removing,
              setting and displaying stock information.
    > Price : This class is for calculating price.
    > Transaction : This class is for order recording and receipt displaying
                    from the database

##### Code structure:
    > main.py : This file is the main program
    > order.py : This file get input from user
    > price.py : This file is for calculating price from input from order.py
    > stock.py : This file is for adding, removing, updating and stock display
    > transaction.py : This file is for recording and displaying transaction
    > stock.csv : This file is for storing flavor stock and amount
    > menu.json : This file is for storing customer menu
    > price.json : This file stores data to price
                such as size to price, topping to price, container to price
