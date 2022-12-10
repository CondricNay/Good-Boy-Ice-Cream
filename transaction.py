import json

class Transaction:
    def __init__(self, flavor_dict, topping_dict, container_dict, size_dict, \
                total_price, paid_amount, change):
        # initialize parameters in the class, set up order data in json format
        # and load up menu.json file
        self.__flavor = flavor_dict["flavor"]
        self.__topping = topping_dict["topping"]
        self.__container = container_dict["container"]
        self.__size = size_dict["size"]
        self.__total_price = total_price
        self.__paid_amount = paid_amount
        self.__change = change

        self.__all_menu_list = []
        self.__new_menu =  {

                "Ice Cream" : {

                    "Flavor" : self.__flavor,

                    "Topping" : self.__topping,

                    "Container" : self.__container,
                    
                    "Size" : self.__size,

                    "Price" : float(f"{self.__total_price:.2f}"),

                    "Paid Amount" : float(f"{self.__paid_amount:.2f}"),

                    "Change" : float(f"{self.__change:.2f}")

                }
            }
        try:
            with open("menu.json", "r") as data_file:
                self.__all_menu_list = json.load(data_file)
        except FileNotFoundError:
            pass


    def record(self):
        # record current order into menu.json
        with open("menu.json", "w") as data_file:
            self.__all_menu_list.append(self.__new_menu)
            json.dump(self.__all_menu_list, data_file, indent=4)

    
    def search(self, index=0):
        #search order by index (current order if order not given) from menu.json
        return print(self.__all_menu_list[index-1])


    def display(self, index=0):
        # display order by accessing ice cream flavor, topping, container, size
        # from menu.json
        flavor_list = self.__all_menu_list[index-1]["Ice Cream"]["Flavor"]
        topping_list = self.__all_menu_list[index-1]["Ice Cream"]["Topping"]
        container_list = self.__all_menu_list[index-1]["Ice Cream"]["Container"]
        size_list = self.__all_menu_list[index-1]["Ice Cream"]["Size"]
        print("---------------------------------------------------------------")
        print("            Goob Boy Ice Cream Shop\n")
        print(f"Ice Cream:                            {self.__total_price:.2f}")
        print(f"    Flavor: ")
        for i in range(len(flavor_list)):
            print(f"     - {flavor_list[i].capitalize()}"
             f" ({size_list[i].capitalize()}) x1")
        print(f"    Topping: ")
        for each_topping in topping_list:
            print(f"     - {each_topping.capitalize()}")
        print(f"    Container: ")
        for each_container in container_list:
            print(f"     - {each_container.capitalize()}")
        print("---------------------------------------------------------------")
        print(f"Total Price:                          {self.__total_price:.2f}")
        print(f"Cash:                                 {self.__paid_amount:.2f}")
        print(f"Change:                               {self.__change:.2f}")
        print()
        print(f"        THANK YOU FOR YOUR PATRONAGE")