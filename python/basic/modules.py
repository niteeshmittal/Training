print('This program is to practice modules. fucntions.py will be used as a module for practice here.');

#import a default module and test
import time;

struct_time = time.localtime(time.time());
print();print('Structured Time: ',struct_time);

#import user defined module, function.py in this case:
import functions
print();print("Import functions command executes everything above from function.py. In order to avoid this, we import only specific function from function module.");

from functions import sum;
print();print("We just imported sum from functions, and nothing else was executed.");
total = functions.sum(12, 18);
print();print("Sum of 12 and 18 using sum function from function module is: ", total); 