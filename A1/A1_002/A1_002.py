def แลกเงิน(am_money):
    coin_10 = 10
    coin_5 = 5
    coin_2 = 2
    coin_1 = 1

    num_coin_10 = 0
    num_coin_5 = 0
    num_coin_2 = 0
    num_coin_1 = 0
    
    if am_money >= coin_10:
        num_coin_10 = am_money // coin_10
        am_money %= coin_10

    if am_money >= coin_5:
        num_coin_5 = am_money // coin_5
        am_money %= coin_5

    if am_money >= coin_2:
        num_coin_2 = am_money // coin_2
        am_money %= coin_2

    if am_money >= coin_1:
        num_coin_1 = am_money // coin_1
        am_money %= coin_1
        
    print(f"เหรียญ 10 บาท :  {num_coin_10} เหรียญ")
    
    print(f"เหรียญ 5 บาท :  {num_coin_5} เหรียญ")
    
    print(f"เหรียญ 2 บาท :  {num_coin_2} เหรียญ")
    
    print(f"เหรียญ 1 บาท :  {num_coin_1} เหรียญ")
    
am_money = int(input("จำนวนเงินที่ต้องการแลกเหรียญ : "))
แลกเงิน(am_money)