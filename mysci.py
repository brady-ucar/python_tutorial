# Column names and column indices to read
columns = {'data':0, 'time':1, 'tempout':2, 'windspeed':7}

#data types for each column only if non-string
types = {'tempout':float, 'windspeed':float}

#intitialize data variable:
data = {} 
for column in columns:
    data[column]= []

# Read the data file
filename = "data/wxobs20170821.txt"

with open(filename, 'r') as datafile:

    #read the header:
    for _ in range(3): 
        headerline = datafile.readline()

    #read and parse the rest of the file:
    for line in datafile:
        split_line= line.split()
        for column in columns:
            i = columns[column]
            t = types.get(column, str) 
            value = t(split_line[i])
            data[column].append(value)

#debug
print(data['tempout'])


