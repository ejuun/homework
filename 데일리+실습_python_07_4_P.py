def fee(minute,distance):
    #대여 요금
    rental_fee = 1200 * (minute // 10)
    #보험료
    if minute % 30 >= 20 :
        premium_time = (minute // 30) + 1
    else:
        premium_time = minute // 30 
    premium = 525 * premium_time
    #주행요금
    if distance > 100:
        distance_fee = 100 * 170 + (distance-100) * 85
    else:
        distance_fee = distance * 170
    
    print(rental_fee + premium + distance_fee)



fee(600, 50)#=> 91000
fee(600, 110) #=> 10
