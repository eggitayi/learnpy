import re

phone_number = r'^\d{3,4}\-\d{7,8}'
print re.match(phone_number, '025-55565655')
print re.match(phone_number, '0111 545454')

href = 'http://controller:8004/v1/4a5fcc8565c4428aaa9dedde248e828f/stacks/autoscale_test2/d655da47-8659-4706-a48b-9f389a5eade7'

project_id = r'v\d?/(.*)/stacks'
m = re.search(project_id, href)

print m.group(0), m.group(1)

w = r'\d*(\w\w)\d*'
m1 = re.match(w, '123fe12')
print m1.groups()
print m1.group(1)
