import random

x = random.randint(1,100)
y = random.randint(1,100)

while True:
  print( x, "+" , y , "=" )
  userNo = int(input())
  if userNo == ( x + y ):
    print("정답입니다.")
    break
  else:
    print("오답입니다.")
    print("다시 풀어보세요")
    

