in_money = int(input("투입한 돈:"))
price = int(input("물건 값:"))
change = in_money - price
coin500 = int(change // 500)
coin100 = int((change % 500) // 100)
remain = change-500*coin500-100*coin100
print("거스름돈:",change)
print("500원 동전의 수:",coin500)
print("100원 동전의 수:",coin100)
print("완전 잔돈:", remain,"원")
