print("This program is to test a simple class definition, it's instance creation and using the class.");

# A simple car class
class Car(object):
	wheels = 4;
	
	def __init__(self, model, make, color):
		self.model = model;
		self.make = make;
		self.color = color;
	
	def displaycar(self):
		#print(self.model, "is a ", self.color, "color", self.wheels, "wheeler light motor vehicle manufactured by ", self.make,".");
		print("%s is a %s color %d wheeler light motor vehicle manufactured by %s." % (self.model, self.color, self.wheels, self.make));
		
bmw = Car("BMW", "BMW", "Red");
bmw.displaycar();

c200 = Car("Mercedes", "Diamler", "Black");
c200.displaycar();


#Now we will define a more useful class with more attributes in order to understand class use in detail.
#Class is Employee which takes details of employee and can display details, calculate bonus, service year etc. Basically, we can have multiple instance for multiple employees.

class Employee:
	empcount = 0;
	bonus = 0;
	
	def __init__(self, fname, lname, dept, sal, tenure):
		self.fname = fname;
		self.lname = lname;
		self.dept = dept;
		self.sal = sal;
		self.tenure = tenure;
		Employee.empcount +=1;

	def displayemployee(self):
		print("Employee %d: %s %s" % (self.empcount, self.fname, self.lname));
		
	def calcbonus(self):
		self.bonus = 2 * self.tenure;
		print("Employee %d bonus is : %d " % (self.empcount, self.bonus));
	
	def newsal(self):
		newsal = self.sal + ((self.sal * self.bonus)/100);
		print("Employee %d new salary is : %d " % (self.empcount, newsal));

	def retiretime(self, age):
		if(age > 60):
			print("Employee %d has already retired from the job." % self.empcount);
		else:
			print("Employee %d is due to retire in %d years." % (self.empcount,(60 - age)));

emp = [["Dave", "Pattric", "IT", 500000, 5],
	   ["James", "Matthew", "HR", 2500000, 10]];

for i in range(0,len(emp)):
	print();
	emp[i][0] = Employee(emp[i][0], emp[i][1], emp[i][2], emp[i][3], emp[i][4]);
	emp[i][0].displayemployee();
	emp[i][0].calcbonus();
	emp[i][0].newsal();
	emp[i][0].retiretime(55);
	emp[i][0].retiretime(61);
	
print();print("*** END ***");