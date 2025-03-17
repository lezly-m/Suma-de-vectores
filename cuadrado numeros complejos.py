# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 15:55:15 2025

@author: lezly
"""

from abc import ABC, abstractmethod

class IRecursiveMethods(ABC):
    @abstractmethod
    def sum_vectors(self, vector1, vector2):
        pass
    
class RecursiveMethods(IRecursiveMethods):
    def sum_vectors(self, vector1, vector2):
        if not vector1 or not vector2:
            return []
        return [vector1[0] + vector2[0]] + self.sum_vectors(vector1[1:], vector2[1:])

def get_vector_array(vector):
    strings_array = vector.split()
    return recursive_cast(strings_array)

def recursive_cast(arr):
    if not arr:
        return []
    return [int(arr[0])] + recursive_cast(arr[1:])

def recursive_data_request_and_process(recursive: IRecursiveMethods, data):
    if not data:
        return []
    dimensions = int(input("Ingrese la dimensión del vector (2 o 3): ").strip())
    if dimensions not in [2, 3]:
        print("Dimensión no válida")
        return recursive_data_request_and_process(recursive, data[1:])
    
    vector1 = get_vector_array(input("Ingrese el primer vector: ").strip())
    vector2 = get_vector_array(input("Ingrese el segundo vector: ").strip())
    
    if len(vector1) != dimensions or len(vector2) != dimensions:
        print("Los vectores deben tener la dimensión especificada.")
        return recursive_data_request_and_process(recursive, data[1:])
    
    return [recursive.sum_vectors(vector1, vector2)] + recursive_data_request_and_process(recursive, data[1:])

def recursive_print(result):
    if not result:
        return
    print(result[0])
    recursive_print(result[1:])

def main():
    number_of_tests = int(input("Ingrese el número de pruebas: ").strip())
    recursive_methods = RecursiveMethods()
    if 1 <= number_of_tests <= 100:
        data = [0] * number_of_tests
        result = recursive_data_request_and_process(recursive_methods, data)
        recursive_print(result)

if __name__ == "__main__":
    main()
