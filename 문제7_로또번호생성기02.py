import random

for i in range(1,6):
    print("로또 ; " ,sorted(random.sample(range(1,46),6)))