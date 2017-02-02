import hashlib
from Crypto.PublicKey import RSA
from hashlib import sha256

file = open('file_signed', 'r')
texto = file.read()

#separa o conteúdo do arquivo
(texto2,hashtexto, assinaturaArquivo, chave_publica) = texto.split(b'##')
hashtexto = hashtexto.replace("\n", "")
assinaturaArquivo = assinaturaArquivo.replace("\n","")

chave = RSA.importKey(chave_publica)

hashtexto2 = hashlib.sha256(texto2).hexdigest()

assinatura = chave.encrypt(hashtexto2, 32)

print("hash...")
print(hashtexto)
print(hashtexto2)
print("hash criptografado...")
print(assinaturaArquivo)
print(assinatura)

if assinaturaArquivo == str(assinatura):
	print("Arquivo válido")
else:
	print("Arquivo invalido")

file.close()

