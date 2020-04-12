menuList = []


def showBill():
    text1 = "My Food"
    print(text1.center(30,"-"))
    totalPrice = 0
    for food in range(len(menuList)):
        print(menuList[food])
        totalPrice += int(menuList[food][1])
    print("Total = ", totalPrice)
while True:
    menuName = input("Please Enter Your Menu: ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price: ")
        menuList.append([menuName, menuPrice])

print(menuList)
showBill()

#edit
