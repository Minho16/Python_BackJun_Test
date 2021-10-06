freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

cart = {}
purse = 1000

# inventory morning
department_store = {}

for department in (freelancers, antiques, pet_shop) : department_store.update(department)
print('Morning inventory of stores', sorted(department_store.items()))


def buy_item(dict_name, item_name,): 
    if item_name in dict_name.keys():
        amount = int(input("Let me know the quantity of the items you want to buy: "))
        dict_name.update({item_name: int(dict_name[item_name])-amount})
        cart.update({item_name: int(amount)})
        print("The item " + item_name + " with quantity: " + str(amount) + " has been added in the cart. Now your money in purse is: " + str(purse - amount))
        print("The remaining quantity of the item " + item_name + "is: " + str(dict_name[item_name]))
        # inventory after purchasing the item
        department_store_after = {**freelancers, **antiques, **pet_shop}
        print('Evening inventory of stores', sorted(department_store_after.items()))
    else: 
        print("The requested item does not exist, please check it again")   

item_name = input("Let me know which item you want to buy or write 'exit' if you just want to leave: ").lower() 

if item_name in ["brian", "black knight", "biccus diccus", "grim reaper", "minstrel"]: 
    dict_name = freelancers
    buy_item(dict_name, item_name)

elif item_name in ["french castle", "wooden grail", "scythe", "catapult", "german joke"]: 
    dict_name = antiques
    buy_item(dict_name, item_name)

elif item_name in ["blue parrot", "white rabbit", "newt"]:
    dict_name = pet_shop
    buy_item(dict_name, item_name)

elif item_name in ["exit"]:
    print("Thank you for visiting the store")
    exit()
    
else:  
    print("Please check again the item name")   
    exit()