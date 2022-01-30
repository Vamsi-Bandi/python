tableData=[['apples', 'oranges', 'cherries', 'banana'],['Alice', 'Bob', 'Carol', 'David'],['dogs', 'cats', 'moose', 'goose']]

def printTables(tableData):
    colWidths = [0] * len(tableData)

    x, y, z = 0, 0, 0
    for c in tableData:
        for w in tableData[0]:
            if len(w) > x:
                x = len(w)
        colWidths[0] = x
        for w in tableData[1]:
            if len(w) > y:
                y = len(w)
        colWidths[1] = y
        for w in tableData[2]:
            if len(w) > z:
                z = len(w)
        colWidths[2] = z
    
        colWidths.sort()
    
        maxWidth = colWidths[-1]

    column = []
    c = 0
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            column.append(tableData[j][i])

    for i in tableData[0]:
        for j in tableData:
            print(column[c].rjust(maxWidth), end='')
            c += 1
        print()

printTables(tableData)
