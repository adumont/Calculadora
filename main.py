import math

pila = []

def showPila():
  print(pila)

while True:
  showPila()
  s = input("")
  s = s.strip()

  for a in s.split(" "):
    if a in ["+", "-", "/", "*", "^"]:
      n2 = pila.pop()
      n1 = pila.pop()
      
      if a == "+": pila.append(n1+n2)
      elif a == "-": pila.append(n1-n2)
      elif a == "*": pila.append(n1*n2)
      elif a == "/": pila.append(n1/n2)
      elif a == "^": pila.append(n1**n2)

    elif a == "pi":
      pila.append(math.pi)

    else:
      pila.append(float(a))

