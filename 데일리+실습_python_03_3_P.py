infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]

value_age = list(old['age'] for old in infos)

sum_val = 0

for val in value_age:
    sum_val += val
    
print(sum_val)

