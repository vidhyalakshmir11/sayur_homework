parkingLot =[]

def initParking(row, coln):
    global parkingLot
    parkingLot = []
    for i in range(0, row):
        parkingLot.append([])
        for j in range(0, coln):
            parkingLot[i].append(0)
    print(f"Parking lot with {row} rows and {coln} columns is \n{parkingLot}")


def assignParking(carId):
    # find an empty spot
    for parkingRow in range(0, len(parkingLot)):
        for spot in range(0, len(parkingLot[parkingRow])):
            if parkingLot[parkingRow][spot] == 0:
                print("\nFound available spot at row", parkingRow, "and column", spot)
                parkingLot[parkingRow][spot] = carId
                return parkingRow, spot


def leaveParking(carId):
    for i in range(0, len(parkingLot)):
        for spot in range(0, len(parkingLot[i])):
            if parkingLot[i][spot] == carId:
                parkingLot[i][spot] = 0
                print("\nSpot is available in row no.", i, "and column no.", spot)
                getToll()
                return
    print("Car not found! Please check your car id again ..")


def getToll():
    ask = int(input("Pay toll amount 500Rs? "))
    if ask == 500:
        print("Thank you!!")
    elif ask < 500:
        print("Sir, please pay balance amount", 500 - ask)
    elif ask > 500:
        print("Sir, your balance", ask - 500)
    else:
        print("Invalid amount")


row = int(input("Enter number of rows: "))
coln = int(input("Enter number of columns: "))
initParking(row, coln)
while True:
    ask = input(" Are you Enter / Leave / Stop ? ")
    if ask.lower() == "enter":
        carId = input("\nEnter your car id: ")
        result = assignParking(carId)
        print("Your spot is", result)
        
    elif ask.lower() == "leave":
        carId = input("Enter your car id: ")
        leaveParking(carId)
    elif ask.lower() == "stop":
        break   
    else:
        print("Invalid Answer sir!")
    view = input("\nWant to view the Parking Lot ? ")
    if view == "yes":
        print(f"Parking lot is \n{parkingLot}")