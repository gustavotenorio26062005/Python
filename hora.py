'''hour = int(input("Hora de início (horas): "))
mins = int(input("Hora de início (minutos): "))
dura = int(input("Duração do evento (minutos): "))

# Escreva seu código aqui.

i=0
mins+=dura

while mins > 59:
    mins-=60
    i+=1

if hour = 24:
    hour = 0

    
hour+=i

print(f'{hour}:{mins}')
'''
hour = int(input("Hora de início (horas): "))
mins = int(input("Hora de início (minutos): "))
dura = int(input("Duração do evento (minutos): "))
# encontre um total de todos os minutos
mins+=dura
# encontre um número de horas escondido em minutos e atualize a hora
i=0
while mins > 59:
    mins-=60
    i+=1
# minutos corretos para cair no intervalo (0..59)
# horas corretas para cair no intervalo (0..23)
hour+=i
if hour >= 24:
    hour=0
hour=i-1
print(hour, ":", mins, sep='')