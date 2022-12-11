from stock import Stock
import json

class Order:
    def get_order(self):
        # load menu and get order from customer and reformat the input into 
        # dictionary to list to pass onto other functions
        stock = Stock()

        with open("stock.csv", "r") as data_file:
            stock_data = data_file.read().splitlines()
            icecream_to_amount = {}
            for icecream in stock_data:
                if icecream != "" and icecream != "Ice Cream, Amount":
                    splitted_data = icecream.split(", ")
                    icecream_to_amount.update({splitted_data[0]:\
                        splitted_data[1]})

        with open("price.json", 'r') as data_file:
            price_data = json.load(data_file)
            
        flavor_list = []
        size_list = []

        print("[☐ Amount] -> ☐ Flavor -> ☐ Size -> ☐ Topping -> ☐ Container")
        scoop = input("Enter amount of scoop: ")
        while not scoop.isdigit():
            print("Amount of scoop must be a positive integer." \
                "Please try again.")
            scoop = input("Enter amount of scoop: ")

        for _ in range(int(scoop)):
            print("☑ Amount -> [☐ Flavor] -> ☐ Size -> ☐ Topping ->" \
                " ☐ Container")
            print("Flavor:")
            for each_icecream, each_amount in icecream_to_amount.items():
                print(f"{each_icecream.capitalize()}: {each_amount} available")

            flavor = input("Enter flavor: ").lower()
            while flavor not in icecream_to_amount:
                print("Invalid flavor, please select a valid flavor.")
                flavor = input("Enter flavor: ").lower()

            while int(icecream_to_amount[flavor]) <= 0:
                print(f"{flavor.capitalize()} is out of stock, please select \
                        another flavor.")
                flavor = input("Enter flavor: ").lower()
            print(f"{flavor.capitalize()} flavor selected.")
            print("-----------------------------------------------------------")

            print("☑ Amount -> ☑ Flavor -> [☐ Size] -> ☐ Topping ->"
                " ☐ Container")
            print("Size:")
            for each_size, each_size_price in price_data["size"].items():
                print(f"{each_size.capitalize()} {(each_size_price)}", end = \
                    ", ")
            print()

            size = input("Enter size: ").lower()
            while size not in price_data["size"]:
                print("Invalid size, please select a valid size.")
                size = input("Enter size: ").lower()
            print(f"{size.capitalize()} size selected.")
            print("-----------------------------------------------------------")

            flavor_list.append(flavor)
            size_list.append(size)
            stock.update(flavor, size)
        
        flavor_dict = {"flavor": flavor_list}
        size_dict = {"size": size_list}

        print("☑ Amount -> ☑ Flavor -> ☑ Size -> [☐ Topping] -> ☐ Container")
        print("Topping: ")
        print(*price_data["topping"], sep = ", ")
    
        topping = input("Enter topping: ").lower().split(", ")
        not_topping_list = [each_topping for each_topping in topping if \
                            each_topping not in price_data["topping"]]

        while not_topping_list != []:
            print("Invalid topping, please select a valid topping.")
            topping = input("Enter topping: ").lower().split(", ")
            not_topping_list = [each_topping for each_topping in topping if \
                                each_topping not in price_data["topping"]]

        while len(topping) > 3:
            print("Topping exceeds maximum. Only 3 toppings or less \
                can be selected.")
            print("Please select a valid topping")
            topping = input("Enter topping: ").lower().split(", ")

        if "none" in topping:
            print("No topping selected.")
        else:
            if len(topping) == 1:
                print(f"{topping[0].capitalize()} topping selected.")
            elif len(topping) == 2:
                print(f"{topping[0].capitalize()} and {topping[1].capitalize()} \
                    topping selected.")
            elif len(topping) == 3:
                print(f"{topping[0].capitalize()}, {topping[1].capitalize()}, \
                    and {topping[2].capitalize()} topping selected.")
        print("---------------------------------------------------------------")
        
        print("☑ Amount -> ☑ Flavor -> ☑ Size -> ☑ Topping -> ☐ Container")
        print("Container: ")
        for each_container, each_container_price in \
            price_data["container"].items():
            print(f"{each_container.capitalize()} {(each_container_price)}", \
                end = ", ")
        print()
            
        container = input("Enter container: ").lower()
        while container not in price_data["container"]:
            print("Invalid container, please select a valid container.")
            container = input("Enter container: ").lower()
        print(f"{container.capitalize()} container selected.")
        print("---------------------------------------------------------------")

        if "none" in topping:
            topping_dict = {"topping": ["None"]}
        else:
            topping_dict = {"topping": topping}
        container_dict = {"container": [container]}
        
        return flavor_dict, topping_dict, container_dict, size_dict