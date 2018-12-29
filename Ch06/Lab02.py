count = 0
import random
cpuNo = random.randint(1,100)
userNo = 0

while cpuNo != userNo:
  userNo = int(input("1~100까지의 수를 입력하세요."))
  if cpuNo > userNo:
    print("입력한 숫자보다 큽니다.")
  elif cpuNo < userNo:
    print("입력한 숫자보다 작습니다.")
  else:
    print("맞았습니다, 축하합니다.")
  count = count + 1
print(count, "번만에 맞추셨습니다.")
  
