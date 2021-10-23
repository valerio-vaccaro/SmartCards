from smartcard.System import readers
# originale su https://www.mmxforge.net/index.php/sviluppo/python/item/9-lettura-dei-dati-della-tessera-sanitaria-con-python
# convertito per python3 

r = readers()
reader = r[0]
print(f'Sto usando: {reader}')
connection = reader.createConnection()
connection.connect()

#Seleziona del MF
#CLS 00, istruzione A4 (seleziona file), P1 = P2 = 0 (seleziona per ID),
#Lc: 2, Data: 3F00 (id del MF)
SELECT_MF = [0x00, 0xA4, 0x00, 0x00, 0x02, 0x3F, 0x00]
data, sw1, sw2 = connection.transmit(SELECT_MF)
#se tutto è andato a buon fine sw1 e sw2 contengono
#rispettivamente i valori 0x90 e 0x00 il corrispettivo del 200 in HTTP

#Seleziona del DF1...vedi sopra
SELECT_DF1 = [0x00, 0xA4, 0x00, 0x00, 0x02, 0x11, 0x00]
data, sw1, sw2 = connection.transmit(SELECT_DF1)

#Seleziona del file EF.Dati_personali... vedi sopra sopra
SELECT_EF_PERS = [0x00, 0xA4, 0x00, 0x00, 0x02, 0x11, 0x02]
data, sw1, sw2 = connection.transmit(SELECT_EF_PERS)

#leggiamo i dati
#CLS 00, istruzione B0 (leggi i dati binari contenuti nel file
READ_BIN = [0x00, 0xB0, 0x00, 0x00, 0x00, 0x00]
data, sw1, sw2 = connection.transmit(READ_BIN)
#data contiene i dati anagrafici in formato binario
#trasformiamo il tutto in una stringa
stringa_dati_personali = bytearray(data).decode()
print(f'Stringa dati personali: {stringa_dati_personali}')

dimensione = int(stringa_dati_personali[0:6],16)
print(f'Dimensione in byte dei dati: {dimensione}')


prox_field_size = int(stringa_dati_personali[6:8], 16)
da = 8
a = da + prox_field_size
if prox_field_size > 0:
  codice_emettitore = stringa_dati_personali[da:a]
  print(f'Codice emettitore: {codice_emettitore}')

da = a
a +=2
prox_field_size = int(stringa_dati_personali[da:a], 16)
da=a
a += prox_field_size
if prox_field_size > 0:
  data_rilascio_tessera = stringa_dati_personali[da:a]
  print(f'Data rilascio tessera: {data_rilascio_tessera[0:2]}/{data_rilascio_tessera[2:4]}/{data_rilascio_tessera[-4:]}')

da = a
a +=2
prox_field_size = int(stringa_dati_personali[da:a], 16)
da=a
a += prox_field_size
if prox_field_size > 0:
  data_scadenza_tessera = stringa_dati_personali[da:a]
  print(f'Data scadenza tessera: {data_scadenza_tessera[0:2]}/{data_scadenza_tessera[2:4]}/{data_scadenza_tessera[-4:]}')

da = a
a +=2
prox_field_size = int(stringa_dati_personali[da:a], 16)
da=a
a += prox_field_size
if prox_field_size > 0:
  cognome = stringa_dati_personali[da:a]
  print(f'Cognome: {cognome}')

da = a
a +=2
prox_field_size = int(stringa_dati_personali[da:a], 16)
da=a
a += prox_field_size
if prox_field_size > 0:
  nome = stringa_dati_personali[da:a]
  print(f'Nome: {nome}')

da = a
a +=2
prox_field_size = int(stringa_dati_personali[da:a], 16)
da=a
a += prox_field_size
if prox_field_size > 0:
  data_nascita = stringa_dati_personali[da:a]
  print(f'Data di nascita: {data_nascita}')

da = a
a +=2
prox_field_size = int(stringa_dati_personali[da:a], 16)
da=a
a += prox_field_size
if prox_field_size > 0:
  sesso = stringa_dati_personali[da:a]
  print(f'Sesso: {sesso}')

da = a
a +=2
prox_field_size = int(stringa_dati_personali[da:a], 16)
da=a
a += prox_field_size
if prox_field_size > 0:
  statura = stringa_dati_personali[da:a]
  print(f'Statura: {statura}')

da = a
a +=2
prox_field_size = int(stringa_dati_personali[da:a], 16)
da=a
a += prox_field_size
if prox_field_size > 0:
  cf = stringa_dati_personali[da:a]
  print(f'CF: {cf}')

da = a
a +=2
prox_field_size = int(stringa_dati_personali[da:a], 16)
da=a
a += prox_field_size
if prox_field_size > 0:
  cittadinanza = stringa_dati_personali[da:a]
  print(f'Cittadinanza: {cittadinanza}')

da = a
a +=2
prox_field_size = int(stringa_dati_personali[da:a], 16)
da=a
a += prox_field_size
if prox_field_size > 0:
  comune = stringa_dati_personali[da:a]
  print(f'Comune di Nascita: {comune}')

da = a
a +=2
prox_field_size = int(stringa_dati_personali[da:a], 16)
da=a
a += prox_field_size
if prox_field_size > 0:
  stato = stringa_dati_personali[da:a]
  print(f'Stato: {stato}')

da = a
a +=2
prox_field_size = int(stringa_dati_personali[da:a], 16)
da=a
a += prox_field_size
if prox_field_size > 0:
  estremi = stringa_dati_personali[da:a]
  print(f'Estremi atto nascita: {estremi}')

da = a
a +=2
prox_field_size = int(stringa_dati_personali[da:a], 16)
da=a
a += prox_field_size
if prox_field_size > 0:
  residenza = stringa_dati_personali[da:a]
  print(f'Comune di residenza: {residenza}')

da = a
a +=2
prox_field_size = int(stringa_dati_personali[da:a], 16)
da=a
a += prox_field_size
if prox_field_size > 0:
  indirizzo = stringa_dati_personali[da:a]
  print(f'Indirizzo: {indirizzo}')

da = a
a +=2
prox_field_size = int(stringa_dati_personali[da:a], 16)
da=a
a += prox_field_size
if prox_field_size > 0:
  note = stringa_dati_personali[da:a]
  print(f'Note: {note}')
