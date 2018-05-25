from abc import ABCMeta, abstractmethod;

print("This program is to test a inheritence in classes.");

# A Parent vehicle class
class Vehicle:
	
	__metaclass__ = ABCMeta;
	
	wheels = 0;
	
	def __init__(self, model, brand, color):
		self.model = model;
		self.brand = brand;
		self.color = color;
	
	def displaycar(self):
		#print(self.model, "is a ", self.color, "color", self.wheels, "wheeler light motor vehicle manufactured by ", self.make,".");
		print("%s is a %s color %d wheeler light motor vehicle manufactured by %s." % (self.model, self.color, self.wheels, self.brand));
		
class Car(Vehicle):
	
	wheels = 4;
		
class Truck(Vehicle):

	wheels = 6;
	
	def displaycar(self):
		print("This is truck's method.");
		super().displaycar();

	
bmw = Car("BMW", "BMW", "Red");
bmw.displaycar();

bharat = Truck("Bharat", "TaTa", "Black");
bharat.displaycar();

#c200 = Car("Mercedes", "Diamler", "Black");
#c200.displaycar();
