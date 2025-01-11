import pandas as pd
from datetime import datetime
import pprint

#load the data
file_path = 'powercut_report.txt'
with open(file_path, 'r') as file:
    #this will create an array called lines and make each line as an element of lines
    lines = file.readlines()

# print(lines)

#parse data into a structured format
data = []
for line in lines: 
    if "Battery" in line:
        #convert line into an array called parts and separate it if ' - ' exists in line 
        parts = line.split(' - ')
        if len(parts) == 2:
            timestamp, status = parts
        else: 
            timestamp, status = None, parts[0]
            
        data.append({
            #strip: remove spaces, tabs and newline characters
            "timestamp" : timestamp.strip() if timestamp else None,
            "status" : status.strip()
        })
        
# pprint.pprint(data)

df = pd.DataFrame(data)

#parse the timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

df['plugged_status'] = df['status'].apply(lambda x: "Plugged In" if "Plugged In" in x else "Not Plugged In")
print(df)   

