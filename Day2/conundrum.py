import re
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14
# Main
# Open the file in read mode ('r')
with open('data.txt', 'r') as file:
  # Read the entire contents of the file and separate lines into a vector
  lines = [line.strip() for line in file.readlines()]
  red_regex_pattern = re.compile(r'[0-9]+ red', re.IGNORECASE)
  green_regex_pattern = re.compile(r'[0-9]+ green', re.IGNORECASE)
  blue_regex_pattern = re.compile(r'[0-9]+ blue', re.IGNORECASE)
  total_ids = 0
  id = 0
  for line in lines:
    id += 1
    skip = False
    red_string =  red_regex_pattern.findall(line)
    red_numbers = [int(re.search(r'\d+', string).group()) for string in red_string]
    for numbers in red_numbers:
      if numbers > MAX_RED:
        skip = True

    green_string =  green_regex_pattern.findall(line)
    green_numbers = [int(re.search(r'\d+', string).group()) for string in green_string]
    for numbers in green_numbers:
      if numbers > MAX_GREEN:
        skip = True

    blue_string =  blue_regex_pattern.findall(line)
    blue_numbers = [int(re.search(r'\d+', string).group()) for string in blue_string]
    for numbers in blue_numbers:
      if numbers > MAX_BLUE:
        skip = True

    if skip == True:
      continue
    total_ids += id
  file.close()
    
  print (total_ids)
  

