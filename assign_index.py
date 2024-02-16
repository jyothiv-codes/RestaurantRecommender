f=open("yelp-ratings-cleaned.csv","r")
write_file=open("yelp-ratings-cleaned-index.csv","w")
write_friends=open("yelp-user-cleaned-index.csv","w")
i=0
users={}
restaurants={}
user_id=0
restaurant_id=0
for line in f:
    if i!=0:
        line=line.split(",")
        u_id=line[0]
        r_id=line[1]
        if u_id not in users:
            users[u_id]=user_id
            user_id+=1
        if r_id not in restaurants:
            restaurants[r_id]=restaurant_id
            restaurant_id+=1
        to_write=line[0]+","+str(users[line[0]])+","+line[1]+","+str(restaurants[line[1]])+","+line[2]
        write_file.write(to_write)
        

    i+=1
i=0
g=open("yelp-user-cleaned-final-without-index.csv","r")
for line in g:
    if i!=0:
        line=line.split(",",1)
        user=line[0].strip()
        if user not in users:
            pass
        else:

            friends=line[1].replace("\"","")
            friends=friends.split(",")
            if "None" in friends:
                print("yes")
            if len(friends)>0:
                string=""
                for friend in friends:
                    if friend in users:
                        friend=friend.strip()
                        string+=str(users[friend])
                        string+=","
                if len(string)>0 and string[-1]==",":
                    string=string[:-1]
                final_string=str(users[user])+","+"\""+string+"\""
                write_friends.write(final_string)
                write_friends.write("\n")
            else:
                final_string=str(users[user])+",None"
                write_friends.write(final_string)
                write_friends.write("\n")

    i+=1


f.close()
write_file.close()
g.close()
write_friends.close()


