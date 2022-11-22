#1. Popola il dizionario con i dati qui sopra.
import pprint
pp=pprint.PrettyPrinter(indent=4)
diz={"Giuseppe Gullo":[(("corsa campestre"),(40,21,0),"allievi"),(("corsa 100mt"),(0,12,0),"juniores mas"),(("corsa 200mt"),(0,29,19),"juniores mas")],
     "Antonia Barbera":[(("corsa campestre"),(0,39,11),"juniores fem"),(("corsa 100mt"),(0,18,0),"juniores fem"),(("corsa 200mt"),(0,0,0),"juniores fem")],
     "Nicola Esposito":[(("corsa campestre"),(0,43,22),"allievi"),(("corsa 100mt"),(0,14,0),"juniores mas"),(("corsa 200mt"),(0,36,19),"juniores mas")]}
pp.pprint(diz) 
print()

#2. Aggiungi alla struttura il tuo nominativo con valori a scelta
diz["Valentina Marinelli"]=[(("corsa campestre"),(30,25,0),"allievi"),(("corsa 100mt"),(3,13,0),"juniores fem"),(("corsa 200mt"),(16,0,19),"juniores fem")]
pp.pprint(diz) 
print()

#3. Aggiungi la 4.disciplina sportiva 'corsa ad ostacoli 400 mt' per ogni atleta con tempo e categoria: (gornati 9:36)
    #Giuseppe Gullo (0,40,34) Allievo
    #Antonia Barbera (0,39,10) Allieva
    #Nicola Esposito (0,40,10) Allievo
    #TuoNominativo (0,40,26) Allievo/a.
diz["Giuseppe Gullo"]+=[(("corsa ostacoli 400mt"),(0,40,34),"allievi")]
diz["Antonia Barbera"]+=[(("corsa ostacoli 400mt"),(0,39,10),"allievi")]
diz["Nicola Esposito"]+=[(("corsa ostacoli 400mt"),(0,40,10),"allievi")]
diz["Valentina Marinelli"]+=[(("corsa ostacoli 400mt"),(0,40,26),"allievi")]
pp.pprint(diz) 
print()

#4. Stampa la tupla con le informazioni sulla disciplina sportiva corsa campestre per l'atleta Giuseppe Gullo (gornati 9:36)
print("Informazioni sulla corsa campestre di Giuseppe Gullo: ")
print(diz["Giuseppe Gullo"][0])
print()

#5. Stampa i singoli valori della tupla con le informazioni sulla disciplina corsa 200 mt. per Nicola Esposito (gornati 9:36)
print("Valori della tupla della corsa 200mt di Nicola Esposito: ")
print("Disciplina: " + str(diz["Nicola Esposito"][2][0]))
print("Tempi: " + str(diz["Nicola Esposito"][2][1]))
print("Categoria: " + str(diz["Nicola Esposito"][2][2]))
print()

#6. Stampa il tempo di Antonia Barbera nella corsa 100 mt. (gornati 9:36)
print("Tempo di Antonia Barbera nella corsa 100 mt: " + str(diz["Antonia Barbera"][1][1]))
print()

#7. Stampa il tempo minimo riportato nella corsa 100mt della categoria Juniores mas. (gornati 9:36)
min=diz["Giuseppe Gullo"][1][1][1]
for chiave in diz.keys():
  if(diz[chiave][1][2]=="juniores mas"):
    for i in range(2):
      if(diz[chiave][1][1][i]<min and diz[chiave][1][1][i]!=0):
        min=diz[chiave][1][1][i]
print(f"Il tempo minimo riportato nella corsa 100mt della categoria juniores mas è pari a {min}.")
print()

#8. Stampa il tempo massimo riportato nella corsa 200mt della categoria Juniores mas. (gornati 9:47)
max=diz["Giuseppe Gullo"][2][1][0]
for chiave in diz.keys():
  if(diz[chiave][2][2]=="juniores mas"):
    for i in range(2):
      if(diz[chiave][2][1][i]>max):
        max=diz[chiave][2][1][i]
print(f"Il tempo massimo riportato nella corsa 200mt della categoria juniores mas è pari a {max}.")
print()

#9. Stampa la media dei tempi nella corsa campestre della categoria allievi. (gornati 9:47)
sommaMin=0
sommaSec=0
sommaMill=0
cont=0
for chiave in diz.keys():
  if(diz[chiave][0][2]=="allievi"):
    sommaMin+=diz[chiave][0][1][0]
    sommaSec+=diz[chiave][0][1][1]
    sommaMill+=diz[chiave][0][1][2]
    cont+=1
mediaMin=sommaMin/cont
mediaSec=sommaSec/cont
mediaMill=sommaMill/cont
print(f"La media dei minuti nei tempi della corsa campestre nella categoria allievi è pari a {round(mediaMin)}.")
print(f"La media dei secondi nei tempi della corsa campestre nella categoria allievi è pari a {round(mediaSec)}.")
print(f"La media dei millisecondi nei tempi della corsa campestre nella categoria allievi è pari a {round(mediaMill)}.")
mediaTotale=(mediaMin+mediaSec+mediaMill)/3
print(f"La media generale dei tempi della corsa campestre per la categoria allievi è pari a {round(mediaTotale)}.")

#10. Popola() : Realizzare le opportune funzioni per aggiungere al dizionario i dati validi relativi alle 4 gare per un atleta. (gornati 9:47, non completato)
def leggiNomeValido():
  nome=""
  while len(nome)==0:
    nome=input("Inserisci il nome: ")
    if len(nome)==0:
      print("Devi inserire il nome")
  return nome

def leggiCognomeValido():
  cognome=""
  while len(cognome)==0:
    cognome=input("Inserisci il cognome: ")
    if len(cognome)==0:
      print("Devi inserire il cognome")
  return cognome

def leggiChiave():
  nome=leggiNomeValido()
  cognome=leggiCognomeValido()
  return cognome+" "+nome

def leggiDisciplinaValida():
  disciplina=""
  while (len(disciplina)==0 and (disciplina!="corsa campestre" or disciplina!="corsa 100mt" or disciplina!="corsa 200mt" or disciplina!="corsa ostacoli 400mt")):
    disciplina=input("Inserisci la disciplina: ")
    if (len(disciplina)==0 and (disciplina!="corsa campestre" or disciplina!="corsa 100mt" or disciplina!="corsa 200mt" or disciplina!="corsa ostacoli 400mt")):
      print("Devi inserire la disciplina")
  return disciplina

def leggiTempiValidi():
  tempi=[0,0,0]
  tempi[0]=int(input("Inserire minuti: "))
  tempi[1]=int(input("Inserire secondi: "))
  tempi[2]=int(input("Inserire millisecondi: "))
  return tempi

def leggiCategoriaValida():
  categoria=""
  while (len(categoria)==0 and (categoria!="juniores fem" or categoria!="juniores mas" or categoria!="allievi")):
    categoria=input("Inserisci la categoria: ")
    if (len(categoria)==0 and (categoria!="juniores fem" or categoria!="juniores mas" or categoria!="allievi")):
      print("Devi inserire la categoria")
  return categoria  

def leggiDatiValidi():
  disciplina=leggiDisciplinaValida()
  tempi=leggiTempiValidi()
  categoria=leggiCategoriaValida()
  return[disciplina,tempi,categoria]

def aggiungi():
  while True:
    chiave=leggiChiave()
    if chiave in diz:
      print("Atleta già presente!")
    else:
      break
  for chiave in diz.keys():
    dati=leggiDatiValidi()
    diz[chiave]=dati

aggiungi()
print(diz)
