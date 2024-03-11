'''
Parking garage problem
1.Write a program to calculate the revenue generated in a parking garage in a shopping mall

Parking fee is 
If you return within 15 mins, its free
Rs 100 for the first hr
Rs 150 for each hr after that. 
Fee is calculated in 30 min increments. (meaning, if you spent 25 mins, you will be charged for 30 mins
If you spend 35 mins, you will be charged for one hr)
Get entry time and exit time from customer as input and display the fee.

2.same as above. End the program if 24hrs passes from when the first customer comes in. 
Print the total fees collected.

3. Same as above, adding more condition.
The parking garage has 10 spaces numbered from 1 to 10.
THere is a car entering or exiting every 10 mins.
When a car enters, you need to tell them which lot is allotted for them.
When the customer comes to pick up the car, get the lot number as input and calculate the fees.

Use arrays if needed.
'''
from datetime import datetime

def get_time_gap(star_time_str, end_time_str):
  
  try:
    start_time = datetime.strptime(start_time_str, "%H:%M")
    end_time = datetime.strptime(end_time_str, "%H:%M")
  except ValueError:
    print("Invalid time format. Please use HH:MM (e.g., 10:20).")
    return
  time_gap = end_time - start_time
  print("Time Gap is ",time_gap)
  hours = time_gap.seconds // 3600
  minutes = (time_gap.seconds % 3600) // 60
  print(f"Time Gap: {hours}h:{minutes}m")
  time = str(hours) +":"+str(minutes)
  return hours,minutes 

def fee(hr,minu):
    #min = time. split(",")
    #comeBack =int(min[0])*60 + int(min[1])
    comeBack = hr*60 + minu
    print("total minutes ",comeBack )
    amount =0
    if comeBack <=15:
        amount +=  0
        return 
    elif comeBack >=60 or comeBack ==35 :
        amount +=100
        comeBack -=60
    while comeBack>=60 :
        if comeBack  !=0 and comeBack >=60:
            amount+= 150
            comeBack-=60
        else:
            break
    return amount 
totalFees = 0
while True:
    start_time_str = input("Enter starting time (HH:MM): ")
    end_time_str = input("Enter ending time (HH:MM): ")
    hr,minu = get_time_gap(start_time_str,end_time_str)
    fees = fee(hr,minu)
    print("Fees is ",fees)
    ask = input("Stop / No?")
    if ask.lower() == "stop":
       totalFees += fees
       print("Total Collected Fees is ",totalFees)
       break
    