import hashlib
from Crypto.PublicKey import RSA
from Crypto import Random
from hashlib import sha256

#gera o par de chaves (publica e privada)
random = Random.new().read
chave = RSA.generate(1024, random)

#exporta a chave publica, para utiliza-la para criptografar uma mensagem
chave_publica = chave.publickey()

file = open('arquivo.txt', 'r')
texto = file.read()
file.close()

print texto

hashtexto = hashlib.sha256(texto).hexdigest()

print(hashtexto)

hashCodificado = chave.encrypt(hashtexto, 32)
print(hashCodificado)

file = open('file_signed', 'w')
file.write(str(texto))
file.write('##')
file.write(str(hashtexto))
file.write('\n##')
file.write(str(hashCodificado))
file.write('\n##')
file.write(str(chave_publica.exportKey("PEM")))
file.close()

