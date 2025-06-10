def show_orders(orders):
    """
    현재 주문 내역 출력 함수

    Args:
        orders (list): 주문 내역 리스트 (dict 요소)
    """
    
    if not orders:
        print("현재 주문이 없습니다.")

    else:
        for i, order in enumerate(orders):
            print(f"{i+1}. {order['menu_name']} — {order['price']:,}원")
            for idx, name in enumerate(order['flavor_names']):
                print(f"   - 맛 {idx+1}: {name}")


def canceled(orders):
    """
    주문 취소 처리 함수
    주문 내역을 출력하고 사용자가 취소를 원하는 주문을 삭제할 수 있게 함

    Args:
        orders (list): 현재 주문 내역 리스트

    Returns:
        bool: 남은 주문이 있으면 False (결제 진행) 없으면 True (처음으로 돌아감)
    """
    while True:
        if not orders:
            print("현재 주문이 없습니다.")
            return True
                  
        print("\n다시 주문 내역을 보여드립니다:")
        show_orders(orders)

        del_input = input("취소할 주문 번호를 입력하세요 (0 입력시 선택창으로): ").strip()
        if del_input == '0':
            return False
        if del_input.isdigit() and 1 <= int(del_input) <= len(orders):
            del_index = int(del_input) - 1
            removed = orders.pop(del_index)
            print(f"'{removed['menu_name']}' 주문이 삭제되었습니다.")
            return False
        else:
            print("잘못된 번호입니다.")
        

def check_out(orders):
    """
    최종 결제 금액 계산 함수

    Args:
        orders (list): 현재 주문 내역 리스트

    Returns:
        int: 총 결제 금액
    """
    print("\n💳 최종 주문 내역:")
    show_orders(orders)
    
    total_price = sum(order['price'] for order in orders)
    print('\n' + '='*45)
    print(f"💰 총 결제 금액: {total_price:,}원")
    return total_price


def member_ship(point_list, total_price):
    """
    포인트 적립 처리 함수
    전화번호로 적립 또는 신규 등록

    Args:
        point_list (list): 포인트 정보 저장 리스트
        total_price (int): 총 결제 금액

    Returns:
        str: 전화번호 (회원), 또는 "고객"
    """
    while True:
        point_q = input('포인트 적립하시겠습니까? (Y/N): ').strip().lower()
        if point_q == 'y':
            membership = input("전화번호를 입력해주세요: ").strip()
            saved_point = total_price // 100
            idx = -1
            
            for i, user in enumerate(point_list):
                if user['membership_nb'] == membership:
                    idx = i
                    break
                    
            if idx != -1:
                point_list[idx]['membership_point'] += saved_point
                total_point = point_list[idx]['membership_point']
            else:
                point_list.append({'membership_nb': membership, 'membership_point': saved_point})
                total_point = saved_point
                
            print(f"{saved_point}포인트 적립 완료 → 총 {total_point}포인트")
            return membership  # 함수 반환으로 name 대체
            
        elif point_q == 'n':
            return "고객"
        else:
            print('!(Y/N)로 입력해주세요!')
