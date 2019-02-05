# Finds a possible trip with minimum total penalty score and prints each hotel accomadations along the way.
# Also optimumDistance can be set manually but defaulted to 200 as suggested in assignment.
def print_min_penalty_trip(hotels, optimumDistance = 200):
    A = hotels
    OPTIMUM_DISTANCE = optimumDistance
    X = 0
    totalPenalty = 0
    for i in range(len(A)):
        if X == A[len(A) - 1]:
            break
        closestHotel = A[i] - X
        possiblePenalty = closestHotel - OPTIMUM_DISTANCE
        appliedPenalty = possiblePenalty
        if (possiblePenalty == 0): # No Penalty Optimum distance, go for it
            X += closestHotel
        elif (possiblePenalty < 0): # Try to get closer to an hotel.
            for j in range(i, len(A)):
                nextClosestHotel = A[j] - X
                nextPossiblePenalty = nextClosestHotel - OPTIMUM_DISTANCE
                if (nextPossiblePenalty == 0):
                    X += nextClosestHotel
                    i = j
                    appliedPenalty = 0
                    break
                elif (nextPossiblePenalty > 0):
                    if (abs(nextPossiblePenalty) <= abs(possiblePenalty)):
                        X += nextClosestHotel
                        totalPenalty += abs(nextPossiblePenalty) ** 2
                        appliedPenalty = nextPossiblePenalty
                        i = j
                    else:
                        X += closestHotel
                        totalPenalty += abs(possiblePenalty) ** 2
                        appliedPenalty = possiblePenalty
                        i = j - 1
                    break
                else: 
                    closestHotel = nextClosestHotel
                    possiblePenalty = nextPossiblePenalty
        else: # There is not any closer hotel.
            X += closestHotel
            totalPenalty += abs(possiblePenalty) ** 2

        print("Total miles =", X, "----", "Total penalty =", totalPenalty, "----", "Applied Penalty Score is Square of", appliedPenalty)

# Main driver function
def main():
    A = [190, 220, 410, 580, 640, 770, 950, 1100, 1350]
    print_min_penalty_trip(A)

main()