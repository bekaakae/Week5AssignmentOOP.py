#question 1

class FootballPrinciple:
    def __init__(self, name, formation, style):
        self.name = name
        self.formation = formation
        self.style = style
    
    def describe(self):
        return f"{self.name} uses {self.formation} formation with {self.style} style"
    
    def train(self):
        return "Running basic drills"
# Inherited class - specific playing philosophy
class PlayingPhilosophy(FootballPrinciple):
    def __init__(self, name, formation, style, pressing_intensity):
        super().__init__(name, formation, style)
        self.__pressing = pressing_intensity  # Encapsulated attribute
    
    # Getter method for encapsulated attribute
    def get_pressing(self):
        return self.__pressing
    
    # Polymorphism - overriding parent method
    def train(self):
        return "Running intensive tactical sessions"
    
    def match_plan(self):
        return f"High press ({self.__pressing}/10) and quick transitions"

# Create objects
tiki_taka = FootballPrinciple("Tiki-Taka", "4-3-3", "possession")
gegenpress = PlayingPhilosophy("Gegenpress", "4-2-3-1", "aggressive", 9)

print(tiki_taka.describe())  # Tiki-Taka uses 4-3-3 formation with possession style
print(gegenpress.train())    # Running intensive tactical sessions
print(gegenpress.get_pressing())  # 9 (accessed through getter)    


#Question 2

# Base class
class Vehicle:
    def move(self):
        pass

# Car class
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Plane class
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Boat class
class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

# Create objects
car = Car()
plane = Plane()
boat = Boat()

# Same action, different behaviors
vehicles = [car, plane, boat]

for vehicle in vehicles:
    print(vehicle.move())