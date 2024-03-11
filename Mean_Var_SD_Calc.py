#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(numbers).reshape(3, 3)

    result = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
    }

    return result

def main():
    input_numbers = []
    for i in range(9):
        while True:
            try:
                num = float(input(f"Enter number {i + 1}: "))
                input_numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    try:
        result = calculate(input_numbers)
        print(result)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

