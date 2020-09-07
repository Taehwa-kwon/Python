import random

com=random.sample(range(1,10),3)    
print(com) 
strike = 0
check=0
print("시작")
while strike != 3:
    strike = 0
    ball = 0
    guess = list(input("3자리 숫자를 입력하세요 : "))
    print(guess)
    for a in guess:
        for b in com:
            if int(a)==b:
                if guess.index(a)==com.index(b):
                    strike+=1
                else:
                    ball+=1
    check+=1
    print("스트라이크:%d, 볼:%d, 시도횟수:%d" %(strike,ball,check)) 
print("정답")
                    
                    