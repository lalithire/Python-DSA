def selection_sort(array):
    for i in range (len(array)):
        min_index = i
        for j in range (i+1 , len(array)): #FIRST OF ALL 5 WILL COMPAIR WITH OTHER REMAINING 
                                           #ELEMENTS TILL LOOP ENDS ,THEN WE WILL GET NEW SORTED ARRAY 
                                           #LIKE [4,3,2,1,5] AND LIKEWISE IT WILL GET SORTED AND GIVE O/P [1, 2, 3, 4, 5]
            if array[j] < array[min_index] :
                min_index = j 
        array[i],array[min_index] = array[min_index],array[i]
    return array
array = [5,4,3,2,1]
print(selection_sort(array))

#EXPECTED OUTPUT 
#[1, 2, 3, 4, 5]