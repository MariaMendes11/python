import time

beatles = [] #lista beatles etapa 1

beatles.append("John Lennon") #etapa 2
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print(beatles)

for i in range(1): #etapa 3
    beatles.append("Stu Sutcliffe, Pete Best")

print(beatles)

del beatles[3:]  #etapa 4

beatles.insert(0, "Ringo Starr") #etapa 5

print("Lista final dos Beatles:", beatles)

time.sleep(2)