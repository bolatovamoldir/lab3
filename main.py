# Лабораториялық жұмыс №3. 1-есептің әр тапсырмасы өз астындағы print-пен


# 1. S1, S2 жолдары және C таңбасы берілген, S1 жолына C таңбасын енгізер алдында S2 жолын салыңыз.
def task_1(s1, s2, c):
  idx = s1.find(c)
  if idx != -1:
    return s1[:idx] + s2 + s1[idx:]
  return s1 + s2


print("1-есеп нәтижесі:", task_1(s1="abcdef", s2="XY", c="c"))


# 2. S1 жолынан S2 сәйкес келетін барлық ішкі жолдарды жойыңыз.
def task_2(s1, s2):
  return s1.replace(s2, "")


print("2-есеп нәтижесі:", task_2(s1="hello world world", s2="world"))


# 3. S1 жолындағы S2 жолының соңғы пайда болуын S3-ке ауыстырыңыз.
def task_3(s1, s2, s3):
  idx = s1.rfind(s2)
  if idx != -1:
    return s1[:idx] + s3 + s1[idx + len(s2) :]
  return s1


print("3-есеп нәтижесі:", task_3(s1="test test test", s2="test", s3="NEW"))


# 4. Бастапқы жолдың бірінші және екінші нүктелерінің арасында орналасқан ішкі жолды көрсету.
def task_4(s):
  first = s.find(".")
  second = s.find(".", first + 1) if first != -1 else -1
  if first != -1 and second != -1:
    return s[first + 1 : second]
  return s


print("4-есеп нәтижесі:", task_4(s="abc.def.ghi"))


# 5. Бос орындармен бөлінген сөздердің санын анықтаңыз.
def task_5(s):
  return len(s.split())


print(
    "5-есеп нәтижесі (Сөздер саны):",
    task_5(s="қазақстан республикасы алматы қаласы"),
)


# 6. Бір әріптен басталатын және аяқталатын сөздердің санын анықтаңыз.
def task_6(s):
  words = s.split()
  count = 0
  for w in words:
    if len(w) > 0 and w[0].lower() == w[-1].lower():
      count += 1
  return count


print("6-есеп нәтижесі (Басы мен аяғы бірдей):", task_6(s="аша қала казак тез"))


# 7. Дәл үш "А" (немесе "а") әрпі бар сөздердің санын анықтаңыз.
def task_7(s):
  words = s.split()
  return sum(1 for w in words if w.lower().count("а") == 3)


print("7-есеп нәтижесі (Үш 'а' әрпі бар):", task_7(s="абака малина банан"))


# 8. Ең қысқа және ең ұзын сөздердің ұзындығын анықтаңыз.
def task_8(s):
  words = s.split()
  if not words:
    return 0, 0
  lengths = [len(w) for w in words]
  return min(lengths), max(lengths)


print("8-есеп нәтижесі (Мин/Макс ұзындық):", task_8(s="үй кітап компьютер"))


# 9. Сөздерді нүкте арқылы бөліп шығару (соңында нүкте қоймай).
def task_9(s):
  words = s.split()
  return ".".join(words)


print("9-есеп нәтижесі (Нүктемен бөлу):", task_9(s="алма өрік жүзім"))


# 10. Сөздерді кері ретпен орналастырып шығару.
def task_10(s):
  words = s.split()
  return " ".join(words[::-1])


print("10-есеп нәтижесі (Кері рет):", task_10(s="бір екі үш төрт"))


# 11. Әр сөздің бірінші әрпінің барлық келесі көріністерін алып тастау.
def task_11(s):
  words = s.split()
  new_words = []
  for w in words:
    if not w:
      continue
    first_char = w[0]
    rest = w[1:].replace(first_char, "")
    new_words.append(first_char + rest)
  return " ".join(new_words)


print("11-есеп нәтижесі (Әріпті өшіру):", task_11(s="алатау ананас"))


# 12. Сөздерді алфавиттік ретпен орналастырып шығару.
def task_12(s):
  words = s.split()
  return " ".join(sorted(words, key=str.lower))


print(
    "12-есеп нәтижесі (Алфавит бойынша):", task_12(s="алматы астана шымкент")
)


# 13. Әр сөз бас әріптен басталатын етіп жолды түрлендіру.
def task_13(s):
  return s.title()


print("13-есеп нәтижесі (Бас әріп):", task_13(s="привет мир, как дела?"))


# 14. Тыныс белгілері мен дауысты дыбыстардың санын есептеу (орыс тілі).
def task_14(s):
  vowels = "аеёиоуыэюя".lower()
  punctuations = ".,!?;:—-\"'"
  v_count = sum(1 for ch in s.lower() if ch in vowels)
  p_count = sum(1 for ch in s if ch in punctuations)
  return v_count, p_count


print(
    "14-есеп нәтижесі (Дауысты мен тыныс белгісі):",
    task_14(s="Привет, мир! Как дела?"),
)


# 15. Ең қысқа және ең ұзын сөзді шығару (бірнеше болса, соңғысын).
def task_15(s):
  words = s.split()
  if not words:
    return "", ""
  shortest = min(words, key=lambda x: (len(x), -words.index(x)))
  longest = max(words, key=lambda x: (len(x), -words.index(x)))
  return shortest, longest


print(
    "15-есеп нәтижесі (Ең қысқа және ұзын):",
    task_15(s="ай күн планета галактика"),
)