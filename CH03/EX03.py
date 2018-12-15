Ame = 2000
Caf = 3000
Cap = 3500

Ame_no = int(input("오늘 판매한 아메리카노의 숫자는?"))
Caf_no = int(input("오늘 판매한 카페라떼의 숫자는?"))
Cap_no = int(input("오늘 판매한 카푸치노의 숫자는?"))

Ame_sum = Ame * Ame_no
Caf_sum = Caf * Caf_no
Cap_sum = Cap * Cap_no

All_sum = Ame_sum + Caf_sum + Cap_sum

print("총 매출은",All_sum,"원 입니다.")
