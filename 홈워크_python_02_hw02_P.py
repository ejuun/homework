orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

orders_list = orders.split(',')
ice_count = 0

for i in range(len(orders_list)):
    if orders_list[i][:3] == '아이스':
        ice_count +=1
print(f'1. 아이스 음료 주문 : {ice_count}\n')

orders_sets = set(orders_list)
orders_sets_list = list(orders_sets)
print('2. 메뉴별 주문 수')
for i in range(len(orders_sets_list)):
    count = 0
    for j in range(len(orders_list)):
        if orders_sets_list[i] == orders_list[j]:
            count +=1
    print(f'{orders_sets_list[i]} : {count}')

# orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
# ordersspl = orders.split(',')
# set_orders = set(ordersspl)
# arr = [[i, orders.count(i)] for i in set_orders]
# print(arr)