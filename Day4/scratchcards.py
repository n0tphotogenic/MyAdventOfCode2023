import re

def main():
  with open('data.txt', 'r') as file:
    # Read the entire contents of the file and separate lines into a vector
    lines = [line.strip() for line in file.readlines()]
  file.close
  winner_pattern = re.compile(r'(?<=:)([^|]+)')
  picked_pattern = re.compile(r'(?<=\|)([^|\n]+)')
  result = 0
  for line in lines:
    winner_matches = re.findall(winner_pattern, line)
    picked_matches = re.findall(picked_pattern, line)
    winner_list = winner_matches[0].split()
    picked_list = picked_matches[0].split()
    winner_numbers = set(winner_list)
    picked_numbers = set(picked_list)
    common_numbers = winner_numbers.intersection(picked_numbers)
    number_of_commons = len(common_numbers)
    if number_of_commons == 0:
      points_in_line = 0

    else:
      points_in_line = 2**(number_of_commons - 1)
    result += points_in_line
    print(points_in_line)
  print(result)
if __name__ == "__main__":
  main()
