#input 2 names and reveal which name has higher amount of consonants than other

name1 = input("write name 1: ")
name2 = input("write name 2: ")

amount_of_consonants_in_name1 = 0
amount_of_consonants_in_name2 = 0

for char in name1:
    if char not in "aeiou":
        amount_of_consonants_in_name1 +=1

for char in name2:
    if char not in "aeiou":
        amount_of_consonants_in_name2 +=1

if amount_of_consonants_in_name1 > amount_of_consonants_in_name2:
    print("first is higher and amount of consonants are {}".format(amount_of_consonants_in_name1))
elif amount_of_consonants_in_name2 > amount_of_consonants_in_name1:
    print("second is higher and amount of consonants are {}".format(amount_of_consonants_in_name2))
else:
    print("they have the same amount of consonants")