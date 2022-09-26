
Name = "Davit"
Surname = "Bobokhidze"
Age = 24
Origin = "Tbilisidan"
Self = "Me var"
Occupation = "programirebis studenti Goal oriented academy-shi"
Selfage = "wlis"
Teacher = "Nika Keshelava"
full_name = "dato bobokhidze"
Height = 181

profession = "   programmer   "
#if function
knows_programming = True
if knows_programming:
    print("hell yea")  #tab = indentacia

if "D" in Name:
    print("bobo")

if "K" not in Name:
    print("Bobokhidze")


#format - capitalize - upper - lower
print("chemi saxelia {} da chemi asakia {}" .format(Name,Age))

print("chemi maswavlebelia {} da me var {}" .format(Teacher,Occupation))

print("My height is {} and my Surname is {}" .format(Height,Surname))

print(Name.capitalize())
print(Name.upper())
print(Name.lower())


 #str list
print(Name[0])
print(full_name[9])
print(full_name[2:9])
print(full_name[2:]) 
print(full_name[:6]) 
print(full_name[::2]) #ყოველი მეორე
print(full_name[-1])

#lenght
print(len(Name))
print(len(Teacher))

#replace - strip

print(profession.strip())

print(profession.replace("p","l"))