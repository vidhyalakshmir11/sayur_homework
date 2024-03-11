#Find the sum of first N numbers  

def natural(num):
    sum =0 
    for i in range(num+1):
            sum += i
    return sum
num = int(input("enter a number :"))
print(natural(num))

