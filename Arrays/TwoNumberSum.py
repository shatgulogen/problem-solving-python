'''
Sample input
  array = [3, 5, -4, 8, 11, 1, -1, 6]
  targetSum = 10

Sample output
[-1, 11]// the numbers could be in reverse order
'''

# Solution No.1 while loop solution
# O(nlog(n)) time | O(1) space
# O(nlog(n)) because of the sorting algorithm
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array)-1
    while left < right:
          currentSum = array[left] + array[right]
          if currentSum == targetSum:
              return [array[left], array[right]]
          elif currentSum < targetSum:
              left += 1
          elif currentSum > targetSum:
              right -= 1
    return []



# Solution No.2 Hash Table
# O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []

# Solution No.3 for loop solution
# O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):
    for i in range(len(array)- 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []

'''
Test cases
{
  "array": [3, 5, -4, 8, 11, 1, -1, 6],
  "targetSum": 10
}
{
  "array": [4, 6],
  "targetSum": 10
}
{
  "array": [4, 6, 1],
  "targetSum": 5
}
{
  "array": [4, 6, 1, -3],
  "targetSum": 3
}
{
  "array": [1, 2, 3, 4, 5, 6, 7, 8, 9],
  "targetSum": 17
}
{
  "array": [1, 2, 3, 4, 5, 6, 7, 8, 9, 15],
  "targetSum": 18
}
{
  "array": [-7, -5, -3, -1, 0, 1, 3, 5, 7],
  "targetSum": -5
}
{
  "array": [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47],
  "targetSum": 163
}
{
  "array": [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47],
  "targetSum": 164
}
{
  "array": [3, 5, -4, 8, 11, 1, -1, 6],
  "targetSum": 15
}
{
  "array": [14],
  "targetSum": 15
}
{
  "array": [15],
  "targetSum": 15
}


import program
import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = program.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)
'''