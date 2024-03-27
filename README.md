# Input-Output
We have a list input and output list
``` python
data_input = [
    1, 0, 1,
    0, 1, 0,
    1, 1, 1
]

data_output = [] # in here, we don't write anything
```

Each step, we check if the element ***data_input*** is 1, then we write to ***data_output***, decrementing by one if the element is 0 then we write in exactly the same way to ***data_output***, but only increase by one
``` python
for i in range(0, len(data_input)):
    if data_input[i] == 1:
        data_output.append(data_input[i] - 1)
    if data_input[i] == 0:
        data_output.append(data_input[i] + 1)
```
And we show ***data_input*** and ***data_output***
``` Python
print(f"Input:  {data_input}\nOutput: {data_output}")
```
Result:
```
Input:  [1, 0, 1, 0, 1, 0, 1, 1, 1]
Output: [0, 1, 0, 1, 0, 1, 0, 0, 0]
```

We can also reduce the number of elements in ***data_input***, and the number of elements in ***data_output*** will be exactly the same as in ***data_input***, using ```len()```
