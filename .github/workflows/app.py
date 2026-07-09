info = {"name": "John", "age": 30, "city": "New York"}
print(info["name"])  # Output: John
info["age"] = 31  # Update age  


 # Update city and add country

info.update({"city": "hyderabad", "country": "india"})  # Update city and add country
info["email"] = "s@g.com"  # Add email  
print(info)  # Output: {'name': 'John', 'age': 31, 'city': 'Los Angeles', 'country': 'USA', 'email': '
print(dir(info))  # Output: List of all attributes and methods of the dictionary
for key in info.keys():
    print(key)  # Output: name, age, city, country, email
for value in info.values():
    print(value)  # Output: John, 31, Los Angeles, USA, s@g.com 
    for key, value in info.items(): 
        print(f"{key}: {value}")  # Output: name: John, age: 31, city: Los Angeles, country: USA, email:

        for key, value in info.items():
            print(f"{key}: {value}")  # Output: ('name', 'John'), ('age', 31), ('city', 'Los Angeles'), ('country', 'USA'), ('email', 's@g.com')
