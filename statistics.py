import math as m

def calculateStats(numbers):
  if type(numbers) == list:
    length = len(numbers)
    for x in range(length):
      if (type(numbers[x]) == float) or (type(numbers[x]) == int) and (length != 0):
        avgVal = sum(numbers) / length
        maxVal = max(numbers)
        minVal = min(numbers)
        test = {"avg":avgVal, "min":minVal, "max":maxVal}
        return test
