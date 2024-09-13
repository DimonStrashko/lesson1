# [0, 1, 0, 12, 3]
#  [0]
# [1, 0, 13, 0, 0, 0, 5]
list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
new_list = []
for x in list:
    if x != 0:
        new_list.append(x)

zero_count = list.count(0)

print(new_list + [0] * zero_count)