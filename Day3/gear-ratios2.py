ADJACENT = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]

def is_symbol(char):
  return char == '*'

def is_possible(x, y, max_x, max_y):
  return 0 <= x < max_x and 0 <= y < max_y

def get_number(x, y, matrix, visited_matrix):
  number_string = str(matrix[y][x])
  visited_matrix[y][x] = True

  number_string = get_numbers_on_left(x, y, matrix, visited_matrix) + number_string
  number_string = number_string + get_numbers_on_right(x, y, matrix, visited_matrix)
  
  return int(number_string)

def get_numbers_on_left(x, y, matrix, visited_matrix):
  matrix_rows = len(matrix)
  matrix_cols = len(matrix[0])

  numbers_on_left = ""
  while is_possible(x - 1, y, matrix_rows, matrix_cols):
    x -= 1
    current_char = matrix[y][x]
    if not current_char.isdigit() or visited_matrix[y][x]:
      break
    numbers_on_left = str(current_char) + numbers_on_left
    visited_matrix[y][x] = True

  return numbers_on_left

  
def get_numbers_on_right(x, y, matrix, visited_matrix):
  matrix_rows = len(matrix)
  matrix_cols = len(matrix[0])

  numbers_on_right = ""
  while is_possible(x + 1, y, matrix_rows, matrix_cols):
    x += 1
    current_char = matrix[y][x]
    if not current_char.isdigit() or visited_matrix[y][x]:
      break
    numbers_on_right = numbers_on_right +str(current_char)
    visited_matrix[y][x] = True

  return numbers_on_right
def get_sum(matrix, visited_matrix):
  matrix_rows = len(matrix)
  matrix_cols = len(matrix[0])
  result = 0
  for y_pos in range(matrix_rows):
    for x_pos in range(matrix_cols):
      current_char = matrix[y_pos][x_pos]
      if not is_symbol(current_char):
        continue
      vector_of_numbers = []
      for direction in ADJACENT:
        new_x, new_y = x_pos + direction[0], y_pos + direction[1]
        if not is_possible(new_x, new_y, matrix_rows, matrix_cols):
          continue
        if matrix[new_y][new_x].isdigit() and not visited_matrix[new_y][new_x]:
          vector_of_numbers.append(get_number(new_x, new_y, matrix, visited_matrix))
      if len(vector_of_numbers) == 2:
        result += vector_of_numbers[0] * vector_of_numbers[1]
  return result

def main():
  with open('data.txt', 'r') as file:
    # Read the entire contents of the file and separate lines into a vector
    matrix = [line.strip() for line in file.readlines()]
  file.close
  visited_matrix = [[False for _ in row] for row in matrix]
  print(get_sum(matrix, visited_matrix))
  

if __name__ == "__main__":
  main()
