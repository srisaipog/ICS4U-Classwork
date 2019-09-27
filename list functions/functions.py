from typing import List

#using the python method
def insert_at_python(original: List, value: int, i: int) -> List:
    return original[:i] + [value] + original[i:]

#using the java method
def insert_at_java(original: List, value: int, i: int) -> List:
    new_list = [0] * (len(original) + 1)
    for index in range(i):
        new_list[index] = (original[index])
    
    new_list[index+1] = value

    for index in range(index+2, len(new_list)):
        new_list[index] = original[index-1]
    
    return new_list

def insert(original: List, value: int) -> List:
    for i,num in enumerate(original):
        if original[i] > value:
            break
        else:
            i += 1
    return insert_at_java(original, value, i)

def remove_at_python(original: List, i: int) -> List:
    return original[:i] + original[i+1:]  