''' Dictionary + Logic
Write a function that takes a list of student dictionaries and returns the name of the top scorer. 
If there's a tie, return both names in a list.'''


students = [
    {'name': 'Alice', 'score': 88},
    {'name': 'Bob', 'score': 9},
    {'name': 'Carol', 'score': 9}
]


def finder(lst):
    topper=[]
    value=lst[0]['score']

    for item in lst:
        if item['score']>value:
            topper=[item['name']]
            value = item['score']
        elif item['score']==value:
            topper.append(item['name'])

    if len(topper)==1:
        return topper[0]
    else:
        return topper
          


print(finder(students))
