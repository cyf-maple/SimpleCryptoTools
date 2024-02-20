def ic(text):
  resoult = {}
  for i in text:
      resoult[i] = text.count(i)  
  
  num = 0.0
  den = 0.0
  for val in resoult:
    i = resoult[val]
    num += i * (i - 1)
    den += i
  
  if (den == 0.0):
    return 0.0
  else:
    return num / ( den * (den - 1))

f = open("ic.txt", 'r', encoding='utf-8')
text = ''.join(filter(str.isalpha, f.read())).upper()

print(ic(text))