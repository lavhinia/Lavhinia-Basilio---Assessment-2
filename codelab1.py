#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:10:22 2024

@author: lavignejoicee
"""

import winsound
import definitions
import sqlite3
conn = sqlite3.connect("Item List.db")
#This is a comment:
"""Above this line, shows two connections to different files
        Definitions is the other part of this code, where you can find several functions that speeds
        up several processes.
        SQlite3('Item List.db') on the other hand, connects this file to my database which has the
        product_id, item, price, bundle, type, and amount of each product"""

shopping_cart = [] #This creates a list where the bought products will end up in. 
product_id = ("None")
check = False
current_price = 0.0
total_price = float(0)
money_check = False
current_money = 0.0
change_money = 0.0
item_check = False
continue_check = False
cur = conn.cursor()
qry = cur.execute("SELECT product_id FROM Item_Database")
res = qry.fetchall()
database_list = [x[0] for x in res]
#Above are variables that will be used later.
 
winsound.PlaySound('Lounge_Spiritfarer.wav', winsound.SND_LOOP + winsound.SND_ASYNC) #This adds the music in the background

input("Hello, welcome to tLavhinia's vending machine. This program was made by Lavhinia Joice C. Basilio, let us start. ")

#This is a comment:
"""The while loop below allows the program to loop until the user is satisfied with
their selections, it allows for multiple products to be selected from the vending machine."""

while check == False: #This restarts the loop when it reaches the end unless the user chooses to buy another product.
    product = {
            'amount' : 0,
            'item' : '',
            'price' : 0.0,
            'type' : '',
            'bundle_item' : 'None',
            }
    #This is the product's values that are impacted by the user's input.
    
    definitions.product_list() 
    #This is a comment:
    """
    This line of code gets a definitions called "product_list()" from the definitions file. 
    Which shows off the products, their price, and the amount left on the product.
    """
    
    product_id = input("Please input the product ID, you would want to buy: ")
    #This allows the user to select an item to add to their shopping cart.
    
    #This if conditions changes the product id to it's right id if the user made a mistake in their grammar
    if product_id == "c1": 
        product_id = "C1"

    elif product_id == "c2":
        product_id = "C2"

    elif product_id == "c3":
        product_id = "C3"

    elif product_id == "c4":
        product_id = "C4"

    elif product_id == "ch1" or product_id == "CH1":
        product_id = "Ch1"

    elif product_id == "ch2" or product_id == "CH2":
        product_id = "Ch2"

    elif product_id == "ch3" or product_id == "CH3":
        product_id = "Ch3"

    elif product_id == "p1":
        product_id = "P1"

    elif product_id == "p2":
        product_id = "P2"

    elif product_id == "p3":
        product_id = "P3"

    elif product_id == "d1":
        product_id = "D1"

    elif product_id == "d2":
        product_id = "D2"

    elif product_id == "d3":
        product_id = "D3"

    elif product_id == "sd1" or product_id == "Sd1":
        product_id = "SD2"

    elif product_id == "sd2" or product_id == "Sd2":
        product_id = "SD2"

    elif product_id == "sd3" or product_id == "Sd3":
        product_id = "SD3"

    elif product_id == "j1":
        product_id = "J1"

    elif product_id == "j2":
        product_id = "J2"

    elif product_id == "j3":
        product_id = "J3"
    
    elif product_id == "Cart" or product_id == "cart": #This allows the user to see what they have currently bought
        product_id == "Cart"
        print("")
        definitions.show_product(shopping_cart)
        input("...")
        continue
    elif product_id == "Exit" or product_id == "exit": #This allows the user to proceed to the next part if they have bought a product
        product_id == "Exit"
        if item_check == True:
            continue_check = False
            while continue_check == False: #This allows the user to buy another product or move on to the next step
                continue_answer = input('\nAre you sure you are finished? Please enter "Yes" or "No": ')
                if continue_answer == 'Yes' or continue_answer == 'yes' or continue_answer == 'YES' or continue_answer == 'y':
                    check = True
                    continue_check = True
                    break
                elif continue_answer == 'No' or continue_answer == 'no' or continue_answer == 'NO' or continue_answer == 'n':
                    continue_check = True
                else:
                    print("Sorry, our system did not recognize your answer please try again.\n")
        else:
            input("\nSorry, but you need to select an item first before leaving. ")
            continue
    
    if product_id in database_list: #This checks if the selected product still has a stock inside the database
        print("")
        cur = conn.cursor()
        qry = cur.execute("SELECT amount, item, price, type FROM Item_Database WHERE product_id=?", (product_id,))
        res = qry.fetchone()
        product['amount'] = res[0] #This changes the value of the dictionary named "product"

        if product['amount'] > 0:
            product['item'] = res[1]
            product['price'] = res[2]
            product['type'] = res[3]
            definitions.decrease_amount(product_id)
            print ("You added " + product['item'] + " to your cart, it cost " + str(product['price']) + " dhs and it is in the " + product['type'] + " category.")
        else:
            input("Sorry, but the item you selected ran out. Please choose again. ")
            print("")
            continue

    elif product_id == "Cart" or product_id == "Exit":
        continue

    else:
        input("Sorry, our system did not recognize your answer please try again. ")
        print("")
        continue

    if product['item'] == 'Doritos Nacho Cheese' or product['item'] == 'Sprite': #This checks if the product has a bundle or not. Along the rest
        if product['item'] == 'Doritos Nacho Cheese':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("SD2")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)
        elif product['item'] == 'Sprite':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("C1")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)

    elif product['item'] == 'Lays Classic' or product['item'] == 'Miranda':
        if product['item'] == 'Lays Classic':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("SD3")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)
        elif product['item'] == 'Miranda':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("C2")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)

    elif product['item'] == 'Lays French Cheese' or product['item'] == 'Coke':
        if product['item'] == 'Lays French Cheese':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("SD3")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)
        elif product['item'] == 'Coke':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("C3")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)

    elif product['item'] == 'Flaming Hot Cheetos' or  product['item'] == 'Mixed Berries Juice':
        if product['item'] == 'Flaming Hot Cheetos':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("J3")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)
        elif product['item'] == 'Mixed Berries Juice':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("C4")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)

    elif product['item'] == 'M&M' or  product['item'] == 'Orange Juice':
        if product['item'] == 'M&M':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("J2")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)
        elif product['item'] == 'Orange Juice':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("Ch1")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)

    elif product['item'] == 'Kitkat' or  product['item'] == 'Apple Juice':
        if product['item'] == 'Kitkat':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("J1")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)
        elif product['item'] == 'Apple Juice':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("Ch2")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)

    elif product['item'] == 'Chocolate Chip Cookie' or  product['item'] == 'Milk':
        if product['item'] == 'Chocolate Chip Cookie':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("D2")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)
        elif product['item'] == 'Milk':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("P1")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)

    elif product['item'] == 'Biscuit' or  product['item'] == 'Hot Coffee':
        if product['item'] == 'Biscuit':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("D2")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)
        elif product['item'] == 'Hot Coffee':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("D3")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)
    else:
        print ("There does not seem to be a bundle associated with your purchase")
    
    print("-----------------------------\n")
    
    remove_check = False
    while remove_check == False: #This allows user to remove the current product they have selected
        if product['type']  == "bundle":
            print(f"The item you selected is {product['item']} and {product['bundle_item']}.\n")
        else:
            print(f"The item you selected is {product['item']}.\n")
        remove = input('Are you sure this is your order? Please write "Yes" or "No": ')
        if remove == 'Yes'  or remove == 'yes' or remove == 'YES' or remove == 'y':
            remove_check = True
            remove == 'Yes'
        elif remove == "No" or remove == 'no' or remove == 'NO' or remove == 'n':
            remove_check = True
            remove == 'No'
        else:
            print("Sorry, our system did not recognize your answer please try again.\n")
    
    if remove == 'No':
        if product['type']  == "bundle":
            definitions.increase_amount(product_id) #This redo's the amount changes made previously
            product_id = previous_product_id
            definitions.increase_amount(product_id)
            continue
        else:
            definitions.increase_amount(product_id)
            continue
    elif remove == 'Yes':
        shopping_cart.append(product) #This adds the product details to the shopping_cart
        item_check = True
    
    print("\n-----------------------------")
    
    continue_check = False
    while continue_check == False: #This allows the user to buy another product or move on to the next step
        continue_answer = input('\nDo you want to continue your shopping? Please enter "Yes" or "No": ')
        if continue_answer == 'Yes' or continue_answer == 'yes' or continue_answer == 'YES' or continue_answer == 'y':
            continue_check = True
        elif continue_answer == 'No' or continue_answer == 'no' or continue_answer == 'NO' or continue_answer == 'n':
            check = True
            continue_check = True
        else:
            print("Sorry, our system did not recognize your answer please try again.\n")

for product in shopping_cart: #This gets the total price by checking each product's price
    current_price = (product['price'])
    total_price += current_price

input("\nProcessing order...\n")

print("Your total purchase is " + str(total_price) + " dhs\n")
definitions.show_product(shopping_cart)

while money_check == False: #This loops back until the right amount of coins is inserted
    if current_money >= total_price: #This checks if the amount of money inputted is higher than the total price
        change_money = current_money - total_price
        if change_money == 0: #This checks if the change is equal to zero
            print("\n~~ A sound is heard in the opening beneath ~~\n")
            print("Here are your products:")
            for product in shopping_cart: #This shows off your shopping cart again for the final time
                if product['type'] == "bundle":
                    print("\t" + product['item'] + " and " + product['bundle_item'])
                else:
                    print("\t" + product['item'])
            input("\nThank you for shopping with us.")
            money_check = True
        else:
            change_check = input(f'\nPlease enter "Yes" keep your change and "No" if you want to donate it to charity, it is {change_money} dhs: ')
            
            #This allows you to get back your leave over money if there is one
            
            if change_check == 'Yes': 
                print(f"\nHere is your change: {change_money} dhs")
                print("\n~~ A sound is heard in the opening beneath ~~\n")
                print("Here are your products:")
                for product in shopping_cart:
                    if product['type'] == "bundle":
                        print(f"\t{product['item']} and {product['bundle_item']}")
                    else:
                        print("\t" + product['item'])
                input("\nThank you for shopping with us.")
                money_check = True
            elif change_check == 'No':
                print("\n~~ A sound is heard in the opening beneath ~~\n")
                print("Here are your products:")
                for product in shopping_cart:
                    if product['type'] == "bundle":
                        print(f"\n{product['item']} and {product['bundle_item']}")
                    else:
                        print("\n" + product['item'])
                input("\nThank you for shopping with us.")
                money_check = True
            else:
                print("Sorry, our system did not recognize your answer please try again.\n")

    else: #This allows the user to add money to their balance
        print(f"\nYour current balance is: {current_money} dhs")
        print(f"Total price: {total_price} dhs")
        money = input("\nPlease input either 25 fils, 50 fils, 1 dhs, 5 dhs, 10 dhs, or 20 dhs into the machine to get your ordered products: ")
        if money == ("25 fils") or money == ("25 Fils") or money == ("0.25"):
            current_money += 0.25
        elif money == ("50 fils") or money == ("50 Fils") or money == ("0.50"):
            current_money += 0.50
        elif money == ("1 dhs") or money == ("1 Dhs") or money == ("1"):
            current_money += 1
        elif money == ("5 dhs") or money == ("5 Dhs") or money == ("5"):
            current_money += 5
        elif money == ("10 dhs") or money == ("10 Dhs") or money == ("10"):
            current_money += 10
        elif money == ("20 dhs") or money == ("20 Dhs") or money == ("20"):
            current_money += 20
        else:
            print("Sorry, our system did not recognize your answer please try again.\n")

winsound.PlaySound(None, winsound.SND_LOOP + winsound.SND_ASYNC) #This stops the music in the background