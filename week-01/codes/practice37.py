spam=[
 "Alice 10 login",
 "Alice 20 logout",
 "Bob 20 login"
]
def concurrent(logs):
    order={}
    series=[]
    status={}
    for item in logs:
        name, time, state=item.split()
        time=int(time)
        if time not in series:
            series.append(time)
        
        if time not in order:
            order[time]={}
        
        if name not in status:
            status[name]='logout'
        
        order[time][name]=state

    series.sort()
    active=0
    max_users=0
    for item in series:
        for user in order[item]:
            if order[item][user]=='login' and status[user]!=order[item][user]:
                active+=1
                status[user]='login'
            elif order[item][user]=='logout' and order[item][user]!=status[user]:
                active-=1
                status[user]='logout'
            
        max_users=max(max_users, active)

    return max_users

print(concurrent(spam))




#Correction: I WROTE THIS PROGRAMME ENTIRELY..