
currunt_bal=200
e_wallet=5000


def fun(currunt_bal,e_wallet):
    global to_wid
    print("You dont enough blance to play the game.\nThe minimum balance to play the game is 1000.\nYou can withdraw the money fron e-wallet")
        
    qs=(input("Do you Want to Widraw the money from your e-wallet?\nEnter 'yes' to widraw the money and type anything to no = "))
        
    if qs=="yes" or qs=="Yes":
        to_wid=eval(input("Your E-Wallet balance = 5000\nHow much money you want withdraw = "))
        if to_wid>e_wallet or to_wid<0:
            print("You have entered wrong amount please try again")
        elif e_wallet==0:
            print("Sorry! You dont have money in E-Wallet")
                
        elif to_wid>1 and to_wid<5000:
            currunt_bal=currunt_bal+to_wid
            e_wallet=e_wallet-to_wid
            print("you have withdrawel {} Rupees and your currunt balce is {} and E-Waleet Balance is = {} ".format(to_wid,currunt_bal,e_wallet))
    else:
        print("Sorry! You need to widraw the money.You dont have enough balance to play game")
    return currunt_bal,e_wallet






j=0

while True:
        
    if currunt_bal<1000:
        currunt_bal,e_wallet=fun(currunt_bal,e_wallet)
        
    elif currunt_bal>=1000:
        print("WOW!............Now You can Play the Game\nYour Currunt Balance is = ",currunt_bal)
        break
    
    j=j+1