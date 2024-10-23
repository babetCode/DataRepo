"""
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Name Checker
________________________________________________________________________

‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Author: Adrien Babet | GitHub: @babetcode | Email: adrienbabet1@gmail.com  
_______________________________________________________________________________
"""

local_data_fp = 'C:/Users/goper/Files/vsCode/DataRepo/mydata/stuscraped.csv'
ssa_data_fp = 'C:/Users/goper/Files/vsCode/DataRepo/mydata/babyNamesUSYOB-full.csv'
strange_names_fp = 'C:/Users/goper/Files/vsCode/DataRepo/mydata/StrangeNames.txt'

import pandas as pd
import time

local_data = pd.read_csv(local_data_fp)
ssa_data = pd.read_csv(ssa_data_fp)
ssa_data = ssa_data.sort_values(by=['Name', 'YearOfBirth'])
ssa_data = ssa_data.reset_index(drop=True)

local_unique_names = []
for name in local_data['first']:
    if name.capitalize() not in local_unique_names:
        local_unique_names.append(name.capitalize())
lun_len = len(local_unique_names)

with open(strange_names_fp, 'r') as file:
    content = file.read()
strange_names = content.strip().replace("'", "").split(", ")

len_ssa = len(ssa_data.index)
print(f'the data is {len_ssa} items long')
all_ssa_names = ['placeholder']
f_score = []
m_score = []
start_time = time.time()
for index, row in ssa_data.iterrows():
    if row['Name'] == all_ssa_names[-1]:
        if row['Sex'] == 'F':
            f_score[-1] += int(row['Number'])
            # print(
            #     f'old name, {row["Number"]} was added to Fscore.\
            #     It is now {f_score[-1]}')
        elif row['Sex'] == 'M':
            m_score[-1] += int(row['Number'])
            # print(
            #     f'old name, {row["Number"]} was added to Mscore.\
            #     It is now {m_score[-1]}')
        else:
            print(f'error at row {index} when name was in')
    else:
        all_ssa_names.append(row['Name'])
        if row['Sex'] == 'F':
            f_score.append(int(row['Number']))
            m_score.append(0)
            # print(
            #     f'new name, {row["Number"]} was appended to Fscore.\
            #     It is now {f_score[-1]}')
        elif row['Sex'] == 'M':
            f_score.append(0)
            m_score.append(int(row['Number']))
            # print(
            #     f'new name, {row["Number"]} was appended to Mscore.\
            #     It is now {m_score[-1]}')
        else:
            print(f'error at row {index} when name NOT in')
    
    if index != 0 and index%300000==0:
        percent_done = round((index/len_ssa)*100, 2)
        runtime = time.time() - start_time
        minutes = int(runtime//60)
        seconds = int(runtime%60)
        totaltime = runtime * (len_ssa/index)
        tminutes = int(totaltime//60)
        tseconds = int(totaltime%60)
        ltime = totaltime-runtime
        lminutes = int(ltime//60)
        lseconds = int(ltime%60)
        print(f'runtime {minutes}m {seconds}s     est time left {lminutes}m {lseconds}s     est total time {tminutes}m {tseconds}s     we are {percent_done}% done') #end='', flush=True
    # print('\r', end='')
print(f'the first ssaname is {all_ssa_names[0]}')
all_ssa_names.pop(0)

score = []
for f, m in zip(f_score, m_score):
    score.append(f/(f+m))

scores_df = pd.DataFrame({'Name': all_ssa_names, 'Score': score})

scores_df.to_csv('C:/Users/goper/Files/vsCode/DataRepo/mydata/namescores.csv', index=False)

print(scores_df)