import random

secret = random.randint(1,10)
temp = input("猜数\n")
guess = int(temp)
while guess != secret:
    if guess>secret:
        print("大了\n")
    else:
        print("小了\n")
    temp = input()
    guess = int(temp)
    
    if guess == secret:
            print("Yes\n")
print("结束游戏")
