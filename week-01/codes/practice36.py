spam=[
 "Alice 10 start",
 "Alice 20 pause",
 "Bob 25 start",
 "Bob 40 pause"
]


def activity(log):
    output={}
    for item in log:
        name, time, state=item.split()
        time=int(time)
        if name not in output:
            output[name]={'state':'', 'time':0, 'total_time':0, 'sessions':0}

        if state=='pause' and output[name]['state']=='start':
            output[name]['total_time']+=time - output[name]['time']
            output[name]['sessions']+=1


        elif state=='start' and output[name]['state']=='start' :
            continue
        
        output[name]['state']=state
        output[name]['time']=time
    
    for k in output:
        output[k]={'total_time':output[k]['total_time'],'sessions':output[k]['sessions']}


    return output


print(activity(spam))