import json
p=['''After you import the json module, you can call loads() and pass it a 
string of JSON data. Note that JSON strings always use double quotes. It 
will return that data as a Python dictionary. Python dictionaries are not 
ordered, so the key-value pairs may appear in a different order when you 
print jsonDataAsPythonValue.''']
print(json.dumps(p))