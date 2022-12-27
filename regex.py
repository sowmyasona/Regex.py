# import re
# txt = "Learning python is easy"
# x = re.findall("^Learning.*easy$", txt)
# print(x)

# import re
# txt = "Learning python is easy"
# x = re.findall("py...n", txt)
# print(x)

import re
test_string= "Hello world"
x = re.findall("\AHello", test_string)
print(x)