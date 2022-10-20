import unittest
import statistics
import math as m

class StatsTest(unittest.TestCase):
  def test_report_min_max_avg(self):
    computedStats = statistics.calculateStats([1, 2, 3, 4])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 2.5, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 4, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1, delta=epsilon)

  def test_avg_is_nan_for_empty_input(self):
    computedStats = statistics.calculateStats([])
    self.assertTrue(m.isnan(computedStats[0])
    self.assertTrue(m.isnan(computedStats[1])
    self.assertTrue(m.isnan(computedStats[2])
    # All fields of computedStats (average, max, min) must be
    # nan (not-a-number), as defined in the math package
    # Design the assert here.
    # Use nan and isnan in https://docs.python.org/3/library/math.html

  def test_raise_alerts_when_max_above_threshold(self):
    emailAlert = EmailAlert()
    ledAlert = LEDAlert()
    maxThreshold = 10.5
    statsAlerter = StatsAlerter(maxThreshold, [emailAlert, ledAlert])
    statsAlerter.checkAndAlert([22.6, 12.5, 3.7])
    self.assertTrue(emailAlert.emailSent)
    self.assertTrue(ledAlert.ledGlows)

if __name__ == "__main__":
  unittest.main()
