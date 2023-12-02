import re

# Transform words to numbers
def string_to_number(strings):
  word_to_number = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
  }
  result_string = ""
  for string in strings:
    lowercased_string = string.lower()
    num = word_to_number.get(lowercased_string, string)
    result_string += num
  return result_string
  

# Main
# Open the file in read mode ('r')
with open('data.txt', 'r') as file:
  # Read the entire contents of the file and separate lines into a vector
  lines = [line.strip() for line in file.readlines()]

  # Regex expression for numbers and numbers as words
  number_pattern = re.compile(r'(?=(zero|one|two|three|four|five|six|seven|eight|nine|\d))', re.IGNORECASE)
  add_result = 0
  for line in lines:
    # Get every number in line and put it into a string
    line_numbers = number_pattern.findall(line)
    # Transform words to numbers
    line_numbers_transformed = string_to_number(line_numbers)
    # Get the first and last numbers and add them to add_result
    correct_line_number = int(line_numbers_transformed[0] + line_numbers_transformed[-1])
    add_result += correct_line_number
file.close()
# Display the content
print(add_result)