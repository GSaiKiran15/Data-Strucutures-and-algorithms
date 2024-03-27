import random

input_array_1 = random.sample(range(1,1000), 100)
input_array_2 = random.sample(range(1,1000), 100)
output_array = []
first_pointer, second_pointer = 0, 0
while first_pointer < len(input_array_1) and second_pointer < len(input_array_2):
    if input_array_1[first_pointer] < input_array_2[second_pointer]:
        output_array.append(input_array_1[first_pointer])
        first_pointer += 1
    else:
        output_array.append(input_array_2[second_pointer])
        second_pointer += 1
print(output_array)