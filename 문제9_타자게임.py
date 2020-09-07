import random, time

word=["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]

n=1
quiz=random.choice(word)
input('시작!')
start = time.time()
while n<=5:
   print("{}번".format(n))
   print(quiz)
   x=input()
   if quiz ==x:
      print("통과!")
      n=n+1
      quiz=random.choice(word)
   else:
      print("오타! 다시도전!")  
end= time.time()
print('타자 시간 : {:.0f}초'.format(end-start))          