#!/usr/bin/env python3
# Tuples
t1 = ('Prime', 'Ix', 'Secundus', 'Caladan')
t2 = (1, 2, 3, 4, 5, 6)

# Accessing tuple values
print(t1[0])
print(t2[2:4])

# Checking membership
print('Ix' in t1)
print('Geidi' in t1)

# Lists
list2 = ['uli101', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635']
list2[0] = 'ica100'
print(list2[0])
print(list2)

# Trying to change a tuple value (this will raise an error)
try:
    t2[1] = 10  # This should raise an error since tuples are immutable.
except TypeError as e:
    print(f"Error: {e}")

# Slicing tuples
t3 = t2[2:3]
print(t3)

# Iterating through a tuple
for item in t1:
    print('item: ' + item)

