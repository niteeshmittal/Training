print("This program is for Strings functions test.");


print('Raw String');
print('a'r'\n''b');

print();print('String formatting');
i=4
str='we'
print('Hello, %s are testing integers %d'%('we',4));

print();print('Membership - in');
if ('n' in 'String'):
	print('N is there in string');
	
print();print('Membership - not in');
if ('f' not in 'String'):
	print('F is not there in string');

print();print('Paragraph testing');
print("""A paragraph with two lines. this is the first line.
this is the second line. This line contains TAB[\t].
This is the third line and this uses escape character [\\t].
Fourth line.\nLine break before this, so this becomes fifth line.
Sixth line, Let's see what does this NEWLINE do. Nothing actually."""); 
print();print('Program Over');