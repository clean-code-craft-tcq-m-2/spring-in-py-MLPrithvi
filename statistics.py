import math as m

def calculateStats(numbers):
  length = len(numbers)
  if length == 0:
    return None
  test = {"avg":avgVal, "min":minVal, "max":maxVal} 
  avgVal = sum(numbers) / length
  minVal = min(numbers)
  maxVal = max(numbers)
  return test
