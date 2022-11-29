stabilimento={}
import pprint
pp=pprint.PrettyPrinter(indent=4)

def leggiCodice():
  codice=0
  while codice<=0:
    codice=int(input("Inserisci il codice: "))
    if codice<=0:
      print("Il codice deve essere un numero maggiore di 0")
  return codice

def leggiPosizione():
  fila=0
  numero=0
  while fila<=0 and numero<=0:
    fila=int(input("Inserire fila dell'ombrellone: "))
    numero=int(input("Inserisci numero dell'ombrellone: "))
    if(fila<=0 and numero<=0):
      print("Inserire numeri maggiori di 0")
  return(fila,numero)

def leggiPrezzo():
  prezzoBassaStagione=0
  prezzoAltaStagione=0
  while prezzoBassaStagione<=0 and prezzoAltaStagione<=0:
    prezzoBassaStagione=int(input("Inserire prezzo bassa stagione: "))
    prezzoAltaStagione=int(input("Inserisci prezzo alta stagione: "))
    if(prezzoBassaStagione<=0 and prezzoAltaStagione<=0):
      print("Inserire prezzi maggiori di 0")
  return[prezzoBassaStagione,prezzoAltaStagione]

def leggiDataPrenotazione():
  giorno=0
  mese=0
  anno=0
  while((giorno<=0 or giorno>31) and (mese<=0 or mese>12) and (anno<=0)):
    giorno=int(input("Inserire il giorno: "))
    mese=int(input("Inserire il mese: "))
    anno=int(input("Inserire l'anno: "))
    if((giorno<=0 or giorno>31) and (mese<=0 or mese>12) and (anno<=0)):
      print("Inserire numeri maggiori di 0")
  return(giorno,mese,anno)

def leggiGiorno():
  numGiorni=0
  while(numGiorni<=0):
    numGiorni=int(input("Inserire il numero di giorni: "))
    if(numGiorni<=0):
      print("Il numero di giorni deve essere maggiore di 0")
  return numGiorni

def leggiOpzione():
  sdraio=0
  lettino=0
  op=input("Ci sono opzioni aggiuntive? sì/no: ")
  if(op=="sì"):
    while sdraio<=0 and lettino<=0:
      sdraio=int(input("Inserire numero di sdraio: "))
      lettino=int(input("Inserire numero di lettini: "))
      if(sdraio<=0 and lettino<=0):
        print("I numeri non devono essere minori di 0")
    return(sdraio,lettino)
  else:
    return(sdraio,lettino)

def leggiChiave():
  codice=leggiCodice()
  return codice

def leggiNumeroCodici():
  numeroCodici=0
  while numeroCodici<=0:
    numeroCodici=int(input("Inserire numero totale di codici: "))
    if(numeroCodici<=0):
      print("Il numero di codici deve essere maggiore di 0")  
  return numeroCodici

def leggiDatiValidi():
  posizione=leggiPosizione()
  prezzo=leggiPrezzo()
  data=leggiDataPrenotazione()
  giorni=leggiGiorno()
  opzione=leggiOpzione()
  print(opzione)
  return[posizione,prezzo,data,giorni,opzione]

def aggiungi():
  while True:
    chiave=leggiChiave()
    if chiave in stabilimento:
      print("COdice già esistente")
    else:
      break
  dati=leggiDatiValidi()
  stabilimento[chiave]=dati

def popola():
  numeroCodici=leggiNumeroCodici()
  for i in range(numeroCodici):
    aggiungi()
    
def prenotazioniOmbrellone():
  posizione=leggiPosizione()
  for chiave in stabilimento.keys():
    if(posizione[0]==stabilimento[chiave][0][0] and posizione[1]==stabilimento[chiave][0][1]):
      print(stabilimento[chiave])

def tuttePrenotazioni():
  pp.pprint(stabilimento)

def riduzionePrezzoPercentuale():
  riduzione=int(input("Inserire numero di punti percentuali per ridurre il prezzo: "))
  while(riduzione<=0):
    print("Reinserire")
    riduzione=int(input("Inserire numero di punti percentuali per ridurre il prezzo: "))
  mese=int(input("Inserire il mese: "))
  while(mese<=0):
    print("Reinserire")
    mese=int(input("Inserire il mese: "))
  


scelta=1
while (scelta!=0):
  print('0) Esci')
  print('1) Popola')
  print('2) Mostra le prenotazioni di un ombrellone')
  print('3) Mostra tutte le prenotazioni')
  print('4) Riduzione prezzo percentuale')
  print("5) Calcolo l'incasso totale di un mese")
  print('6) Visualizza le prenotazioni di n mesi')
  scelta=int(input('Scegli :'))
  if scelta==1:
    popola()
  elif scelta==2:
    prenotazioniOmbrellone()
  elif scelta==3:
    tuttePrenotazioni()
  elif scelta==4:
    riduzionePrezzoPercentuale()
""" 
  elif scelta==5:
    incassoTotaleMese()
  elif scelta==6:
    prenotazioniNMesi()"""
