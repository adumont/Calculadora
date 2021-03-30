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

def showPila():
  l=len(pila)
  n=min(l,4)

  print("____________________")
  for i in range(4-n):
    print("%d:" % (4-i))
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
    if a in ["+", "-", "/", "*", "**"]:
      n2 = pila.pop()
      n1 = pila.pop()
      
      if a == "+": pila.append(n1+n2)
      elif a == "-": pila.append(n1-n2)
      elif a == "*": pila.append(n1*n2)
      elif a == "/": pila.append(n1/n2)
      elif a == "**": pila.append(n1**n2)

    elif a == "pi":
      pila.append(math.pi)

    else:
      pila.append(float(a))

