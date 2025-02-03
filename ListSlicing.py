# list_name [start: end- 1 ]

'''
# list_name [start: end- 1 ]

# List slicing allows you to extract a part of a list by specifying a start, end, and step value.
# Syntax: list_name[start:end:step]
# - start: The starting index of the slice.
# - end: The ending index of the slice (not included in the slice).
# - step: The step value determines the increment between each index for the slice.

# Examples:
# li1 = [10, 20, 30, 40, 50, 60]
# li1[0:4:1] -> [10, 20, 30, 40]
# li1[1::] -> [20, 30, 40, 50, 60]
# li1[::2] -> [10, 30, 50]
# li1[::-1] -> [60, 50, 40, 30, 20, 10]
# li1[-1::] -> [60]

Q what is List Slicing?
Is Used to create sublist from main list.
Synatx: list_name 
[start:end:step]


'''


li1 = [10, 20, 30,40,50,60]
sub_list = li1[0:4:1]
print(sub_list) # [10, 20,30,40,50,60]


sub_list2 = li1[1::]
print(sub_list2) #[20,30.40,50,60]

sub_list3 = li1[::2]
print(sub_list3) # [10, 30, 50]

reverse_lli1 = li1[::-1]
print(reverse_lli1) #[60, 50,40,30,20,10]

print(li1[-1::]) #60
