from re import findall
def order(sentence):
  return ' '.join(sorted(sentence.split(), key=lambda x: findall('[1-9]', x)))

print(order("is2 Thi1s T4est 3a"))
#"Thi1s is2 3a T4est"