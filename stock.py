class Stock:
    def __init__(self):
        # formating data from stock.csv into a dictionary form
        with open("stock.csv", "r") as data_file:
            data = data_file.read().splitlines()

        self.__icecream_to_amount = {}
        for icecream in data:
            if icecream != "" and icecream != "Ice Cream, Amount":
                splitted_data = icecream.split(", ")
                self.__icecream_to_amount.update({splitted_data[0]:splitted_data[1]})


    def add(self, flavor, amount):
        # add an amount of flavor into stock.csv stock if the flavor is in stock.csv
        with open("stock.csv", "r") as data_file:
            stock_data = data_file.read().splitlines()
        
        add_valid = False
        with open("stock.csv", "w") as data_file:
            for each_data in stock_data:
                flavor_info = each_data.split(", ") 
                if flavor == flavor_info[0]:
                    flavor_info[1] = int(flavor_info[1]) + amount
                    add_valid = True
                each_data = f"{flavor_info[0]}, {flavor_info[1]}\n"
                data_file.write(each_data)

        if not add_valid:
            raise KeyError("Invalid flavor. Please try again.")


    def remove(self, flavor, amount):
        # remove an amount of flavor into stock.csv stock if the flavor is in stock.csv 
        self.add(flavor, -amount)


    def set(self, flavor, amount):
        # set an amount of flavor into stock.csv stock if the flavor is in stock.csv 
        with open("stock.csv", "r") as data_file:
            stock_data = data_file.read().splitlines()

        set_valid = False
        with open("stock.csv", "w") as data_file:
            for each_data in stock_data:
                flavor_info = each_data.split(", ")
                if flavor == flavor_info[0]:
                    flavor_info[1] = amount
                    set_valid = True
                each_data = f"{flavor_info[0]}, {flavor_info[1]}\n"
                data_file.write(each_data)

        if not set_valid:
            raise KeyError("Invalid flavor. Please try again.")


    def update(self, flavor, size):
        # remove some amount of ice cream in the stock based on the flavor and
        # size given
        if size == "small":
            self.remove(flavor, 1)
        elif size == "medium":
            self.remove(flavor, 3)
        elif size == "large":
            self.remove(flavor, 5)
        else:
            raise KeyError("Invalid size. Please try again.")


    def display(self):
        # display every flavor and amount of ice cream from stock.csv
        with open("stock.csv", "r") as data_file:
            stock_data = data_file.read().splitlines()
            for each_stock in stock_data:
                print(each_stock)