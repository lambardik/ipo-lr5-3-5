text = input("Введите строку: ")
vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
vowel_count = 0

for char in text.lower():
  if char in vowels:
    vowel_count += 1

print(f"Количество гласных: {vowel_count}")