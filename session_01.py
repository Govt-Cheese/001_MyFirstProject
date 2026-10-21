print("Hello, Python student")
print("Glad to see you learning Python!!!")
print("We are not all snakes.  Ssssssssss....")

# practice number output
part_length_mm = 125.0
print("Part length (mm):%3.2f" % part_length_mm)
print(f"Part length (mm): {part_length_mm:.2f}")

# unit conversion
length_in = 80
length_mm = length_in * 25.4
print(f"{length_in:3.2f} inches = {length_mm:.2f} mm")

print("test123")

# user-input
user_length_inches = float(input("Enter length in inches: "))
user_length_mm = user_length_inches * 25.4
print(f"{user_length_inches:3.2f} inches = {user_length_mm:.2f} mm")

# maximum length check
max_length_mm = 1000
critical_length_mm = 2000

if user_length_mm > critical_length_mm:
    print("Critical: length exceeds 2000 mm.")
elif user_length_mm > max_length_mm:
    print("Warning: length exceeds 1000 mm.")
else:
    print("Length is within the 1000 mm limit.")

print("test234")

# input lengths (as a batch)
sample_lengths_inches = [10.0, 40.0, 80.0]

for sample_length_inches in sample_lengths_inches:
    sample_length_mm = sample_length_inches * 25.4
    print(f"{sample_length_inches:.2f} inches = {sample_length_mm:.2f} mm")

print("test34")
max_length_mm = 1000
critical_length_mm = 2000

for sample_length_inches in sample_lengths_inches:
    sample_length_mm = sample_length_inches * 25.4

    if sample_length_mm > critical_length_mm:
        print(f"{sample_length_inches:.2f} inches = {sample_length_mm:.2f} mm -> CRITICAL")
    elif sample_length_mm > max_length_mm:
        print(f"{sample_length_inches:.2f} inches = {sample_length_mm:.2f} mm -> WARNING")
    else:
        print(f"{sample_length_inches:.2f} inches = {sample_length_mm:.2f} mm -> OK")