import re

regex_string = "/d"

regex = re.compile(regex_string)
fp = open("CS4220 Organization.txt", "rt")
string = fp.read()

result = regex.findall(string)
print(result)