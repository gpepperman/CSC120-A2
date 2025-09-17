class ResaleShop:

    # What attributes will it need?
    inventory: int #how many computers does the store own?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory: int):
        self.inventory = inventory 

    def BuyComputer(self, amt: int):
        self.inventory += amt
    
    def SellComputer(self, amt):
        self.inventory -= amt
    
    #def Refurbish():
    
def main():
    CurrentInventory: ResaleShop = ResaleShop(10)
    CurrentInventory.BuyComputer(10)
    CurrentInventory.SellComputer(5)
    print(CurrentInventory.inventory)
    # What methods will you need?

if __name__ == "__main__":
    main()