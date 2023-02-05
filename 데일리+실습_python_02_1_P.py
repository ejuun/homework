a = 3
b = 6
c = - 5
root_plus = ((-b) + ((b**2) - (4*a*c))**(0.5))/ (2*a)
root_minus = ((-b) - ((b**2) - (4*a*c))**(0.5))/ (2*a)

root = round(root_minus,4),round(root_plus,4)
print(root, type(root))