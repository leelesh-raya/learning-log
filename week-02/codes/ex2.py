import re, urllib.request

url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
data = urllib.request.urlopen(url).read().decode("utf-8")

print(data[:3715])
data=data.split('\n')
pattern=r"(\d+.?\d?),(\d+.?\d?),(\d+.?\d?),(\d+.?\d?),(\w+)"
result={}

for item in data:
 match=re.search(pattern, item)
 if match:
   result.setdefault(match.group(5), {'count':0, 'total_ptl_length':0, 'total_size':0, 'max_sepal_length':0 })
   result[match.group(5)]['count']+=1
   result[match.group(5)]['total_ptl_length']+=float(match.group(3))
   result[match.group(5)]['total_size']+=float(match.group(1))+float(match.group(2))+float(match.group(3))+float(match.group(4))
   result[match.group(5)]['max_sepal_length']=max(result[match.group(5)]['max_sepal_length'], float(match.group(1)))

largest_size=0
largest_species=''
largest_slength=0
largest_sepal=''
avg_ptl_length=0
avg_size=0
for k,v in result.items():
  avg_size=round(result[k]['total_size']/result[k]['count'] , 1)
  avg_ptl_length=round(result[k]['total_ptl_length']/result[k]['count'] , 1)
  if largest_size < avg_size:
    largest_size= avg_size
    largest_species=k
  
  if largest_slength < v['max_sepal_length']:
    largest_slength=v['max_sepal_length']
    largest_sepal=k

  print(f"Average petal length of species {k}: ",avg_ptl_length )
  print(f"Total no. of samples in species {k}:", v['count'])

print(f"Species with largest size is {largest_species} with avg size({largest_size})")
print(f"Species with lengthiest sepal is {largest_sepal} with length({largest_slength})")