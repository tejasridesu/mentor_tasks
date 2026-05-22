#To fetch the index of 1st occurence of 1 in an sorted array of 0's and 1's
#Using Binary Search to reduce complexity.

def first_occurence_of_one(arr):
    low=0
    high= len(arr)-1
    answer= -1

    while low<= high:
        mid= (low+high)//2

        if arr[mid]==1:
            answer= mid
            high= mid-1 #to search left side

        else:
            low= mid+1  #to search right side


    return answer

#sorted array
arr= [0,0,0,0,0,0,0,1,1,1]
result_idx= first_occurence_of_one(arr)
print("First occurence of 1 is at index: ",result_idx)

    
