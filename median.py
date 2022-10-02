"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
     try:
         print("Enter a list of numbers separated by commas: ")
         numbers = [float(value) for value in input().split(",")]
     except ValueError:
         print("Some input could not be converted to a number!")
     else:
         break

numbers.sort()
if len(numbers) % 2 == 0:
      leftMid = numbers[int((len(numbers) / 2) - 1)]
      rightMid = numbers[int(len(numbers) / 2)]
      mid = float(leftMid + rightMid) / 2
else:
      mid = float(numbers[int(len(numbers) / 2)])
print(mid)


