dict = {
    "min" : 0000000,
    "max": 0
}

starter_list = [100, 20, 57, 267, 1]

for x in starter_list:
    if(x>dict["max"]):
        dict["max"] = x
        print(str(dict["max"]) + " is the greatest number righ now")
    if(x<dict["min"]):
        dict["min"] = x
        print(str(dict["min"]) + " is the smallest number righ now")

print("Max: " + str(dict["max"]))
print("Min: " + str(dict["min"]))