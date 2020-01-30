# Basketball: You have a basketball hoop and someone says that you can play one of two games.
# Game 1: You get one shot to make the hoop.
# Game 2: You get three shots and you have to make two of three shots.
# If p is the probability of making a particular shot, for which values of p should you pick one game or the other?
#
# Choose to try to shoot one of one or two of three given a shooting accuracy.

def basketball(accuracy):
  if accuracy < 0.5:
    return "single shot"
  else:
    return "three shots"

import unittest

class Test(unittest.TestCase):
  def test_basketball(self):
    accuracy = 0
    while accuracy <= 1:
      if accuracy >= accuracy ** 3 + 3 * accuracy ** 2 * (1 - accuracy):
        self.assertEqual(basketball(accuracy), "single shot")
      else:
        self.assertEqual(basketball(accuracy), "three shots")
      accuracy += 0.01

if __name__ == "__main__":
  unittest.main()

