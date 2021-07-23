# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 09:44:07 2021

@author: foster-s
"""

import pandas as pd

beer_sales = pd.read_excel('eccentric beer sales.xlsx')

# Understand the shape of the original document
print(beer_sales.iloc[0:5, 0:16])
print(beer_sales.head())

# Hold the columns for Retail accounts, Address, City, and Item Names 
# Manipulate Date and Case Equivs sold for each day
beer_sales_mod = pd.melt(beer_sales,
                         id_vars=['Retail Accounts', 'Address', 'City',
                                  'Item Names'],
                         var_name='Day',
                         value_name='Case Equivs')

# Ensure this worked
print(beer_sales_mod.head())

# Export to new file. 
beer_sales_mod.to_excel('eccentric beer sales modified.xlsx')