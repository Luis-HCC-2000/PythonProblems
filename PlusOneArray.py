#Given an array of integers of any length, return an array that has 1 added to the value represented by the array.
#the array can't be empty
#only non-negative, single digit integers are allowed
#Return null (or your language's equivalent) for invalid inputs.
#Examples
#For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].
#[4, 3, 2, 5] would return [4, 3, 2, 6]

def up_array(arr):
    try:
        for index,item in enumerate(arr):
            if item>-1 and item<10:  arr[index]=str(item)
        arr=list(str((int("".join(arr)))+1))
        for index,number in enumerate(arr): arr[index]=int(number)
        return arr
    except:
        return
