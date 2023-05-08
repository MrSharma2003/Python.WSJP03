seats = 100
normal = 50
vip = 25
premium = 25
nprice = 150
vipprice = 200
pprice = 250
combo_price = 500
vipcombo_price = 999
pcombo_price = 1499
while True:
    name = input("enter a name : ")
    total = 0
    
    print("""Available seats are 
     normal - 199 each 
     vip - 449 each
     premium - 549 each""")
    
    seats_type = input("enter your seats type :").lower()
    seats = int(input("how many seats to take :"))
    
    if seats_type == "normal":
        total += nprice*seats
        combo = input("do you want add to combo of price 500: ")
        if combo in ["yes","YES","yes"]:
            total += combo_price
        print("~" * 40)
        print("total amount ",total)
        print("~" * 40)
        break
    if seats_type == "vip":
        total += vipprice*seats
        combo = input("do you want add to vipcombo of price 999 : ")
        if combo in ["yes","YES","yes"]:
            total += vipcombo_price
        print("~" * 40)
        print("total amount ",total)
        print("~" * 40)
        break
    if seats_type == "premium":
        total += pprice*seats
        combo = input("do you want add to premium combo of price 1499 : ")
        if combo in ["yes","YES","yes"]:
            total += pcombo_price
        print("~" * 40)
        print("total amount ",total)
        print("~" * 40)
        break
    
            
