import pprint
pp=pprint.PrettyPrinter(indent=4)

#1. Popola
noleggio={"AA123BB":[("giugno",9,1293),("luglio",7,3231),("agosto",7,4020),("settembre",6,3928)],
          "AB345CD":[("giugno",8,1391),("luglio",6,1234),("agosto",9,4932),("settembre",8,2872)],
          "CD456FF":[("giugno",7,2872),("luglio",6,3273),("agosto",4,3211),("settembre",8,2827)]}
pp.pprint(noleggio) 

#2. Aggiungi i dati di un nuovo noleggio 
noleggio["ZZ999MV"]=[("giugno",10,15000),("luglio",10,15000),("agosto",10,15000),("settembre",10,15000)]
pp.pprint(noleggio)

#3. Stampa la tupla con tutte le informazioni sul mese di Luglio per la targa AA123BB
print(noleggio["AA123BB"][1])

#4. Stampa solo il numero di noleggi sul mese di Luglio per la targa AA123BB
print("Il numero di noleggi sul mese di Luglio per la targa AA123BB è pari a " + str(noleggio["AA123BB"][1][1]))

#5. Stampa la somma di tutti i km in tutti i mesi per la targa AB345CD
somma=0
for i in range(len(noleggio["AB345CD"])):
  somma+=noleggio["AB345CD"][i][2]
print(f"La somma di tutti i km in tutti i mesi per la targa AB345CD è pari a {somma} km.")

#6. Stampa la somma di tutti i km in tutti i mesi per tutte le macchine
somma=0
for targa, dati in noleggio.items():
  for dato in dati:
    somma+=dato[2]
print(f"La somma di tutti i km in tutti i mesi per tutte le macchine è pari a {somma} km.")

#7. Stampa il mese in cui sono stati fatti più km per la macchina targata CD456FF
max = noleggio["CD456FF"][0][2]
mese = noleggio["CD456FF"][0][0]
i=1
for i in range(len(noleggio["CD456FF"])):
  if(noleggio["CD456FF"][i][2]>max):
    max = noleggio["CD456FF"][i][2]
    mese = noleggio["CD456FF"][i][0]
print(f"Il mese in cui la macchina targata CD456FF ha fatto più km è {mese} con {max} km.")
