import random
num = ("Enter number between 1 to 100")
rand = random.randint(1,100)
count = 0
while(True):
    count += 1
    num = int(input("Enter number"))
    if(num > rand):
        print("Try small")
    elif(num<rand):
        print("Try Bigger")     
    else:
        print("Hurray you did it")
        break
    print(f"attemp {count}")
print(f"you did it in {count} attemp ")