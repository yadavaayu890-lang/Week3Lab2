userRegistered= True
shoppingCart= 0
if userRegistered == True and shoppingCart >=1:
    print("Please proceed to payment!")

elif userRegistered == 'guest' and shoppingCart==0:
    print("Please proceed to payment!")

else:
    print("You cant proceed to payment!")

    