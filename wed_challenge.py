words = ["Cat","Dog","Beaver","Quasimodo"]

vow=0
con=0

for row in words:
    v=c=0
    for r in row:
        if r in 'aeiou':
            v +=1
        else:
            c+=1
    print(f"The number of vowels in {row} is {v} and consonants is {c}")
    vow+=v
    con+=c
print(f"\n\nThe number of vowels in {words} is {vow} and consonants is {con}")

