"""
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Name Checker
________________________________________________________________________

‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Author: Adrien Babet | GitHub: @babetcode | Email: adrienbabet1@gmail.com  
_______________________________________________________________________________
"""

import pandas as pd

local_names = pd.read_csv('mydata/stusorted.csv')
ssa_names = pd.read_csv('mydata/babyNamesUSYOB-full.csv')

unique_names = []
for name in local_names['first']:
    if name.capitalize() not in unique_names:
        unique_names.append(name.capitalize())

ulen = len(unique_names)

# n/ulen = x/250 --> x = 250n/ulen
not_in = []
for n, name in enumerate(unique_names):
    for i in range(int(250*n/ulen)):
        print('_', end='', flush=True)
    print('/', end='', flush=True)
    for i in range(int(250 - 250*n/ulen)):
        print('|', end='', flush=True)
    if name not in ssa_names['Name'].values:
        not_in.append(name)
    print('\r', end='')
print(f'these are unnacounted for: {not_in}')