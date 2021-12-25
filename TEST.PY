
#num = int(input("Enter any integer no:"))
#if num > 0:
#   print("The number is Positive")
#    print(num,"The squere of number is :", num * num)
#EXE : 5
"""distance_km = 564.5
distance_ml = distance_km * 0.621371
print(distance_ml) """

'''language = "Python"
print("1.", language == "python")
age = 18
print("2.", age >= 18)
print("3.", age > 18)
print("4.", age >= 18 and language == "Java") '''

"""score = float(input("Enter your score:  "))

if score > 0:
    print(" The score is Positive")

elif score < 0:
    print("The Score is negative")
else:
    print("The score is Zero")
"""
# WHILE LOOP
"""number = int(input("Enter a Number: "))

count = 10
while count >= 1:
    product = number * count
    print(number, "x", count, "=", product)
    count = count - 1
"""

# ------- FOR LOOP ---------
'''tex = ["PYTHON", "c#", "JAVA"]
for language in tex:
    print(language)

number = int(input("Enter a Number: "))

for count in range(1,11):
    product = number * count
    print(number, "x", count, "=", product)

total = 0
for number in range(1, 101):
    total = total + number
print(total)
'''
#tex = ["PYTHON", "Swift", "c#", "JAVA","C", "c++"]
#for Langs in tex:
    if Langs == "Swift" or Langs == "c++":
       continue
    print(Langs)

def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = int(filesize / 4096)
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size
    return block_size * (full_block + 1)

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192   