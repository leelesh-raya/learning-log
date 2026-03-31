spam='''o  what a thread of execution is, remember the Chapter 2 
 of flow control, when you imagined the execution of a program 
as placing your finger on a line of code in your program and moving to 
the next line or wherever it was sent by a flow control statement. A single
threaded program has only one finger. But a program has mul
tiple fingers. Each finger still moves to the next line of code as defined by 
the flow control , but the fingers can be at different places in the 
program, executing different lines of code at the same time.'''

def long(eggs):
    dix={}
    length=0
    for item in eggs.split():
        for char in '.,!?':
            item=item.replace(char, '')
        if len(item)>length:
            dix={len(item): [item]}
            length=len(item)
            
        elif len(item)==length  and item not in dix[len(item)]:  
            dix[len(item)].append(item)
            dix[len(item)].sort()
    for v in dix.values():
        if len(v)==1:
            return ''.join(v)
        else:
            return v

    

print(long(spam))



         