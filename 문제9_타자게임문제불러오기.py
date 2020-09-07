import random, time
w=["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]

while True:
   print("1.문제불러오기  2.타자게임  3.종료하기")
   menu = input("메뉴를 선택하세요\n")
   if menu=='1':
      f=open('./python_basic/word.txt','r',encoding='UTF8')
      line = 1
      #w.clear() 기존문제 제거하고 추가하기
      while line:
         line = f.readline().replace("\n","")
         if not(line==''):
            w.append(line)
      print(w)
   elif menu=='2':
      n=1
      q=random.choice(w)
      input('시작!')
      start = time.time()
      while n<=5:
         print("{}번".format(n))
         print(q)
         x=input()
         if q ==x:
            print("통과!")
            n=n+1
            q=random.choice(w)
         else:
            print("오타! 다시도전!")  
      end= time.time()
      print('타자 시간 : {:.0f}초'.format(end-start))        
   elif menu=='3':
      break

