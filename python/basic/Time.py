import time;	#to use the time funtions
import calendar;	#to use calendar funtions

print('Programs to Test Time in Python');

struct_time = time.localtime(time.time());
print('Structured Time: ',struct_time);

asci_time = time.asctime(time.localtime(time.time()));
print();print('Readable time format: ', asci_time);

cal=calendar.month(2018, 5, w=10, l=5);
print();print('Calender for the current month: ', cal);

print(calendar.calendar(2018, w=2, l=2, c=10)); #w is width of the day, l is lines(2 means, every alternate line) and c is for spaces between months

print();print('***End***');