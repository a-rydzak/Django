from apps.ninjas.models import *

# Have the first dojo be "CodingDojo Silicon Valley" in "Mountain View", "CA".
# Have the second dojo be "CodingDojo Seattle" in "Seattle", "WA".
# Have the third dojo be "CodingDojo New York" in "New York", "NY"

d_1 = Dojo.objects.create(name="CodingDojo Silicon Valley", city="Mountain View",state="CA")
d_2 = Dojo.objects.create(name="CodingDojo Seattle", city="Seattle",state="WA")
d_3 = Dojo.objects.create(name="CodingDojo New York", city="New York",state="NY")

# Have it include first_name, last_name of each ninja in the dojo.
# Each dojo can have multiple ninjas and each ninja belongs to a specific dojo.

Ninja.objects.create(first_name="a", last_name="c", dojo=d_1)
Ninja.objects.create(first_name="b", last_name="d", dojo=d_1)
Ninja.objects.create(first_name="q", last_name="222", dojo=d_2)
Ninja.objects.create(first_name="w", last_name="22", dojo=d_2)
Ninja.objects.create(first_name="q1", last_name="rr", dojo=d_3)
Ninja.objects.create(first_name="a11", last_name="ntr", dojo=d_3)
Ninja.objects.create(first_name="sffaaf", last_name="sfs", dojo=d_3)
Ninja.objects.create(first_name="fsdfds", last_name="fdsgg", dojo=d_1)