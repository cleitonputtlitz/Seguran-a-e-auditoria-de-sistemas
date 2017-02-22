
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

textoClaro = 'A LIGEIRA RAPOSA MARROM SALTOU SOBRE O CACHORRO CANSADO'
textoEscuro = 'D OLJHLUD UDSRVD PDUURP VDOWRX VREUH R FDFKRUUR FDQVDGR'

chave = ord(textoEscuro[0]) - ord(textoClaro[0])

print 'Chave:' ,
print chave
