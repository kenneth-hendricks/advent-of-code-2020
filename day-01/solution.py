import os
inputNums = open(os.path.join(os.path.dirname(__file__), 'input')).read().splitlines()

nums = set()
for inputNum in inputNums:
  num = int(inputNum)
  complement = 2020 - int(num)
  if complement in nums:
    print(complement * num)
  nums.add(num)
