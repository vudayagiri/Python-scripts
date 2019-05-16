import random

thursday = []
for x in range(10000):
    thursday.append(random.randint(1,250))
#print (thursday)

def sort_channels(channels):
    basic_pkg = []
    Standard_pkg = []
    Premium_pkg = []
    PremiumHD_pkg = []
    Extras = []
    basic = std = Prem = PremHD = Ex = 0
    highest = {"basic1":1,"std1":1,"Prem1":1,"PremHD1":1,"Ex1":1}

    for ch in channels:
        if (ch >=1 and ch <=20):
            basic_pkg.append(ch)
            basic += 1
        elif (ch>=21 and ch <= 50):
            Standard_pkg.append(ch)
            std += 1
        elif (ch >= 51 and ch <=100):
            Premium_pkg.append(ch)
            Prem +=1
        elif (ch >=101 and ch <=200):
            PremiumHD_pkg.append(ch)
            PremHD += 1
        else:
            Extras.append(ch)
            Ex += 1
    highest.update({"basic1": basic, "std1": std, "Prem1": Prem, "PremHD1": PremHD, "Ex1": Ex})
    print(highest)
    high = max(highest, key=highest.get)
    #high_key = [k for k, v in highest.items() if v == high]
    print(f"The following are the list of each pkgs:\n Basic pkg : {basic_pkg}\n Standard Pkg : {Standard_pkg} \n Premium Pkg : {Premium_pkg} \n Premium HD pkg : {PremiumHD_pkg} \n Extras pkg : {Extras} \n")
    print(f"The pkg with the highest number of channels is : {high}")

sort_channels(thursday)

