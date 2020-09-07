'''
import random

com=random.randint(1,100)
count=0
print('답 :',com)
while True:
    input_no = int(input('1~100사이 숫자를 입력하세요\n'))
    if com==input_no:
        count+=1
        print('정답입니다. {}번만에 맞추셨습니다.'.format(count))
        break
    elif com>input_no:
        count+=1
        print('더 큰수를 입력하세요')
    else:
        count+=1
        print('더 작은수를 입력하세요')
'''

import random,time

com=random.randint(1,100)
count=0
print('답 :',com)
input("시작!")
start = time.time()
while True:
    input_no = int(input('1~100사이 숫자를 입력하세요\n'))
    count+=1
    if com==input_no:
        print('정답입니다. {}번만에 맞추셨습니다.'.format(count))
        break
    elif com>input_no:
        print('더 큰수를 입력하세요')
    else:
        print('더 작은수를 입력하세요')
end = time.time()
t = end - start
print('걸린시간은 {:.0f}초입니다.'.format(t))        