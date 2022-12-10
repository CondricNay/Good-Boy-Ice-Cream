import json

class Price:
    def __init__(self, flavor_dict, topping_dict, container_dict, size_dict):
        # initialize parameters in the class
        self.__topping = topping_dict["topping"]
        self.__container = container_dict["container"]
        self.__size = size_dict["size"]


    def get_price(self):
        # get price from user's menu
        with open("price.json", 'r') as data_file:
            price_data = json.load(data_file)

        total_price = 0
        for each_size in self.__size:
            total_price += price_data["size"][each_size]

        for each_container in self.__container:
            total_price += price_data["container"][each_container]  

        if self.__topping != ["None"]:
            total_price += 5*len(self.__topping)
           
        return total_price


    def get_change(self, paid_amount):
        # calculate change from paid amount and total price
        return paid_amount, paid_amount - self.get_price()
