import re
# Main
# Open the file in read mode ('r')
with open('data.txt', 'r') as file:
  # Read the entire contents of the file and separate lines into a vector
  lines = [line.strip() for line in file.readlines()]
  red_regex_pattern = re.compile(r'[0-9]+ red', re.IGNORECASE)
  green_regex_pattern = re.compile(r'[0-9]+ green', re.IGNORECASE)
  blue_regex_pattern = re.compile(r'[0-9]+ blue', re.IGNORECASE)
  total_add = 0
  for line in lines:
    biggest_red = 0
    red_string =  red_regex_pattern.findall(line)
    red_numbers = [int(re.search(r'\d+', string).group()) for string in red_string]
    for number in red_numbers:
      if number > biggest_red:
        biggest_red = number

    biggest_green = 0
    green_string =  green_regex_pattern.findall(line)
    green_numbers = [int(re.search(r'\d+', string).group()) for string in green_string]
    for number in green_numbers:
      if number > biggest_green:
        biggest_green = number

    biggest_blue = 0
    blue_string =  blue_regex_pattern.findall(line)
    blue_numbers = [int(re.search(r'\d+', string).group()) for string in blue_string]
    for number in blue_numbers:
      if number > biggest_blue:
        biggest_blue = number    
    total_add = total_add + (biggest_red * biggest_green * biggest_blue)

  file.close()
    
  print (total_add)
  
