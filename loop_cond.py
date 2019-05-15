vow = con = 0
print("Please enter a string: ")
strng = input()

for i in strng:
    if i in ['a','e','i','o','u']:
        vow +=1
    else:
        con += 1
print(f"In the string - {strng}, there are {vow} vowels and {con} consonants")
