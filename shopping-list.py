product_name = []
product_is_bought = []
product_price = []


for i in range(100):
    answer = input( "add , display, edit, remove, search,details, buy, exit :  ")
    answer = answer.lower()
 
 #Add   
    if answer == "add" :
        name = input (" product name : ").lower()
        if name not in product_name :
            product_name.append(name)
            product_is_bought.append(False)
            product_price.append(None)
            print("Added! ")
        else:
            print("Already Exist!")
            
#Display      
    elif answer == "display" :
        for i , name in enumerate(product_name):
            print(i+1, name, product_is_bought[i],product_price[i])
    
 #Edit   
    elif answer == "edit" :
        name = input(" name for edit: ").lower()
        if name in product_name:
            new_name = input(" New Name: ").lower()
            if new_name not in product_name : 
                i = product_name.index(name)
                product_name[i] = new_name
                print("Edited!")
            else:
                print("Already Exit! ")
        else:
            print("Not found! ")

    
 #Remove   
    elif answer == "remove" :
        name = input("name for remove :").lower()
        if name in product_name:
            i = product_name.index(name)
            product_name.pop(i)
            product_is_bought.pop(i)
            product_price.pop(i)
            print("Removed!")
            
        else:
            print("Not found!") 
 
 #Search           
    elif answer == "search" :
        name = input("name for search :").lower()
        if name in product_name:
            i = product_name.index(name)
            status = product_is_bought[i]
            price = product_price[i]
            print(f"status: {status}, Price: {price}")
        else:
            print("Not Found!")
    
#Buy
    elif answer == "buy" :
        name = input("name for Buy :").lower()
        if name in product_name:
            price = float(input(f"price of {name}: "))
            i = product_name.index(name)
            product_is_bought[i] = True
            product_price[i] = price
            print("Done!")
            
        else:
            print("Not Found!")

    elif answer == "details":
        numbers = len(product_name)
        not_purchased = product_is_bought.count(False)
        #purchased = product_is_bought.count(True)
        purchased = sum(product_is_bought)
        
        print (f" number of product : {numbers}")
        print (f" number of not purchased : {not_purchased}")
        print (f" number of purchased : {purchased}")
        
        price = []
        for p in product_price:
            if p:
                price.append(p)
        sum_price = sum(price)
        print (f" Total Price : {sum_price}")
        


#Exit   
    elif answer == "exit" :
        break
    
    else:
        print(f"{answer}: command not found! ")

