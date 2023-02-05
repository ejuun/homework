for i in range(5):
    concen = input()
    salt_water = int(input())
    if concen == 'Done':
        break
    concen = int(concen)
    salt = (concen / 100) * salt_water 
