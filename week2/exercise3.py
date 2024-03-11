# Find the sum of first N numbers divisible by 5 and 10

def natural(num):
    sum=0
    for i in range(num+1):
        if i%5 == 0 or  i% 10 == 0:
            sum += i
    return sum
num = int(input("enter a number :"))
print(natural(num))

