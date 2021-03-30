import math

import os

# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
   # print out some text

pila = []

tamanio = 9

def showPila():
  l=len(pila)
  n=min(l,tamanio)

  print("____________________")
  for i in range(tamanio-n):
    print("%d:" % (tamanio-i))
  for i in range(n):
    num = "%f" % pila[l-n+i]
    pad = ' ' * (17 - len(num))

    print("%d: %s%s" % (n-i, pad, num))
  print("")
    
while True:
  screen_clear()
  showPila()
  s = input("")
  s = s.strip()

  for a in s.split(" "):
    if a in ["+", "-", "/", "*", "**", "%"]:
      n2 = pila.pop()
      n1 = pila.pop()
      
      if   a == "+":  pila.append(n1+n2)
      elif a == "-":  pila.append(n1-n2)
      elif a == "*":  pila.append(n1*n2)
      elif a == "/":  pila.append(n1/n2)
      elif a == "**": pila.append(n1**n2)
      elif a == "%":  pila.append(n1%n2)

    elif a.lower() == "drop":
      pila.pop()

    elif a.lower() == "dropn":
      n = int(pila.pop())
      for i in range(n):
        pila.pop()

    elif a.lower() == "pick":
      n = int(pila.pop())
      pila.append(pila[-n])

    elif a.lower() == "swap":
      n2 = pila.pop()
      n1 = pila.pop()
      pila.append(n2)
      pila.append(n1)

    elif a.lower() in ["purge", "clear"]:
      pila=[]

    elif a.lower() == "len":
      pila.append(len(pila))

    elif a == "pi":
      pila.append(math.pi)

    else:
      pila.append(float(a))

