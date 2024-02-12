import numpy as np
arry=np.array([[1,2,3,4],[1,2,3,4]])
print(arry)
arr_arange=np.arange(0,10,3)
print(arr_arange)


#a=([[1,2,3],[4,5]])
a1=arr_arange.reshape(2,2)
print(a1)

#multipication of array(dot product)
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
result=np.dot(arr1,arr2)
print("matrix multipication",result)


#array multipication 
matrix1=np.array([[1,2],[3,4]])
matrix2=np.array([[5,6],[7,8]])
result_matrix=np.dot(matrix1,matrix2)
print("matrix multipication\n",result_matrix)

#statical operations 
data=np.array([1,2,3,4,5,6])
mean_value=np.mean(data)
std_deviation=np.std(data)
print("mean is ",mean_value,"\nstandard deviation ",std_deviation)



#Random vaule Genaration 
random_number=np.random.rand(3,3) #(matrix order)
#random_int=np.random.randint(lower_bound,upper_bound,number_of_numbers)
random_int=np.random.randint(1,2,40)
print("random matrix \n",random_number,"\nrandom range ",random_int)
