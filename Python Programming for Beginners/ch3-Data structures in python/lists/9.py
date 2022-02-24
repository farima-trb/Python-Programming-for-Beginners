num_players=int(input())
num_games=[]
count=0

num_games.extend(input())

for i in range(0,len(num_games)):
    if num_games[i]=='2' or num_games[i]=='1' or num_games[i]=='0' :
        count+=1
    
print(int(count/3))