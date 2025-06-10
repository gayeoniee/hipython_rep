def select_menu(store_name, menu_list, flavor_list, point_list, all_orders):
    """
    메뉴를 선택하는 함수.
    선택된 메뉴 인덱스를 반환.
    """
    print("="*45)
    print(f'{store_name:^40}')
    print("="*45)
    print("어서오세요 아이스크림을 또 주는 또젤라또입니다\n")

    for i, menu in enumerate(menu_list):
        print(f'{i + 1}. {menu["name"]:<6} {menu["count"]:>12} {menu["price"]:>10,}원')
    print("="*45)

    order_input = input('주문할 메뉴 번호를 입력해주세요: ').strip().lower()

    if not order_input.isdigit() or not (1 <= int(order_input) <= len(menu_list)):
        print("잘못된 입력입니다. 다시 시도해주세요.\n")
        return None

    return int(order_input) - 1

def select_flavors(selected_menu, flavor_list):
    """
    맛 선택 함수
    선택한 메뉴에 따라 선택해야 하는 맛의 개수만큼 입력을 받음

    Args:
        selected_menu (dict): 사용자가 선택한 메뉴 정보 (name, count, price 포함)

    Returns:
        list[str] | None: 선택된 맛 리스트 (정상 선택), 0 입력 시 None 반환
    """
    flavor_count = int(selected_menu['count'][0])
    print(f"\n'{selected_menu['name']}' 선택 — {flavor_count}가지 맛을 골라주세요")

    cols_per_row = 3
    for i, fla in enumerate(flavor_list):
        print(f"{i+1}. {fla['flavor']:<10}", end='')
        if (i + 1) % cols_per_row == 0 or i == len(flavor_list) - 1:
            print()

    flavor_input = input("\n맛 번호들을 입력하세요 (예: 1, 3, 5) / 0 입력시 메뉴 선택으로 돌아가기: ").strip()

    if flavor_input == '0':
        print("맛 선택을 취소하고 메뉴로 돌아갑니다.\n")
        return None  # flavor_canceled 대신 None 반환

    parts = flavor_input.split(',')
    flavor_nums = [int(p.strip()) - 1 for p in parts if p.strip().isdigit()]

    if len(flavor_nums) != flavor_count or any(i < 0 or i >= len(flavor_list) for i in flavor_nums):
        print(f"정확히 {flavor_count}가지 맛을 정확히 입력해주세요.")
        return []

    selected_flavors = [flavor_list[i]['flavor'] for i in flavor_nums]
    return selected_flavors


def cart(orders, selected_menu, selected_flavors):
    """
    주문 확인 및 장바구니 추가 함수
    현재 선택한 메뉴와 맛을 출력하고 사용자에게 장바구니 추가 여부를 확인

    Args:
        orders (list): 현재 주문 목록 리스트 (dict 요소)
        selected_menu (dict): 선택된 메뉴 정보
        selected_flavors (list): 선택된 맛 리스트

    Returns:
        bool: 장바구니에 추가(True), 취소(False)
    """
    print("\n선택한 주문:")
    print(f"메뉴: {selected_menu['name']}") # 선택한 메뉴(사이즈) 
    for idx, name in enumerate(selected_flavors):
        print(f" - 맛 {idx+1}: {name}") #맛 순번과 맛이름
    print(f"가격: {selected_menu['price']:,}원") #총 가격

    while True:
        confirm = input("\n이 주문을 장바구니에 추가할까요? (Y: 추가 / N: 취소): ").strip().lower()
        if confirm == 'y':               
            orders.append({
                'menu_name': selected_menu['name'],
                'flavor_names': selected_flavors,
                'price': selected_menu['price']
            })
            print("주문이 장바구니에 추가되었습니다.\n")
            return True
        elif confirm == 'n':
            print("주문이 취소되었습니다.\n")
            return False
        else:
            print('!(Y/N)로 입력해주세요!')

def after_cart_menu():
    """
    장바구니 담은 후 사용자 선택 메뉴
    1: 추가 주문, 2: 주문 내역 보기, 3: 주문 취소, 4: 결제 진행
    """
    print("무엇을 하시겠습니까?")
    print("1. 추가 주문")
    print("2. 주문 내역 보기")
    print("3. 주문 취소")
    print("4. 결제 진행")
    
    while True:
        choice = input("번호를 선택해주세요: ").strip()
        if choice in ['1', '2', '3', '4']:
            return choice
        else:
            print("1~4번 중에서 선택해주세요.\n")