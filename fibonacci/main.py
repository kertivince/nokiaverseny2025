with open('./input.txt', 'r') as f:
  input = f.read()

lines = input.split('\n')

#generates fibonacci numbers
def fibonacci_if_divisible(max_value):
  fibonacci_nums = [0, 1]
  divisible_fibonacci = [0]
  while fibonacci_nums[len(fibonacci_nums) - 1] + fibonacci_nums[len(fibonacci_nums) - 2] <= max_value:
    current = (fibonacci_nums[len(fibonacci_nums) - 1] + fibonacci_nums[len(fibonacci_nums) - 2])
    fibonacci_nums.append(current)
    if current % 3 == 0:
      divisible_fibonacci.append(current)
  return divisible_fibonacci

def main_function():
  for line in lines:
    # input validation
    if line.isdigit() == False:
      print('N/A')
    else:
      nums = fibonacci_if_divisible(int(line))
      # no solution
      if len(nums) == 0:
        print('N/A')
      else:
        for n in range(len(nums)):
          #we don't put a comma to the end of the line
          if n < len(nums) - 1:
            print(nums[n], end=", ")
          else:
            print(nums[n])

main_function()

