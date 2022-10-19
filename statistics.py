import math as m

def calculateStats(numbers):
  length = len(numbers)
  avgVal = sum(numbers) / length
  minVal = min(numbers)
  maxVal = max(numbers)
  return avgVal, minVal, maxVal
