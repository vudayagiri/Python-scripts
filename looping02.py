dnsfile = open("dnsservers.txt")
dnslist = dnsfile.readlines()
for svr in dnslist:
    print(svr,end="")
dnsfile.close()
