import tkinter as tk
from tkinter import ttk
class Animal:
    def __init__(self,quantity,habitant,species):
        self.quantity = quantity
        self.habitat = habitant
        self.species = species
    def checkHabitat(self):
        print("Animal Habitat") 
    def getQuantity(self):
        print(f"{self.species } in the zoo are {self.quantity}") 
    def checkHabitat(self):
        print("Animal Habitat") 
    def addAnimal(self,quantity):
        self.quantity+=quantity
    def decreaseAnimal(self,quantity):
        self.quantity-=quantity
class Mammal(Animal):
    def __init__(self,quantity, habitant,species):
        self.type = "Mammals"
        super().__init__(quantity,habitant,species)
    def checkHabitat(self):
        print(f"Looks like the {self.species} are nurturing") 
class Bird(Animal):
    def __init__(self,quantity, habitant,species):
        self.type = "Birds"
        super().__init__(quantity,habitant,species)
    def checkHabitat(self):
        print(f"Looks like the {self.species} are nesting") 
class Fish(Animal):
    def __init__(self,quantity, habitant,species):
        self.type = "Fish"
        super().__init__(quantity,habitant,species)
    def checkHabitat(self):
        print(f"The {self.species} are eating") 
class Invertebrate(Animal):
    def __init__(self,quantity, habitant,species):
        self.type = "Invertebrate"
        super().__init__(quantity,habitant,species)
    def checkHabitat(self):
        print(f"The {self.species} are molting") 
class Reptile(Animal):
    def __init__(self,quantity, habitant,species):
        self.type = "Reptiles"
        super().__init__(quantity,habitant,species)
    def checkHabitat(self):
        print(f"The {self.species} are basking") 
class Amphibian(Animal):
    def __init__(self,quantity, habitant,species):
        self.type = "Amphibians" 
        super().__init__(quantity,habitant,species)
    def checkHabitat(self):
        print(f"The {self.species} are doing metamorphosis") 
        print("Animal Habitat") 

#Actual Implementation
elephant = Mammal(3,"Grassland Area","Elephants")
elephant.checkHabitat()
elephant.getQuantity()

eagle = Bird(5,"Aviary Area","Eagles")
eagle.checkHabitat()
eagle.getQuantity()

sunFish = Fish(2,"Aquatic Area","Sunfish")
sunFish.checkHabitat()
sunFish.getQuantity()

tilapia = Fish(3,"Aquatic Area","Tilapia")
tilapia.checkHabitat()
tilapia.getQuantity()

butterfly =Invertebrate(10,"Garden Haven","Butterfly")
butterfly.checkHabitat()
butterfly.getQuantity()

crocodile =Reptile(5,"Fresh Water(PONDS)","Crocodile")
crocodile.checkHabitat()
crocodile.getQuantity()
axolotl =Amphibian(10,"Aquarium Area","Axolotl")
axolotl.checkHabitat()
axolotl.getQuantity()
axolotl.addAnimal(10)
axolotl.getQuantity()
axolotl.decreaseAnimal(5)
axolotl.getQuantity()



#class App:
#    def __init__(self,root):
#        self.root = root
#        self.root.title = ("Something")
         
#root = tk.Tk()
#app = App(root)
#root.mainloop()