text = input("Введите строку: ")
letters = "аеёиоуыэюя"
letters_count = 0

for char in text.lower():
  if char in letters:
    letters_count += 1

print(f"Кол-во гласных: {letters_count}")
