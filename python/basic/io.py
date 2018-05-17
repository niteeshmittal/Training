print('This program is to practice IO.');

#Test input()
#str = input("Enter your Name: ");
#print();print("Your name is: ", str);

#evaluation of input()
#num = eval(input("Enter your expression: "));
#print();print("Result of the expression entered is: ",num);

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

#Writing into a file and then reading items
print();print("Creating a new file 'new_sample.txt' and writing some text in the same.");
fo = open("new_sample.txt", "w");
fo.write("This is a newly created file using python file handling.\nEvery time program runs, this file is replaced with a new one,\nas it opened in write mode.");
fo.close();
print("File creation, write and close complete. Now we will open the file in read mode, read from the file and display the content here: ");
jo = open("new_sample.txt");
str = jo.read();
print("Contents of the file: ", str);
jo.close();