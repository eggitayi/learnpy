import re

phone_number = r'^\d{3,4}\-\d{7,8}'
print re.match(phone_number, '025-55565655')
print re.match(phone_number, '0111 545454')

