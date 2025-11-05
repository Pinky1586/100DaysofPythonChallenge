# Functions with input

#def greet_with_name(name, location):
#    print(f"Hello {name}")
#    print(f"How do you do {name}?")


name_in = input(f"What is your name?: ")
location_in = input(f"What is your location?: ")

def greet_with_name(name, location):
    print(f"Hello, {name_in}.")
    print(f"What is it like in {location_in}?")

#greet_with_name(name_in, location_in)

greet_with_name(name=name_in, location=location_in)