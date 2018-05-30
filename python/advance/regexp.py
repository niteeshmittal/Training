print("This program is to test a regular expression.");

import re;

line = "GR_4456_PP_MASTER_USAGE_20180908.csv.gz";

print();print("File name: ",line);

#str = re.match(r'(\w{3})(\d{4})_(PP_MASTER_USAGE|POST_MASTER_USAGE|PP_MASTER_STATUS|POST_MASTER_STATUS)_(\d{4})(\d{2})(\d{2}).csv.gz', line);
#str = re.match(r'(\w{3})(\d{4})(_)(PP_MASTER_USAGE|POST_MASTER_USAGE|PP_MASTER_STATUS|POST_MASTER_STATUS)(_)(\d{8})(.csv.gz)', line);
str = re.match(r'(\w{3})(\d{4})(_PP_MASTER_USAGE_|_POST_MASTER_USAGE_|_PP_MASTER_STATUS_|_POST_MASTER_STATUS_)(\d{8})(.csv.gz)', line);

list = [];
print("Regular Expression group: ", str.group());
print();print("Sepaerate groups:");

for i in range(1,6):
#for i in range(1,8):
	print("Group %d: %s" % (i, str.group(i)));
	list.append(str.group(i));
	
if (str.group(1) == 'GR_'):
	print();print("This file is Greece.");
else:
	print();print("This file is not greece.");
	

print("All groups stored in a list: ");print(list);

print(str);
