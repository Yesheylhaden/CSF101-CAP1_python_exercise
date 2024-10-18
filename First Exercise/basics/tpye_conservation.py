age = 19
age_str = str(age)
message  = "I am " + age_str + "years old."
print(message)

num_str = "42"
num_int = int(num_str)
print(num_int)

non_num_str = "hello"
try:
    non_num_str = int(non_num_str)
    print(non_num_str)
except ValueError as e:
    print(f"Error: {e}")


