data_input = [
    1, 0, 1,
    0, 1, 0,
    1, 1, 1
]
data_output = []
for i in range(0, len(data_input)):
    if data_input[i] == 1:
        data_output.append(data_input[i] - 1)
    if data_input[i] == 0:
        data_output.append(data_input[i] + 1)
print(f"Input:  {data_input}\nOutput: {data_output}")