import math as m

def calculateStats(numbers):
  length = len(numbers)
  if length == 0:
    return m.isnan(numbers)
  avgVal = sum(numbers) / length
  minVal = min(numbers)
  maxVal = max(numbers)
  test = {"avg":avgVal, "min":minVal, "max":maxVal}
  return test
