# 1 -> adds nums from 2 pos | puts sum in 3rd pos
# 2 -> multiplies nums from 2 pos | puts product in 3rd pos
# 99 -> halt

stuff = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 9, 1, 19, 1, 9, 19, 23, 1, 23, 5, 27, 2, 27, 10, 31, 1, 6, 31, 35, 1, 6, 35, 39, 2, 9, 39, 43, 1, 6, 43, 47, 1, 47, 5, 51, 1, 51, 13, 55, 1, 55, 13, 59, 1, 59, 5, 63, 2, 63, 6, 67, 1, 5, 67, 71, 1, 71, 13, 75, 1, 10, 75, 79, 2, 79, 6, 83, 2, 9, 83, 87, 1, 5, 87,91, 1, 91, 5, 95, 2, 9, 95, 99, 1, 6, 99, 103, 1, 9, 103, 107,2, 9, 107, 111, 1, 111, 6, 115, 2, 9, 115, 119, 1, 119, 6, 123, 1, 123, 9, 127, 2, 127, 13, 131, 1, 131, 9, 135, 1, 10, 135, 139, 2, 139, 10, 143, 1, 143, 5, 147, 2, 147, 6, 151, 1, 151, 5, 155, 1, 2, 155, 159, 1, 6, 159, 0, 99, 2, 0, 14, 0]

global buff
buff = stuff


def part_1(noun, verb) -> int:
    stuff = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 9, 1, 19, 1, 9, 19, 23, 1, 23, 5, 27, 2, 27, 10, 31, 1, 6, 31, 35, 1, 6, 35, 39, 2, 9, 39, 43, 1, 6, 43, 47, 1, 47, 5, 51, 1, 51, 13, 55, 1, 55, 13, 59, 1, 59, 5, 63, 2, 63, 6, 67, 1, 5, 67, 71, 1, 71, 13, 75, 1, 10, 75, 79, 2, 79, 6, 83, 2, 9, 83, 87, 1, 5, 87,91, 1, 91, 5, 95, 2, 9, 95, 99, 1, 6, 99, 103, 1, 9, 103, 107,2, 9, 107, 111, 1, 111, 6, 115, 2, 9, 115, 119, 1, 119, 6, 123, 1, 123, 9, 127, 2, 127, 13, 131, 1, 131, 9, 135, 1, 10, 135, 139, 2, 139, 10, 143, 1, 143, 5, 147, 2, 147, 6, 151, 1, 151, 5, 155, 1, 2, 155, 159, 1, 6, 159, 0, 99, 2, 0, 14, 0]

    stuff[1] = noun
    stuff[2] = verb

    # buff = stuff

    i = 0
    while True:
        if stuff[i] == 99:
            break
        elif stuff[i] == 1:
            index_1 = stuff[i + 1]
            index_2 = stuff[i + 2]
            index_3 = stuff[i + 3]

            temp_sum = stuff[index_1] + stuff[index_2]
            stuff[index_3] = temp_sum

            i += 4
            continue
        elif stuff[i] == 2:
            index_1 = stuff[i + 1]
            index_2 = stuff[i + 2]
            index_3 = stuff[i + 3]

            temp_product = stuff[index_1] * stuff[index_2]
            stuff[index_3] = temp_product

            i += 4
            continue
        
    return stuff[0]


noun = 0
verb = 0

to_equal = 19690720
first = stuff[0]

for k in range(100):
    noun = k
    for j in range(100):
        verb = j
   
        first = part_1(noun, verb)
        if first == to_equal:
            print(noun, verb, first)
            print(100 * noun + verb)
        else:
            pass
            # print(first)
            



# print(buff)
print(stuff[0])
