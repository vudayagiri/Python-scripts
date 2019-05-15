import csv

i=0
f = open("csv_users.csv","r")
for r in csv.reader(f):
    print(r)
    i+=1
    filename = "admin.rc%d"%(i,)
    rcfile = open(filename,"w")
    print("export OS_AUTH_URL=" + r[0],file=rcfile)
    print("export OS_IDENTITY_API_VERSION=3",file=rcfile)
    print("export OS_PROJECT_NAME=" + r[1],file=rcfile)
    print("export OS_PROJECT_DOMAIN_NAME=" + r[2],file=rcfile)
    print("export OS_USERNAME=" + r[3],file=rcfile)
    print("export OS_USER_DOMAIN_NAME=" + r[4],file=rcfile)
    print("export OS_PASSWORD=" + r[5], file=rcfile)
    rcfile.close()


