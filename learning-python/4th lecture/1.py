dict = {
    "name" : "Aditya",
    "subjects" : {
        "maths" : 69,
        "sst" : 91,
        "english" : 84,
        "computer" : 97,
        "hindi" : 91,
        "science" : 94,
    }
}

print(dict)

# Some dictionary methods are given below: 
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("name"))

dict.update({"surname":"Singh"})
