print("This program is to practice Exception Handling");

#Open a file that doesn't exists and catch the exception so the program goes on properly

#print();print("We will try to open a file that doesn't exists and catch that exception. Program will continue to run instead to terminating.");
#try:
#	fo = open("test.txt");
#except IOError:
#	print("File test.txt doesn't exists");
#else:
#	print("There was no error in file reading");	#Program continues to run after this line also.
#	fo.close();
#
##Finally block
#import os;
#print();print("All files present: ",os.listdir());
#print();print("Let's try to remane a file after opening it.");
#try:
#	print("This is try block. We will open Sample.txt here:");
#	fo = open("Sample.txt");
#	print("Sample.txt opened. Contents from sample.txt are:");
#	str = fo.read();
#	print(str);
#	print("Now let's try to rename the file, which throws an exception:");
#	os.rename("Sample.txt", "new_sample.txt");
#except IOError:
#	print("This is except block. File couldn't be renamed because it was already opened.");
#finally:
#	print();print("This is finally block. We will close the file here and rename it now.");
#	fo.close();
#	os.rename("Sample.txt", "new_sample.txt");
#	print("All files present: ",os.listdir());
#	os.rename("new_sample.txt", "Sample.txt");
	
#Exception Arguments
print();print("Printing arguments of the exception caught.");
a=5;
try:
    c=a/0;
except ZeroDivisionError as z:
	print("You are trying to divide a number by 0, that is not allowed. {0}".format(z.args));
	
#Rasiing exceptions
#print();print("Raising an exception.");
#if a < 6:
#	raise ValueError("Number is less than 6");

#Rasiing and catching exceptions
print();print("Rasing and catching an exception.");
try:
	if a < 6:
		raise ValueError("Number is less than 6")
except ValueError:
	print("Exception encountered, looks like the number is less than 6.")
#	raise
	

print();print("***END***");
