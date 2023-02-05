multiple = set()
for i in range(2,100):
    if i % 2 == 0:
        multiple.add(i)
    elif i % 7 == 0:
        multiple.add(i)

multiple_list = list(multiple)
multiple_sum = 0

for i in range(len(multiple_list)):
    multiple_sum += multiple_list[i]

print(multiple_sum)
