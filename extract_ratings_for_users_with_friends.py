read_rating_again=open("yelp-ratings-cleaned-index.csv","r")
read_user_index_again=open("yelp-user-cleaned-index.csv","r")
graph_write=open("yelp-final-ratings-cleaned.csv","w")
users_with_ratings={}
for lines in read_rating_again:
    line=lines.split(",")
    if line[1] not in users_with_ratings:
        user=line[1]
        users_with_ratings[user]=lines

i=0
for lines in read_user_index_again:
    line=lines.split(",")
    if str(line[1])!="\"\"":
        if line[0] in users_with_ratings:
            data_write=users_with_ratings[line[0]]
            graph_write.write(data_write)
    i+=1
    if i==20:
        break
        
users_write=open("yelp-final-users-cleaned.csv","w")
for lines in read_user_index_again:
    if ",\"\"" not in lines:
        users_write.write(lines)

read_rating_again.close()
read_user_index_again.close()
graph_write.close()
users_write.close()