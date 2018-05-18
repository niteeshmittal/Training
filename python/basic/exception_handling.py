print("This program is to practice Exception Handling");

#Open a file that doesn't exists and catch the exception so the program goes on properly

try:
	fo = open("test.txt");
except IOError:
	print("File test.txt doesn't exists");
else:
	print("There was no error in file reading");
	fo.close();

print();print("***END***");
