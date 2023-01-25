class Power:

    def __init__(self, is_powered: bool):           # initialisation method for state of power pack
        self.is_powered = is_powered

    def set_power_level(self, is_powered: int):    # # allows you to set the attribute 'is_powered'
        self.is_powered = is_powered
        return self.is_powered

class RotaryPen(Power):                         # creates a new class using a parent class 'Power'

    def __init__(self, is_powered, correct_needle_type: bool):
        super().__init__(is_powered)                     # super refers to the parentclass (Power)
        self.correct_needle_type = self.set_needle(correct_needle_type)

    def set_needle(self, needle: str):              # allows you to set the attribute needle
        self.needle = needle

    def needle_checker(self, needle: str):  # allows you to check that the user has selected the right attribute for needle
        if needle == "Cartridge":
            return True        #this machine type can only accept cartridges
        else:
            return False        #if cartridge is not used it won't work

    def runmachine(self):                                                      #function to run the machine
        if self.needle == "Cartridge" and self.is_powered > 0:
            return print("Machine is up and running")                       #if powered and the needle is setup the machine will run
        else:
            return print("Something went wrong machine is not running ")    #if needle type is wrong or the machine is not powered it will not run

class Coil(Power):  # creates a new class using a parent class 'Power'

    def __init__(self, is_powered, correct_needle_type: bool):
        super().__init__(is_powered)  # super refers to the parentclass (Power)
        self.correct_needle_type = self.set_needle(correct_needle_type)

    def set_needle(self, needle: str):  # allows you to set the attribute needle
        self.needle = needle

    def needle_checker(self, needle: str):  # allows you to check that the user has selected the right attribute for needle
        if needle == "Needle Bar":
            return True        #this machine type can only accept Needle Bar's
        else:
            return False        #if Needle Bar's is not used it won't work

    def runmachine(self):                                               #function to run the machine
        if self.needle == "Needle Bar" and self.is_powered > 0:
            return print("Machine is up and running")                   #if powered and the needle is setup the machine will run
        else:
            return print("Something went wrong machine is not running ") #if needle type is wrong or the machine is not powered it will not run



setup_machine = RotaryPen(5, "Cartridge")           #creates a variable and sets the arguments for tattoo machine choosen, first argument is the power level, second is the needle type choosen

setup_machine.runmachine()                          #access the function to run machine within the variable we created

