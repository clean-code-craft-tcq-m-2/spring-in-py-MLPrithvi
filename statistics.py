import math as m

def calculateStats(numbers):
  length = len(numbers)
  if length == 0:
    a = m.isnan(sum(numbers) / length)
    b = m.isnan(min(numbers))
    c = m.isnan(max(numbers))
    test2 = {"avg":a, "min":b, "max":c}
    return test2
  avgVal = sum(numbers) / length
  minVal = min(numbers)
  maxVal = max(numbers)
  test1 = {"avg":avgVal, "min":minVal, "max":maxVal}
  return test1
