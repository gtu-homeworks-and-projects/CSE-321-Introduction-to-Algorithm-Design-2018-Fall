jobList = [
    {
        "ID": 1,
        "Weight": 8,
        "Time": 4
    },
    {
        "ID": 2,
        "Weight": 1,
        "Time": 2
    },
    {
        "ID": 3,
        "Weight": 3,
        "Time": 6
    },
    {
        "ID": 4,
        "Weight": 15,
        "Time": 1
    },
    {
        "ID": 5,
        "Weight": 7,
        "Time": 7
    },
    {
        "ID": 6,
        "Weight": 3,
        "Time": 14
    }
]

def min_weight_completion_order(jobs):
    return mergeSortJobs(jobs)


def merge(left, right): 
    if not len(left) or not len(right): 
        return left or right 
  
    result = [] 
    i, j = 0, 0
    while (len(result) < len(left) + len(right)): 
        if left[i]["Time"] / left[i]["Weight"] < right[j]["Time"] / right[j]["Weight"]: 
            result.append(left[i]) 
            i+= 1
        else: 
            result.append(right[j]) 
            j+= 1
        if i == len(left) or j == len(right): 
            result.extend(left[i:] or right[j:]) 
            break

    return result 
  
def mergeSortJobs(list): 
    if len(list) < 2: 
        return list
  
    middle = int(len(list)/2)
    left = mergeSortJobs(list[:middle]) 
    right = mergeSortJobs(list[middle:]) 
  
    return merge(left, right) 

def main():
    print("Jobs:")
    for job in jobList:
        print(job)
    print("Minimum weighted sum of completion time order: ")
    for job in min_weight_completion_order(jobList):
        print(job)

main()