print('This program is to practice IO.');

#Test input()
str = input("Enter your Name: ");
print();print("Your name is: ", str);

#evaluation of input()
num = eval(input("Enter your expression: "));
print();print("Result of the expression entered is: ",num);

#File Handling
print();print("Let's test file handling now.");
fo = open("Sample.txt");
print("Name of the file: ", fo.name);
print("Access mode of the file: ", fo.mode);
print("Closed status of the file: ", fo.closed);
#print("Softspace of the file: ", fo.softspace);	##Doesn't work in Python3
print("Closing file.");
fo.close();
print("Status of the file now: ",fo.closed);

Writing into a file and then reading items
print();print("Creating a new file 'new_sample.txt' and writing some text in the same.");
fo = open("new_sample.txt", "w");
fo.write("This is a newly created file using python file handling.\nEvery time program runs, this file is replaced with a new one,\nas it opened in write mode.");
fo.close();
print("File creation, write and close complete. Now we will open the file in read mode, read from the file and display the content here: ");
jo = open("new_sample.txt");
str = jo.read();
print("Contents of the file: ", str);
jo.close();

print();print("Replacing/Creating a new file 'new_sample.txt' and writing and reading some text in the same.");
fo = open("new_sample.txt", "w+");
str = fo.read();
print("Contents of the file just after opening: ", str);
fo.write("This is a newly created/replaced file opened in read and write mode using python file handling.\nWe are writing and reading from the same time.");
print("File creation/replace and write complete. Now we will read from the file without closing it and display the content here: ");
fo.seek(0);		#This is to take the cursor back to 0 position to read the file.
str = fo.read();
print();print("Contents of the file after writing: ", str);
fo.close();
jo = open("new_sample.txt");
str = jo.read();
print();print("Contents of the file: ", str);
jo.close();

print();print("We will write to a file and practice tell() and seek() functions.");
fo = open("new_sample.txt", "w");
fo.write("0123456789abcdef");
print("Cursor position after writing to the file: ",fo.tell());
fo.close();
jo = open("new_sample.txt");
str = jo.read(5);
print("First 5 digits from the file: ", str);
print("Current cursor position: ",jo.tell());
str = jo.read(3);
print("Next 3 digits from the file: ", str);
print("Current cursor position: ",jo.tell());
jo.seek(5,0);		#seek with from values other than 0 is not supported by python 3.
print("New cursor position: ",jo.tell());
jo.close();

#OS Module - Remane and delete a file
import os;
print();print("File above created was new_sample.txt. We will open the file and check the name:");
fo = open("new_sample.txt");
print("Name of the file: ",fo.name);
#os.rename("new_sample.txt","new_filename.txt");	#This line throws error as we are trying to rename an opened file.
fo.close();
os.rename("new_sample.txt","new_filename.txt");	#This will work now as we have closed the file in previous command.
print("File name changed from new_sample.txt to new_filename.txt. Now we will try to access the file with the old name, which we will throw an error.");
#fo = open("new_sample.txt");	#This throws an error as file name changed.
fo = open("new_filename.txt");
print("New filename is: ", fo.name);
fo.close();

#Delete all created files:
os.remove("new_filename.txt");

#Directories
print();print("We will create a directory newdir now, then we will change the directory and and delete the directory after coming back out from the newdir.");
#os.chdir("newdir");	#This must throw error as newerror doesn't exists.
os.mkdir("newdir");
str = os.getcwd();
print("Current working directory is: ", str);
os.chdir("newdir");
str = os.getcwd();
print("Current working directory is: ", str);
os.chdir("..");
os.rmdir("newdir");

print(os.listdir());
print();print("***END***");
