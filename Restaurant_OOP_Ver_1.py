class Restaurant:
    def __init__(self):
        # Initialize the menu with predefined items and prices
        self.menu = {"burger": {"cheese burger": 50.00, "deluxe burger": 100.00},
                     "sides": {"fries": 30.00, "onion rings": 30.00},
                     "beverages": {"coke": 40.00, "iced tea": 30.00}
                     }
        #self.cash = 0

    def add_menu_category(self): # Placeholder for adding a new menu category, to be overridden in Menu class
        pass

    def add_menu_item(self): # Placeholder for adding a new menu item in an existing category, to be overridden in Menu class
        pass

    def cash_register(self, money: int, total: int): # Calculate change or return an error message if money is insufficient
        if money >= total:
            return money - total
        else:
            return "Inufficient amount!"

    def id_discount(self, id_type, total_pay): # # Apply discounts based on customer's ID type
        if id_type == "senior":
            x = total_pay * 0.2
            return total_pay - x
        elif id_type == "pwd":
            x = total_pay * 0.15
            return total_pay - x
        elif id_type == "":
            return total_pay
        else:
            print("Does not exist")
            

    #def show_cash(self):
        #print(f"Total Restaurant Money: {self.cash}")
   

class Menu(Restaurant):
    def __init__(self):
        super().__init__()

    def show_menu(self): # Display the restaurant's menu
        print("-------------MENU------------")
        items = self.menu.items()
        for key_1, value_1 in items:
            print(f"{key_1}: ")
            for key_2 in value_1:
                print(f"{key_2} - {value_1[key_2]}")
        print("-------------------------")

    def add_menu_category(self): # Allow the addition of a new menu category
        new_category = str(input("Category Name: "))
        self.menu[new_category] = {} # the dictionary of the value of self.menu
        # it must be outside the while loop or else it will replace the value element of the value of self.menu
        while True:
            new_item = str(input("Item Name: "))
            price = float(input("Item Price: "))

            self.menu[new_category][new_item] = price

            user_ask = input("Enter end: ")
            if user_ask == "end":
                break
            else:
                continue

    def add_menu_item(self): # # Allow the addition of a new menu item in an existing category
        user_category = input("Enter Category: ")
        user_item = input("Enter new item: ")
        user_price = int(input("Enter price: "))

        self.menu[user_category][user_item] = user_price

class Customer(Menu):
    def __init__(self, id_type: str):
        super().__init__()
        self.platter = []
        self.id_type = id_type

    # # Allow the customer to order food from the menu
    def order_food(self):
        while True:
            user_order = input("Enter your order [or type end]: ")
            flag = False # used for flag
            if user_order == "end":
                break
            else:
                for key, value in self.menu.items(): # it will loop the key and value from the self.menu
                    for i in value: # it will loop the key from the value dictionary
                        if user_order == i: # if user order matched with i then it will append it to the list
                            self.platter.append(user_order)
                            flag = True
                            # after that it will set the flag variable into True
                            break
                if not flag: # if it does not match, the variable will still be false
                    # if not True then print
                    print("Item does not exist!")
                else:
                    continue
        
    def show_platter(self):  # Display the customer's ordered items and their quantities
        count = {} # store the ordered food and its quantity
        for i in self.platter: # will loop the self.platter
            if i not in count: # if item does not have duplicate, its value will remain 1
                count[i] = 1
            else: # if item have duplicate, then it will add 1
                count[i] += 1
        print("---------PLATTER---------")
        for key, value in count.items():
            print(f"{key} - {value}")
        print("--------------------")

    def pay_food(self, money):  # Calculate the total cost of the ordered food, apply discounts, and calculate change
        count = {}
        total = 0

        for i in self.platter:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1

        for key, value in count.items(): # will loop through the count dictionary
            for a, b in self.menu.items(): # will loop through the self.menu
                for i, j in b.items(): # will loop through the dictionary of value "b"
                    if key == i:
                        x = value * j # multiply the value from the count to the value from b
                        total += x
                        print(f"{key} - {x}")
        print(f"ID: {self.id_type}")
        discount = super().id_discount(self.id_type, total)
        print(f"Total Amount: {total}")
        print(f"Your Cash: {money}")
        payment = super().cash_register(money, discount)
        print(f"Your Change: {payment}")
        
        
            





    
