print("This program is to practice Lists Sequence.");

num_list=[1,2,3,4,5,6,7];
str_list=['Music','Books','Travel','Games','Cook','Movies'];
alpha_list=[31,'Bday',12,'Month',1989,'Year'];

print();print('This is the number only list: ',num_list);
print();print('This is the string only list: ',str_list);
print();print('This is the mixed(num & str) list: ',alpha_list);

#Update list
print();print('Update second value from num_list');
num_list[1]=4;
print('New num list: ',num_list);

print();print('Here number only list doesn\'t mean that it can contain only numbers. Now I will insert string value in num_list at 4th position. Also, vice-versa applies for string only list.');
num_list[3]='String';
print(num_list);
str_list[2]=234;
print(str_list);

#Delete List/From the list
print();print('Delete from the list');
print('Current List: ',num_list);
del num_list[1];
print('New List (second element deleted): ',num_list);

del num_list;
print();print('Deleted complete num_lsit. If we try to print the num_list which existed till now, code throws an error: ');
#Below line is commented because it halts the program
#print(num_list);

#Creating the deleted list
num_list=[1,2,3,4,5,6,7];
str_list[2]='Travel';

#Basic list operations
print();print('Basic List Operations');
print('Concatenate num & str list: ',num_list+str_list);
print();print('Repiting num_list');
print(num_list*2);
print();print('Length of the list');
print(len(num_list));
print(len(str_list));
print();print('Length of a list field. Note that \'int\' type list element don\'t have any length, only string type has. So the str_list in the code.');
#print(len(num_list[3])); -- This will throw an error.
print(len(str_list[1]));
print();print('Minimum value from the number list');
print(min(num_list));
print();print('Minimum value from the string list');
print(min(str_list));
print();print('Maximum value from the number list');
print(max(num_list));
print();print('Maximum value from the string list');
print(max(str_list));
print();print('Comparing lists');
if(num_list == str_list):
	print('lists are equal');
else:
	print('lists are not equal');

#Loop for the the list
print();print('Loops on the lists');
for i in num_list:
	print('Elemment in num_list are: ',i);

print();print('Loops on the lists with if condition');
for i in str_list:
	if ('e' in i):
		print('e exists in ',i);
	else:
		print('e doesn\'t exists in ',i);

#Reverse List		
print();print('Reverse the list');
print('Current list: ',num_list);
num_list.reverse();
print('Reversed list: ',num_list);

#Sort List
print();print('Sort the list');
print('Current list: ',num_list);
num_list.sort();
print('Sorted list: ',num_list);

#Clear List
print();print('Clear the list');
print('Current list: ',num_list);
num_list.clear();
print('Cleared list: ',num_list);

#Deleting list to free up the memory
del num_list; del str_list; del alpha_list;

#List of lists
emp = [["Dave", "Pattric", "IT", 500000, 5],
	   ["James", "Matthew", "HR", 2500000, 10]];
print();print(emp);
print(emp[0]);
print(emp[1]);
print(emp[0][1]);
for i in range(0,len(emp)):
	print(emp[i]);

print();print('Program Over');