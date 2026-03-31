spam=["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(words):
    sorter={}
    for item in words:
        group=''.join(sorted(item))
        sorter.setdefault(group,[])
        sorter[group].append(item)

    
    return list(sorter.values())
    
print(groupAnagrams(spam))
        



'''Corrections: 
   Changed    lst = []
              for v in sorter.values():
                lst.append(v)
              return lst
   To         
              return list(sorter.values())
'''