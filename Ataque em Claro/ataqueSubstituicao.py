alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

textoClaro = 'FUJAMTODOSFOMOSDESCOBERTOSFUJAMTODOSFOMOSDESCOBERTOSABCDEFGHIJKLMNOPQRSTUVWXYZ'
textoEscuro ='GSCPF QITIN GIFIN TUNRI OUMQI NGSCP FQITI NGIFI NTUNR IOUMQ INPOR TUGAL BCDEF HIJKM NQSVW XYZ'
tamTexto = len(textoClaro)
chave =['' for x in range(26)]
i = j = 0
while i < tamTexto:
	k = alfabeto.find(textoClaro[i])
	if textoEscuro[j] != ' ':
		chave[k] = textoEscuro[j]
		i += 1
	j += 1

print 'Chave:' ,
i=0
while i < 26:	
	print chave[i],
	i += 1
