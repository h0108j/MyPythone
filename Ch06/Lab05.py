breads = ["호미빵","위트","화이트"]
meats = ["미트볼","소시지","닭가슴살"]
vegis = ["양상추","토마토","오이"]
sauses = ["마요네즈","허니 머스타드","칠리"]

for bread in breads:
  for meat in meats:
    for vegi in vegis:
      for sause in sauses:
        print(bread,"+",meat,"+",vegi,"+",sause)
