class Computer:

    # Define all the attributes a computer has
        #all attributes were pulled from the procedural file!
    description: str 
    processor_type: str
    hard_drive_capacity: int
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    
    #define constructors
    #defines all of the attributes in a contructor
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    
    #defines a shorter computer description for ease when printing list of inventory
    def __str__(self):
        return f"{self.description} ({self.year_made}) - ${self.price}"

    #defines a mannual function that updates the price of a computer to whatever the store wants
    def UpdatePrice(self, price:int):
        self.price = price    # What methods will you need?
