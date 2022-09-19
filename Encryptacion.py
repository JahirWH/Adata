from cryptography.fernet import Fernet


def des():
	
	print("Encriptar escriba 1")
	print("Desencryptar escriba 2")
	opcion=input(":  ")

	return opcion



def encrypted():
	key = Fernet.generate_key()
	print(key)
	encry="hola"
	  
	with open('key.key', 'wb') as filekey:
	   filekey.write(key)
	   

	  
	fernet = Fernet(key) 
	  
	with open('inventario.csv', 'rb') as file: 
	    original = file.read() 
	      
	encrypted = fernet.encrypt(original) 
	with open('inventario.csv', 'rb') as file: 
	    original = file.read()

	  
	with open('inventario.csv', 'wb') as encrypted_file: 
	    encrypted_file.write(encrypted) 
	    print("Archivo encryptado con exito")


def decrypted():
	key = Fernet 
	  
	with open('key.key', 'rb') as filekey: 
	    key = filekey.read() 
	  
	fernet = Fernet(key) 
	  
	with open('inventario.csv', 'rb') as enc_file: 
	    encrypted = enc_file.read() 
	  
	decrypted = fernet.decrypt(encrypted)
	des=['desncryptado']
	  
	with open('inventario.csv', 'wb') as dec_file:
	    dec_file.write(decrypted) 
	    print("archivo desencriptado con exito")
	

def main():
	while True:
		opcion=des()
		if opcion=='1':
			encrypted()
		elif opcion=='2':
			decrypted()
		elif opcion=='exit':
			break
	return

			
	
	

main()
