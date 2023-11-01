# -*- coding: utf-8 -*-
"""ctypesCPU.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dF-YC37cVLYo8FtQ_oaijoMudgxf5q7b
"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile sumArrayCPU.cpp
# #include <iostream>
# 
# extern "C" {
#   int sumArrays(int* arr1, int* arr2, int* result, int size) {
#       for (int i = 0; i < size; ++i) {
#           result[i] = arr1[i] + arr2[i];
#       }
#       return 0;
#   }
# }

!g++ -shared -fPIC -o sumArrayCPU.so sumArrayCPU.cpp

# Load the compiled C++ code
from ctypes import CDLL, c_int, POINTER

# Load the shared library
cpp_lib = CDLL('./sumArrayCPU.so')

# Define the types for the function
cpp_lib.sumArrays.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), c_int]
cpp_lib.sumArrays.restype = c_int

def sum_arrays(arr1, arr2):
    # Convert Python lists to C arrays
    arr1_c = (c_int * len(arr1))(*arr1)
    arr2_c = (c_int * len(arr2))(*arr2)

    # Prepare the result array
    result_c = (c_int * len(arr1))()

    # Call the C++ function
    cpp_lib.sumArrays(arr1_c, arr2_c, result_c, len(arr1))

    # Convert the result C array to a Python list
    result = list(result_c)

    return result

# Example usage
arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]

result = sum_arrays(arr1, arr2)
print(result)