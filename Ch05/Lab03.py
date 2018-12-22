idt = input("ID를 입력하세요")
pwd = input("암호를 입력하세요")
cid = "Korea"
cpwd = "baseball"

if idt == cid:
  if pwd == cpwd:
    print("로그인 성공")
  else:
    print("암호가 틀렸습니다.")
else:
  print("존재하지 않는 ID 입니다.")
