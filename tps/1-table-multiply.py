h=input("veuillez entrer un nombre 2 et 9:")
while not (h.isdigit and 2<=int (h)<=9) :
  h=input("veuillez entrer un nombre 2 et 9:")
    
a=int(h)
for i in range (1,13):
    print(f"{a}*{i}={a*i}")