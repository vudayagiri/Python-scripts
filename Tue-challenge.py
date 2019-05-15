pkg = []
def pk1(pk):
    if pk > 200:
        print("The Best overall package is Extras pkg")
    elif (pk >= 101 and pk <= 200):
        print("The Best overall package is Premium pkg")
    elif (pk >= 51 and pk <= 100):
        print("The Best overall package is Premium pkg")
    elif (pk >= 21 and pk <= 50):
        print("The Best overall package is Std pkg")
    else:
        print("The Best overall package is Basic pkg")

while True:
    print("What Channel Do you want?")
    pkg1 = int(input())

    if (pkg1 <=20):
        print("You should purchase our Basic Package")
    elif (pkg1 <= 50):
        print("You should purchase our Standard Package")
    elif (pkg1 <= 100):
        print("You should purchase our Premium Package")
    elif (pkg1 >= 101 and pkg1 <= 200 ):
        print("You should purchase our Premium HD Package")
    elif (pkg1 >=201 and pkg1 <= 600):
        print("You should purchase our Extras Package")
    else:
        print("You have not chosen a channel")
    decision = input("Would you like to price a different channel? Type 'no' to quit")

    pkg.append(pkg1)
    p1 = max(pkg)


    if (decision.lower() == 'no'):
        pk1(p1)
        print("You have chosen the following Channels:",pkg)
        break

print ("Thanks for considering us")

