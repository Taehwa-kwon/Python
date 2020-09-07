coffee={'아메리카노':2500,'카페라떼':3000,'카푸치노':3500}
for c in coffee:
    print(c,end=' ')
print()

order = input("선택 : ")
for k,v in coffee.items(): # 튜플로 리턴 (키,값)
    if k==order:
        print(v)

