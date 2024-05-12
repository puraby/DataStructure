num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
num4 = int(input("Enter the fourth integer: "))
num_max = num1
if(num2 > num_max):
    num_max = num2
if(num3 >num_max):
    num_max = num3
if(num4 > num_max):
    num_max = num4


num_min = num1
if(num2 < num_min):
    num_min = num2
if(num3 <num_min):
    num_min = num3
if(num4 < num_min):
    num_min = num4
print()
print(f"The minimum number is {num_min} and the maximum number is {num_max}.")
