# 간식박스 관리 프로그램 1
snack_box = ['초코파이']
new_input = input('먹고 싶은 간식을 추가하세요. 단 쉼표(,)로 연결하세요.')
new_input = new_input.replace(' ', '')
new_snack = new_input.split(',')
snack_box += new_snack

print(snack_box)

# 간식박스 관리 프로그램 2
qty = int(input('간식 박스를 몇 세트로 포장할까요? 예: 2 -> 2box'))
snack_box *= qty
print(snack_box)

print(f'주문하신 간식 상자는 {snack_box[0]}, {snack_box[1]}, {snack_box[2]} 등 입니다. 확인해주세요.')

# 간식박스 관리 프로그램 3
snack_no = int(input(f'혹시 빼고 싶은 간식이 있으면 번호를 입력하세요 (0 ~ {len(snack_box)-1})'))
del snack_box[snack_no]
print(snack_box)

# 간식박스 관리 프로그램 4
# 찾고 싶은 간식이름을 입력하세요
# 있어요 or 없어요 출력
snack_find = input('찾고 싶은 간식이름을 입력하세요: ')
if snack_find in snack_box:
    print('있어요')
else:
    print('없어요')

# 간식박스 관리 프로그램 5
print('주문하신 간식박스는 뒤에서부터 다음과 같습니다')
print(f'{snack_box[::-1]}, 총 {len(snack_box)}개입니다.')