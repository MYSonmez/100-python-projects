# with open("project-024/notes/weather_data.csv") as csvfile:
#     data = csvfile.readlines()
#     print(data)
##########################################################################

# import csv
    
# with open("project-024/notes/weather_data.csv") as csvfile:
#     data = csv.reader(csvfile)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)

##########################################################################

# import pandas as pd
# data = pd.read_csv("project-024/notes/weather_data.csv")
# print(data)

# # Get data in column
# print(data.condition) 
# print(data["condition"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# min_temp = data["temp"].min()
# print(min_temp)

# max_temp = data["temp"].max()
# print(max_temp)

# average_temp =data["temp"].mean()
# print(average_temp)

# # Get data in row
# get_row = data[data.day == "Tuesday"] 
# print(get_row)

# max_temp_row = data[data.temp == data.temp.max()]
# print(max_temp_row)

# wednesday = data[data.day == "Wednesday"]
# wednesday_temp = wednesday.temp
# wednesday_temp_list = wednesday_temp.to_list()
# print(wednesday_temp_list[0])

# # Create a dataframe from scratch
# data_dictionary = {
#     "names": ["adar","rojda","şirin","habo"],
#     "ages": [23,25,22,17]
# }

# import pandas as pd

# df = pd.DataFrame(data_dictionary, index = [0,1,2,3])
# print(df)

# new_csv = df.to_csv("new_csv_file.csv")
# new_html = df.to_html("new_html_file.html")

#####################################################################################

# import pandas as pd

# data = pd.read_csv("project-024/notes/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_squrriels = data[data["Primary Fur Color"] == "Gray"]
# cinnamon_squrriels = data[data["Primary Fur Color"] == "Cinnamon"]
# black_squrriels = data[data["Primary Fur Color"] == "Black"]

# gray_squrriels_count = len(gray_squrriels)
# cinnamon_squrriels_count = len(cinnamon_squrriels)
# black_squrriels_count = len(black_squrriels)

# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_squrriels_count, cinnamon_squrriels_count, black_squrriels_count]
# }

# df = pd.DataFrame(data_dict, index=[0,1,2])
# squrriels_count_csv = df.to_csv("squrriels_count.csv")