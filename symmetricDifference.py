def symmetric_difference(differList):
    noMatchList = []
    for lister in differList: 
        for item in lister: 
            if item in noMatchList:
                noMatchList.remove(item)
            else:
                noMatchList.append(item)

    return(noMatchList)

differList = [[1, 2, 5], [2, 3, 5], [3, 4, 5]]
print(symmetric_difference(differList))