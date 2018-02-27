
import os
import csv
import datetime

#Reading in CSV file
Py1= os.path.join("employee_data1.csv")

with open(Py1, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Skip the first row of the csv
    next(csv_reader, None)
    ##naming all empty lists i will be using
    Emp_id=[]
    name=[]
    DOB=[]
    New_DOB=[]
    SSN=[]
    New_SSN=[]
    state=[]
    New_state=[]
    split_first=[]
    split_last=[]
    final=[]
    actual=[]
    
     # Loop through rows
    for row in csv_reader:
        #print(row)
        Emp_id.append(row[0])
        name.append(row[1])
        DOB.append(row[2])
        SSN.append(row[3])
        state.append(row[4])

    
    ## a. splitting name column
    for i in name:
        x=i.split(" ")
        split_first.append(x[0])
        split_last.append(x[1])
    #print(split_last)

    ## b. change DOB column     
    for k in DOB:
        d = datetime.datetime.strptime(k, '%Y-%m-%d')
        #print(datetime.date.strftime(d, "%m/%d/%Y"))
        New_DOB.append(datetime.date.strftime(d, "%m/%d/%Y"))
    
        
    ## c. hidding first 5 values of SSN
        #print(SSN)
        for h in SSN:
            y=h.replace(h[:3],"***")
            z=y.replace(y[4:6],"***")
            New_SSN.append(z)

    ## d. state written as 2 letter abreviation
        us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    }

    for g in state:
        n= us_state_abbrev[g]
        New_state.append(n)
    
    

 ## appending all the individuals i made with edit and putting it in a new list called actual          

    final.append(Emp_id)
    final.append(split_first)
    final.append(split_last)
    final.append(New_DOB)
    final.append(New_SSN)
    final.append(New_state)
    #print(final)
    for j in range(len(Emp_id)):
        #print(j)
        fin=[item[j] for item in final]
        actual.append(fin)
        
        
 ## exporting
# Set variable for output file
output_file = os.path.join("Pyboss_clean.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB",
                     "SSN","State"])

    writer.writerows(actual)

    
    
    
        
