# import numpy library
import numpy
arr = numpy.array([1, 5, 4, 8, 3, 7])

# finding the maximum and minimum element in the array
max_element = numpy.max(arr)
min_element = numpy.min(arr)

# printing the result
print('maximum element in the array is: ',max_element)
print('minimum element in the array is: ',min_element)

#cumulative Sum
list=[10,20,30,40,50]
new_list=[]
j=0
for i in range(0,len(list)):
    j+=list[i]
new_list.append(j)

print(new_list)