# Returns optimal plan cost
def optimalPlanCost(n, m, N, S):
    Rn, Rs = [], [] # we use these lists to hold past costs in order to compare
    for i in range(n):
        if i == 0:
            Rn.append(N[i])
            Rs.append(S[i])
        else:
            j = i - 1
            minN = min(Rn[j], Rs[j] + m) #adds minimum value as path considering moving cost
            minS = min(Rs[j], Rn[j] + m) 
            Rn.append(N[i] + minN)
            Rs.append(S[i] + minS)
        print(Rs, Rn)
    return min(Rn[n - 1], Rs[n - 1]) # Returns the minimum cost in n months

def incorrectAnswer(n, m , N, S):
    R = 0
    currentN = True #added this flag to maintain moving cost in algorithm
    for i in range(n):
        if N[i] < S[i]:
            R += N[i]
            if not currentN:
                currentN = True
                R += m
        else:
            R += S[i]
            if currentN:
                currentN = False
                R += m
        
    return R

def main():
    N = [1, 50, 1, 1]
    S = [50, 1, 40, 50]
    n = len(N)
    W = 30
    print(optimalPlanCost(n, W, N, S))

    # Following algorithm is incorrect because it doesnt regards moving cost at all !!! 
    # It just adds it no matter what if other location is cheaper.
    print(incorrectAnswer(n, W, N, S))

main()