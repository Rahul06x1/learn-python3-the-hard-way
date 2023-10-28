name = 'Zed A. Shaw'
my_age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}")
print(f"He's {height} inches tall.")
print(f"He's {height*2.54} centimeters tall.")
print(f"He's got {weight} pounds heavy.")
print(f"He's got {weight*0.453592} kilograms heavy.")
print(f"Actually that's too heavy.")
print(f"He's got {eyes} eyes and and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + height + weight
print(f"If I add {my_age}, {height}, and {weight} I get {total}.")