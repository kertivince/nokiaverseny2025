with open('./input.txt', 'r') as f:
  input = f.read()

lines = input.split('\n')

dices = {
  2: 'd2',
  3: 'd3',
  4: 'd4',
  6: 'd6',
  8: 'd8',
  10: 'd10',
  20: 'd20'
}

dice_sides = [20,10,8,6,4,3,2]

def calculate_wanted_num(a, b):
  offset = a - 1
  wanted = b - offset
  return wanted

def find_optimal(num, heck_offset):
  opt = []
  check = []
  for s in dice_sides:
    if num - s < 0 or num - s == 1:
      continue
    else:
      times = 1
      while num - s * times > 1:
        times += 1
      if num - s * times != 0:
        times -= 1
      num -= s * times
      opt.append(f"{times}{dices[s]}")
      check.append(dices[s] * times)
  return opt

def format_with_new_offset(main_offset, nums):
  new_offset = main_offset - (len(nums) - 1)
  output = '+'.join(nums)
  if new_offset > 0:
    output += f"+{new_offset}"
  elif new_offset < 0:
    output += str(new_offset)
  return output

def main_function():
  for line in lines:
    if line != '':
      interval = line.split()
      min = int(interval[0])
      max = int(interval[1])
      wanted = calculate_wanted_num(min, max)
      dices = find_optimal(wanted)
      solution = format_with_new_offset(min - 1, dices)
      print(solution)


main_function()
