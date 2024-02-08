import json
 
# Opening JSON file
with open('new_results/json_results/im1-text.json') as json_file:
    data = json.load(json_file)
 
    # Print the type of data variable
 
    # Print the data of dictionary
    for key, value in data.items():
        print(key, value)