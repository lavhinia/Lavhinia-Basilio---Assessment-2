#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:11:00 2024

@author: lavignejoicee
"""

import sqlite3
con = sqlite3.connect("Item List.db")

def update_data(amount, product_id):
    qry = "update Item_Database set amount=? where product_id=?;"
    con.execute(qry,(amount, product_id))
    con.commit()


input("Hello! would you like to restock the vending machine? If so, continue on. ")

product_id='C1'
amount=5
update_data(amount, product_id)

product_id='C2'
amount=5
update_data(amount, product_id)

product_id='C3'
amount=5
update_data(amount, product_id)

product_id='C4'
amount=5
update_data(amount, product_id)

product_id='Ch1'
amount=4
update_data(amount, product_id)

product_id='Ch2'
amount=3
update_data(amount, product_id)

product_id='Ch3'
amount=3
update_data(amount, product_id)

product_id='P1'
amount=3
update_data(amount, product_id)

product_id='P2'
amount=3
update_data(amount, product_id)

product_id='P3'
amount=3
update_data(amount, product_id)

product_id='D1'
amount=6
update_data(amount, product_id)

product_id='D2'
amount=5
update_data(amount, product_id)

product_id='D3'
amount=4
update_data(amount, product_id)

product_id='SD1'
amount=3
update_data(amount, product_id)

product_id='SD2'
amount=3
update_data(amount, product_id)

product_id='SD3'
amount=3
update_data(amount, product_id)

product_id='J1'
amount=3
update_data(amount, product_id)

product_id='J2'
amount=3
update_data(amount, product_id)

product_id='J3'
amount=3
update_data(amount, product_id)

print("\nProcess complete.")