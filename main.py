def count_words(text):
  words = text.split()
  return len(words)


if __name__ == "__main__":
  s = "Сәлем мир бұл тесттік жол"
  print(f"Бастапқы жол: {s}")
  print(f"Сөздер саны: {count_words(s)}")