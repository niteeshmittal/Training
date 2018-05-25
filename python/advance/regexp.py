print("This program is to test a regular expression.");

import re;

line = "GR_4456_PP_MASTER_USAGE_20180908.csv.gz";

print();print(line);

str = re.match(r'(\w{3})(\d{4})_(PP_MASTER_USAGE|POST_MASTER_USAGE|PP_MASTER_STATUS|POST_MASTER_STATUS)_(\d{4})(\d{2})(\d{2}).csv.gz', line);

print(str.group());

print(str);
