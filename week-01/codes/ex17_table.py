tableData = [['apples', 'oranges', 'cherries', 'banana'], 
             ['Alice', 'Bob', 'Carol', 'David'], 
             ['dogs', 'cats', 'moose', 'goose']]
import pyperclip
def prTable(table):
    colwidths=[0]*len(table)
    for i in range(len(table)):
        for j in range(len(table[i])):
            if len(table[i][j]) > colwidths[i]:
                colwidths[i]=len(table[i][j])

    text=''
    for i in range(len(table)+1):
        for j in range(len(table)):
            text+=table[j][i].rjust(colwidths[j])+' '
        text+='\n'
    return text
print(prTable(tableData))

pyperclip.copy(prTable(tableData))


    
    
