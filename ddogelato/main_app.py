from order_core.order_flow import select_menu, select_flavors, cart, after_cart_menu
from utils.customer_utils import show_orders, canceled, check_out, member_ship


import datetime

store_name = '또!젤라또'

menu_list = [
    {'name':'또젤라또','count':'1가지맛', 'price':3000},
    {'name':'또또젤라또','count':'2가지맛', 'price':5000},
    {'name':'또또또젤라또','count':'3가지맛', 'price':7000}
]

flavor_list = [
    {'flavor':'달콤초코봄바람'},
    {'flavor':'새콤달콤딸기정원'},
    {'flavor':'요거트빛파도'},
    {'flavor':'말차소풍'},
    {'flavor':'체리팝송'},
    {'flavor':'포도에몽'},
    {'flavor':'바닐라하모니'},
    {'flavor':'쿠키크러쉬'},
    {'flavor':'소금바다우유'},
    {'flavor':'블루베리썸머'},
    {'flavor':'스윗피치'},
    {'flavor':'레몬샤워'},
]
point_list = []
all_orders = []

# ===== 메인 루프 시작 =====
while True:
    orders = []

    while True:
        order_num = select_menu(store_name, menu_list, flavor_list, point_list, all_orders)
        if order_num is None:
            continue
        selected_menu = menu_list[order_num]

        selected_flavors = select_flavors(selected_menu, flavor_list)
        if selected_flavors is None or not selected_flavors:
            continue

        if not cart(orders, selected_menu, selected_flavors):
            continue

        while True:
            action = after_cart_menu()

            if action == '1':
                break
            elif action == '2':
                print("\n 현재 주문 내역:")
                show_orders(orders)
                print()
            elif action == '3':
                canceled(orders)
                if not orders:
                    print("모든 주문이 취소되어 처음으로 돌아갑니다.\n")
                    break
            elif action == '4':
                break

        if not orders:
            break

        if action == '4':
            break

    if not orders:
        continue

    total_price = check_out(orders)
    if total_price == 0:
        print("주문이 없습니다. 처음으로 돌아갑니다.\n")
        continue

    name = member_ship(point_list, total_price)

    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    all_orders.append({
        'timestamp': now,
        'orders': orders.copy(),
        'total_price': total_price
    })

    print(f"\n{name}님, 주문 감사합니다! 또 오세요.")
    print("=" * 45)
