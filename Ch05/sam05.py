scoreKor = int(input("국어 점수를 입력하세요."))
scoreMath = int(input("수학 점수를 입력하세요."))
scoreEng = int(input("영어 점수를 입력하세요."))

avg = (scoreKor + scoreMath + scoreEng)/3

print("평균:", avg)

if avg >= 90:
  print("A학점 입니다.")
elif avg >= 80:
  print("B학점 입니다.")
elif avg >= 70:
  print("C학점 입니다.")
elif avg >= 60:
  print("D학점 입니다.")
else:
  print("F학점 입니다.")
