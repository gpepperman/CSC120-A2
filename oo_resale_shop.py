from computer import Computer #import the computer class and its functions
""""
This class has all the attributes of what a resale shop would have (just an inventory)in this case. 
It also includes all of the operations and functions that do behaviors inside of the Resale Shop: 
    Buying, Selling, and Refurbishing Computers in addition to inventory checking.
"""

class ResaleShop:

    inventory = []# type: ignore #this defines the inventory as an open list

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = [] #this defines the inventory as an open list

    def BuyComputer(self, Computer): #this function adds a computer to the inventory list
        self.inventory.append(Computer)
    
    def SellComputer(self, Computer): #this function adds a computer to the inventory list
        if Computer in self.inventory:  # Check if the computer exists
            self.inventory.remove(Computer) # If the computer is in the inventory, remove it
        else:
            print(f"Computer does not exist.") # If computer is not in inventory, say so
    
    def Refurbish(self, Computer: Computer):
        if Computer in self.inventory: #check if computer is in inventory
        # Adjust the price depending on year
            if Computer.year_made < 2000:
                Computer.price = 0
            elif Computer.year_made < 2009:
                Computer.price = 100
            elif Computer.year_made < 2012:
                Computer.price = 250
            elif Computer.year_made < 2018:
                Computer.price = 550
            else:
                Computer.price = 1000
        else:
            print("Computer not found in inventory.") #if computer is not in inventory, say so

    def PrintInventory(self):
        if not self.inventory:
            print("Inventory is empty.") #if the inventory is empty, say so
        else:
            for computer in self.inventory:
                print(computer) #if the inventory has computers in it, print the computers as defined in the computer class

"""
The main section includes
    Created Computers, I aribitraily created 3 computers with different descriptions, years, and prices
    Created the ResaleShop with a list to be filled with computers
    Use the already defined function to add the computers to the inventory list of MyResaleShop
    Use the refurbish function to update the prices of the computer to match their years
    Sell a computer
    Lastly print the inventory with the short descriptions
"""
   
def main():
    
    #Define computers, with ComputerID numbers
    CID01: Computer = Computer("Mac Pro (Late 2013)","3.5 GHc 6-Core Intel Xeon E5",1024, 64, "macOS Big Sur", 2013, 1500)
    CID02: Computer = Computer("Mac Air (Late 2019)","3.5 GHc 6-Core Intel Xeon E5",1024, 64, "macOS Big Sur", 2019, 1600)
    CID03: Computer = Computer("Mac Pro (Late 2023)","3.5 GHc 6-Core Intel Xeon E5",1024, 64, "macOS Big Sur", 2023, 1800)

    #Create a resale shop
    MyResaleShop: ResaleShop = ResaleShop()

    #Use the BuyComputer function to add computers to shop
    MyResaleShop.BuyComputer(CID01)
    MyResaleShop.BuyComputer(CID02)
    MyResaleShop.BuyComputer(CID03)
    
    #Update computer price based off age
    MyResaleShop.Refurbish(CID01)
    MyResaleShop.Refurbish(CID02)
    MyResaleShop.Refurbish(CID03)

    #Remove a computer from inventory by selling it
    MyResaleShop.SellComputer(CID02)

    #Print the inventory list
    MyResaleShop.PrintInventory()

if __name__ == "__main__":
    main()