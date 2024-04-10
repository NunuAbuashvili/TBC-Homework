# დაწერეთ ფუნქცია, რომელსაც გადაეცემა ორი დალაგებული სია და დააბრუნებს ახალ სიას, რომელშიც იქნება ელემენტები ორივე სიიდან დალაგებული მიმდევრობით. Main ფუნქციიდან გატესტეთ თქვენ მიერ შექმნილი ფუნქცია სხვადასხვა ინფუთისთვის. არ გამოიყენოთ ფუნქციები sort და sorted. შეეცადეთ, რომ თქვენ შერწყათ გადმოცემული ორი სია ისე, რომ დალაგება არ დაირღვეს.

def merge_sorted_arrays(arr1: list, arr2: list) -> list:
    # This function takes two sorted arrays as parameters, where arr1 is merged into arr2 in a way that the resultant array is also sorted. 
    
    # Initialize sorted_array with arr2
    sorted_array = arr2
    
    # If arr2 is empty, return arr1 since it's already sorted
    if len(arr2) == 0:
        return arr1
    
    # Iterate through each element in arr1 
    for number in arr1:
        # Iterate through each element in sorted_array to find the correct position where to insert the number
        for i in range(len(sorted_array)):
            # If number is less than the current element in sorted_array, insert it at that position and break out of the loop
            if number < sorted_array[i]:
                sorted_array.insert(i, number)
                break
            # If number is greater than the last element in arr2, append it to the end of sorted_array and break out of the loop
            if number > arr2[-1]:
                sorted_array.append(number)
                break

    return sorted_array

def main():
    # Test data 1 (Non-consecutive elements in the merged array)
    arr1 = [0, 4, 7, 9]
    arr2 = [1, 3, 10]
    print("Test data 1:")
    print(merge_sorted_arrays(arr1, arr2))
    
    # Test data 2 (Negative elements)
    arr3 = [-1, 3, 5, 7] 
    arr4 = [-2, 4, 6, 8]
    print("Test data 2:")
    print(merge_sorted_arrays(arr3, arr4))
    
    # Test data 3 (Empty array)
    arr5 = [1, 2, 3]
    arr6 = []
    print("Test data 3:")
    print(merge_sorted_arrays(arr5, arr6))
    
    # Test data 4 (Arrays with overlapping elements)
    arr7 = [1, 2, 3, 5]
    arr8 = [3, 4, 5, 6, 7]
    print("Test data 4:")
    print(merge_sorted_arrays(arr7, arr8))

if __name__ == "__main__":
    main()
