class Category:
    

    def __init__(self, category, amount):
    
        self.category  = Category
        self.amount = amount

    #.....................Methods.................................................

    def deposit(self, amount):
        self.amount += amount
        return "You have successfully deposited ${} in {} category. \n Your current balance is ${}".format(amount, self.category, self.amount) 

    def check_balance(self, amount):
        if self.amount > amount:
            return True
        else:
            return False

    def withdraw(self, amount):
        self.amount -= amount
        return "You have successfully withdrawn ${} in {} category. \n Your current balance is ${}".format(amount, self.category, self.amount) 


    def transfer(self,amount,category):
        if not self.check_balance(amount):
            return "Unable to Complete Transfer"

        self.amount -= amount
        category.amount += amount
        return "You have successfully transferred ${} to {} Category".format(amount, category.category)


#...............................Budget Catgories...........................................


food_category = Category("Food", 500)
clothing_category = Category("Clothing", 300)
car_category = Category("Car Expenses", 600)


#.............................Testing Methods..............................................
print(food_category.deposit(300))

print(food_category.check_balance)

print(clothing_category.withdraw(200))

print(food_category.transfer (100, clothing_category))