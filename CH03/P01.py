x = int(input("x:"))
y = int(input("y:"))
max_no = max(x,y)
min_no = min(x,y)

hap = x + y
cha = max_no - min_no
gop = x * y
avg = (x + y) / 2

print("두 수의 합:",hap)
print("두 수의 차:",cha)
print("두 수의 곱:",gop)
print("두 수의 평균:",avg)
print("큰 수:",max_no)
print("작은 수:",min_no)
