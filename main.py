
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
num3 =[]
if len(num2) > len(num1):
    long = num2
else : long = num1
for i in range(len(long)):
    try: num3.append(num1[i])
    except: continue
    try: num3.append(num2[i])
    except: continue
print(num3)

# ******************************
# Make your Code
# ******************************

# print (num3) 
