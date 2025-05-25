with open('./input.txt', 'r') as f:
  input = f.read()

dices = {
  2: 'd2',
  3: 'd3',
  4: 'd4',
  6: 'd6',
  8: 'd8',
  10: 'd10',
  20: 'd20'
}

def find_dice(a, b):
  main_offset = a if a == 1 else a - 1
  interval_nums = b - a + 1
  multiplyer = 1
  if a == 1:
    for d in dices.keys():
      if d == b:
        print(f"{multiplyer}{dices[d]} + {main_offset}")
  for d in dices.keys():
    # check if it's possible with 1 dice
    if (a == 1 and b == d) or d + main_offset == b:
      print(f"{multiplyer}{dices[d]} + {main_offset}")
      break



find_dice(1, 4)

#print(input)
