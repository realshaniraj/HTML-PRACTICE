### Description

This Python program finds the smallest element in a given array.
It initializes the first element as the minimum value and compares it with all other elements in the array.
If a smaller element is found, the minimum value is updated.
Finally, the program prints the smallest element in the array.

### Time Complexity

The time complexity of this program is O(n), where n is the number of elements in the array.

arr =[10,22,3,43,18]

min_element=arr[0]
for i in arr:
  if i < min_element:
    min_element=i


print("smallest element=",min_element)

