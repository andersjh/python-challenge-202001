# Reading poll data

import csv


# In[2]:


candidates = {}
total_votes = 0


csvpath = "houston_election_data.csv"
with open(csvpath, newline='', encoding='utf-8') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

#   Read each row of data after the header
    for row in csvreader:
        cur_candidate = row[0]
        total_votes += 1
        if cur_candidate not in candidates:
            candidates[cur_candidate] = 0
        # always cast vote because every candidate is in candidates
        candidates[cur_candidate] += 1
            
print( '-' * 28)
print('total_votes', total_votes)
# print('candidate\n', candidates)
print( '-' * 28)

# In[3]:


for key, value in candidates.items():
    print(f"{key}: percentage: {round(value/ total_votes * 100, 2)}% votes: {value}")


# In[4]:


max1 = 0
max2 = 0
candidate1 = ""
candidate2 = ""


# In[5]:


# let's fine top candidate
for key,value in candidates.items():
    if value > max1:
        max1 = value
        candidate1 = key

print('top candidate:', max1, candidate1)    

# lets find number 2
for key,value in candidates.items():
    if value > max2 and key != candidate1:
        max2 = value
        candidate2 = key 

print('second candidate:', max2, candidate2)

