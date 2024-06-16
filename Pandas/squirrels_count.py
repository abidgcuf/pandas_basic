import pandas

data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
# get all gray squirrels 
#gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
#white_squirrels_count = len(data[data["Primary Fur Color"] == "White"])

print(gray_squirrels_count)
print(Cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict = {

    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count":[gray_squirrels_count,Cinnamon_squirrels_count,black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("Squirrels Count.csv")