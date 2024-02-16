u_r=open("yelp-ratings-cleaned.csv","r")
write_u_r=open("yelp-ratings-cleaned-index.csv","w")
write_u=open("yelp-user-cleaned-index.csv","w")
users={}
u=0
restaurants={}

#create new file with indexes of users and restaurants added
write_u_r.write("User,UserID,Restaurant,RestaurantID,Rating\n")
r=0
i=0
for line in u_r:
    if i!=0:
        data=line.split(",")
        if data[0] in users:
            pass
        else:
            users[data[0]]=u 
            u+=1
        if data[1] in restaurants:
            pass
        else:
            restaurants[data[1]]=r
            r+=1
        #to_write=data[0]+","+str(users[data[0]])+","+data[1]+str(users[data[1]])+","+data[2]
        to_write=data[0]+","+str(users[data[0]])+","+data[1]+","+str(restaurants[data[1]])+","+data[2]+"\n"
        write_u_r.write(to_write)
    i+=1
print(len(users))
print(len(restaurants))


#create a new file with indexes of users added from the yelp-user-cleaned.csv file
u_data=open("yelp-user-cleaned.csv","r")
write_u.write("User,Friends\n")
i=0
for line in u_data:
    if i!=0:
        data=line.split(",",1)

        if len(data)>1:
            friends=data[1]

            #remove the " which is the first and the last characters in the string
            friends=friends[1:]
            friends=friends[:-2]+friends[-1]

            #split the string and iterate through the friends list
            friends=friends.split(",")
            friends=friends[1:]
            friends=friends[:-1]
            if data[0] not in users:
                users[data[0]]=u
                u+=1
            else:
                pass
                #print("already present--",users[data[0]])
            if len(friends)>0:
                to_write=str(users[data[0]])+",\""
                for friend in friends:
                    if friend not in users:
                        users[friend]=u
                        u+=1
                    else:
                        pass
                    to_write+=str(users[friend])+","
                        #print("friend already present---",users[friend])
                to_write=to_write[:-1]
                to_write+="\"\n"
                
            else:
                to_write=str(users[data[0]])+",None\n"
            write_u.write(to_write)
        
        else:
            pass
        


    i+=1

print(len(users))





#close all the files 
u_r.close()
u_data.close()
write_u_r.close()
write_u.close()