#Directory

try:
	fo = open("phonenum.txt")
	#print("phonenum.txt exists. We are good to go.")
except IOError as e:
	if (e.args[1] == "No such file or directory"):
		#print("File doesn't exists. Creating a phonenum.txt.")
		fo = open("phonenum.txt", "w")
finally:
	fo.close()

opt = input("1 for store and 2 for read: ")
print(f"You chose {opt}")

#if (opt == '1'):
#	name = input("Enter you name: ")
#	print(f"You entered {name}")
#	fo = open("phonenum.txt", "a")
#	#fo.write("\n" + name)
#	fo.write(name + "\n")
#	fo.close()
#elif (opt == '2'):
#	print("You chose to read and display the file.")
#	fo = open("phonenum.txt")
#	str = fo.read()
#	print(str)
#	fo.close()
#else:
#	print("Functionality under development.")

namelist = []
if (opt == '1'):
	while (opt == '1'):
		name = input("Enter your name: ");
		print(f"You entered {name}");
		namelist.append(name);
		opt = input("1 to coninue saving more names\n2 to display the current list\n3 to display file content: ");
	print(namelist);
	fo = open("phonenum.txt", "a");
	for i in namelist:
		fo.write(i + "\n");
	fo.close();
	
if (opt == '2'):
	print();print("You chose to display the current list of names given by user.\nCurrent list: {0}".format(namelist));
	opt = input("3 to display file content: ");
	
if (opt == '3'):
	print();print("You chose to read and display the file.");
	fo = open("phonenum.txt");
	str = fo.readlines();
	#print(str);
	for x in str:
		print(x.strip());
	fo.close();
else:
	print("You chose to exit.");