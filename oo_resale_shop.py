from computer import Computer

class ResaleShop:

    # What attributes will it need?
    inventory = []# type: ignore #how many computers does the store own?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, ComputerList):
        self.inventory = ComputerList 

    def BuyComputer(self, Computer):
        self.inventory.append(Computer)
    
    def SellComputer(self, Computer):
        if Computer in self.inventory:  # Check if the computer exists
            self.inventory.remove(Computer)
        else:
            print(f"Computer does not exist.")
    
   # def Refurbish(self, Computer):
        #if inventory[Computer] is not None:

   
def main():
    
    CID01: Computer = Computer("Mac Pro (Late 2013)","3.5 GHc 6-Core Intel Xeon E5",1024, 64, "macOS Big Sur", 2013, 1500)
    CID02: Computer = Computer("Mac Air (Late 2018)","3.5 GHc 6-Core Intel Xeon E5",1024, 64, "macOS Big Sur", 1018, 1600)
    CID03: Computer = Computer("Mac Pro (Late 2015)","3.5 GHc 6-Core Intel Xeon E5",1024, 64, "macOS Big Sur", 2015, 1800)

    ComputerList = [CID01, CID02, CID03]

    CurrentInventory: ResaleShop = ResaleShop(10)
    CurrentInventory.BuyComputer(CID01)
    CurrentInventory.BuyComputer(CID02)
    CurrentInventory.BuyComputer(CID03)
    #CurrentInventory.SellComputer(5)
    print(ComputerList)
    # What methods will you need?

if __name__ == "__main__":
    main()