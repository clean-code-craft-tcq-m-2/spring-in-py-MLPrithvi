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

def StatsAlerter(maxThreshold, [emailAlert, ledAlert]):
  computedStats = statistics.calculateStats([22.6, 12.5, 3.7])
      if computedStats["max"] > maxThreshold:
        emailAlert.emailSent = True
        ledAlert.ledGlows = True
  return (emailAlert, ledAlert)
    
def LEDAlert():
  return ledGlows = False

def EmailAlert():
  return emailSent = False
