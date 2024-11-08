def gridSearch(G, P):
    # Write your code here
    g_rows = len(G)
    g_cols = len(G[0])
    p_rows = len(P)
    p_cols = len(P[0])
   
    
    for i in range(g_rows - p_rows +1):
        for  j in range(g_cols - p_cols + 1):
            match_found = True
            for k in range(p_rows):
                
                if G[i + k][j: j + p_cols] !=P[k]:
                    
                    match_found = False
                    break
            if match_found:
                return "YES"
    return "NO"