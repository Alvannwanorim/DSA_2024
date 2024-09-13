def combination(n: int, k:int):
    res = []
    def dfs(start,comb):
        print(start, "here")
        if len(comb) == k:
            res.append(comb.copy())
            return 
        for i in range(start, n+ 1):
            # add the current item to the combination 
            # e.g [1,2,1,3,1,4]
            comb.append(i)
            # run the recursion for i
            dfs(i + 1, comb)
            # remove the last item added
            comb.pop()
    dfs(1,[])
    return res

print(combination(4,2))