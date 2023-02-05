blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

dic_blood = {}
for type in blood_types:
    if type in dic_blood:
        dic_blood[type] += 1
    else:
        dic_blood[type] = 1

print(dic_blood)
