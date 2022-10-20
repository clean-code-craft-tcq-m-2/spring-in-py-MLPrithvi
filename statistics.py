import math as m

def calculateStats(numbers):
  if type(numbers) == list:
    length = len(numbers)
    for x in range(length):
      if type(numbers[x]) == str:
        Nan_Output = m.isnan(x)
        return Nan_Output
      elif (type(numbers[x]) == float) or (type(numbers[x]) == int) and (length != 0):
        avgVal = sum(numbers) / length
        maxVal = max(numbers)
        minVal = min(numbers)
        test = {"avg":avgVal, "min":minVal, "max":maxVal}
        return test

class LEDAlert():
  ledGlows = False

class EmailAlert():
  emailSent = False
  
class StatsAlerter():
  def __init__(self,maxThreshold, Output):
      self.maxThreshold = maxThreshold
      self.Output = Output
      
  def checkAndAlert(self,numbers):
    computedStats = calculateStats(numbers)
    if computedStats["max"] > self.maxThreshold:
      self.Output[0].emailSent = True
      self.Output[1].ledGlows = True
