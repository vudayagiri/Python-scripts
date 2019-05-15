loginfail = loginsuc = 0
keystone_file = open("keystone.common.wsgi","r")
keystone = keystone_file.readlines()
#keystone = "req-e34f17f4-4957-4117-a174-73fb8de19d29 - - - - -] Authorization failed."
lfail = "- - - - -] Authorization failed"
lsuccess = "-] Authorization failed"
ipfail1=[]
ipsuccess=[]
for i in keystone:

    if lfail in i:
        loginfail +=1
        ipfail1 = i.split()
        #ipfail = len(ipfail1)
        print("The following address had a login failure :", ipfail1[-1])

    elif lsuccess in i:
        loginsuc += 1
        ipsuccess = i.split()
        #ipsuc = len(ipsuccess)
        print("\n\nThe following address had a login success :", ipsuccess[-1])
print(f"\n\nThe number of login failures is : {loginfail} and number of success is : {loginsuc}")
