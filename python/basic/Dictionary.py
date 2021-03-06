print("This program is to practice Dictionary.");

#Creating Dictionary
#Empty Dictionary
edict={};
print();print('Empty Dictionary: ',edict);

#Single Value Dictionary with comma
person={'title':'mr','fname':'Pattrick','lname':'david','age':27,'org':'vodafone'}
print();print('Person dictionary: ',person);
print();print('Person dictionary Keys: ',person.keys());
print();print('Person dictionary Values: ',person.values());
print(person['fname']);

#Using for loop with the dictionary
print();print("Presenting Person's dictionary in a more appropriate way: ");
for i in person:
	print('%s of Person is: %s'% (i, person[i]));

print();print("Presenting Person's dictionary in a more appropriate way: ");
for i in person:
	print("{0} of Person is: {1}".format(i, person[i]));
	
print();print('Printing only values from the dictionary using a loop:');
for j in person.values():
	print(j);

#Update Dictionary
print();print("Let's change the first name of the person");
print("Current name: ",person['fname']);
person['fname']='Richard';
print("New name: ",person['fname']);

print();print('Delete from dictionary');
print('Current dictionary is: ',person);
del person['age'];
print('Deleted age with the key: ',person);
#del person['vodafone']			# Delete with value doesn't work.
#print('Deleted org with value: ',person);

print();print('String representation of the dictionary: ', str(person));

print();print('Type of dictionary: ',type(person));

#List of dictionaries
person_list = [{'title':'mr','fname':'Pattrick','lname':'david','age':27,'org':'vodafone'},
				{'title':'mr','fname':'Thomson','lname':'Dave','age':28,'org':'vodafone'}]

print();print("List of dictionaries: Dictionary of two persons:{0}".format(person_list));

print();print("dictionary 1 element: ", person_list[0]['fname']);
print();print("dictionary 2 element: ", person_list[1]['fname']);

print();print('Program Over');