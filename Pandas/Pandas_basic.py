

import pandas

data = pandas.read_csv("weather-data.csv")
#print(data)
#print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
# data_list = data['temp'].to_list()
# print(data_list)

# avg= data['temp'].mean()
# max_value= data['temp'].max()
# min_value= data['temp'].min()

# print(avg)

# print(max_value)
# print(min_value)

# #get data in column

# print(data['condition'])
# # or same as

# print(data.condition)

#get data in row

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]

# print(monday.condition)

# monday_trmp = int(monday.temp)

# print(f"the Farinhiegt is {monday_trmp * 9/5 + 32}")

# creating data frame from scratch

student_dict = {
    "students": ["Adam","Ali","Anna"],
    "Scores": [70,90,90]
}
data= pandas.DataFrame(student_dict)
print(data)
#data.to_csv("new_data.csv")