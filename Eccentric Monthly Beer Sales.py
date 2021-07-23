# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 13:38:46 2021

@author: foster-s
"""

# Eccentric Rolling Month Report is the file to be used
# goal is to melt the dataframe and output a new file before replacing the 
# Month names with just month and year
import pandas as pd
import re
from AdvancedAnalytics.ReplaceImputeEncode import DT, ReplaceImputeEncode

beer_sales = pd.read_excel('Eccentric Rolling Month report.xlsx')

# Understand the shape of the original document
print(beer_sales.iloc[0:5, 0:16])
print(beer_sales.head())

beer_sales_mod = pd.melt(beer_sales,
                         id_vars=['Retail Accounts', 'Address', 'City',
                                  'Item Names'],
                         var_name='Month',
                         value_name='Case Equivs')

# Ensure this worked
print(beer_sales_mod.head())
     

#beer_sales_mod['Month'] = beer_sales_mod['Month'].str.replace('1 Month 2/1/2020 thru 2/29/2020','Feburary 2020', regex=True)
#beer_sales_mod['Month'] = beer_sales_mod['Month'].str.replace('1 Month 1/1/2021 thru 1/31/2021','January 2021', regex=True)
#beer_sales_mod['Month'] = beer_sales_mod['Month'].str.replace('1 Month 10/1/2020 thru 10/31/2020','October 2020', regex=True)
#beer_sales_mod['Month'] = beer_sales_mod['Month'].str.replace('1 Month 11/1/2020 thru 11/30/2020','November 2020', regex=True)
#beer_sales_mod['Month'] = beer_sales_mod['Month'].str.replace('1 Month 12/1/2020 thru 12/31/2020','December 2020', regex=True)
#beer_sales_mod['Month'] = beer_sales_mod['Month'].str.replace('1 Month 2/1/2021 thru 2/28/2021','February 2021', regex=True)
#beer_sales_mod['Month'] = beer_sales_mod['Month'].str.replace('1 Month 3/1/2020 thru 3/31/2020','March 2020', regex=True)
#beer_sales_mod['Month'] = beer_sales_mod['Month'].str.replace('1 Month 3/1/2021 thru 3/31/2021','March 2021', regex=True)
#beer_sales_mod['Month'] = beer_sales_mod['Month'].str.replace('1 Month 4/1/2020 thru 4/30/2020','April 2020', regex=True)
#beer_sales_mod['Month'] = beer_sales_mod['Month'].str.replace('1 Month 4/1/2021 thru 4/30/2021','April 2021', regex=True)
#beer_sales_mod['Month'] = beer_sales_mod['Month'].str.replace('1 Month 5/1/2020 thru 5/31/2020','May 2020', regex=True)
#beer_sales_mod['Month'] = beer_sales_mod['Month'].str.replace('1 Month 5/1/2021 thru 5/31/2021','May 2021', regex=True)
#beer_sales_mod['Month'] = beer_sales_mod['Month'].str.replace('1 Month 6/1/2020 thru 6/30/2020','June 2020', regex=True)
#beer_sales_mod['Month'] = beer_sales_mod['Month'].str.replace('1 Month 6/1/2021 thru 6/30/2021','June 2021', regex=True)
#beer_sales_mod['Month'] = beer_sales_mod['Month'].str.replace('1 Month 7/1/2020 thru 7/31/2020','July 2020', regex=True)
#beer_sales_mod['Month'] = beer_sales_mod['Month'].str.replace('1 Month 7/1/2021 thru 7/8/2021','July 2021', regex=True)
#beer_sales_mod['Month'] = beer_sales_mod['Month'].str.replace('1 Month 8/1/2020 thru 8/31/2020','August 2020', regex=True)
#beer_sales_mod['Month'] = beer_sales_mod['Month'].str.replace('1 Month 9/1/2020 thru 9/30/2020','September 2020', regex=True)


beer_sales_mod.to_excel('eccentric rolling month report beer sales modified.xlsx')