f=open("yelp-user-cleaned.csv","r")
w=open("yelp-user-cleaned-final.csv","w")
for line in f:
    if "None" not in line and "user_id,friends" not in line:
        w.write(line)
f.close()
w.close()