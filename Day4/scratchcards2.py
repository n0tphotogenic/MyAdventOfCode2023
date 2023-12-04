import re

def main():
  with open('data.txt', 'r') as file:
    # Read the entire contents of the file and separate lines into a vector
    lines = [line.strip() for line in file.readlines()]
  file.close
  winner_pattern = re.compile(r'(?<=:)([^|]+)')
  picked_pattern = re.compile(r'(?<=\|)([^|\n]+)')
  result = 0
  card_id = -1
  cards = [1 for _ in lines]
  for line in lines:
    card_id += 1
    aux_card_id = card_id
    winner_matches = re.findall(winner_pattern, line)
    picked_matches = re.findall(picked_pattern, line)
    winner_list = winner_matches[0].split()
    picked_list = picked_matches[0].split()
    winner_numbers = set(winner_list)
    picked_numbers = set(picked_list)
    common_numbers = winner_numbers.intersection(picked_numbers)
    number_of_commons = len(common_numbers)
    for _ in range(number_of_commons):
      if aux_card_id < len(cards):
        aux_card_id += 1
        cards[aux_card_id] += cards[card_id]

  for card in cards:
    result += card
  print(result)
if __name__ == "__main__":
  main()
