from cryptography.fernet import Fernet


def des():
	
	print("Encriptar escriba 1")
	print("Desencryptar escriba 2")
	opcion=input(":  ")

	return opcion


def decrypted():
	key = Fernet.generate_key() 
	  
	with open('filekey.key', 'rb') as filekey: 
	    key = filekey.read() 
	  
	fernet = Fernet(key) 
	  
	with open('nba.csv', 'rb') as enc_file: 
	    encrypted = enc_file.read() 
	  
	decrypted = fernet.decrypt(encrypted) 
	  
	with open('nba.csv', 'wb') as dec_file: 
	    dec_file.write(decrypted) 

def encrypted():
	key = Fernet.generate_key() 
	  
	with open('filekey.key', 'wb') as filekey: 
	   filekey.write(key)
	  
	fernet = Fernet(key) 
	  
	with open('nba.csv', 'rb') as file: 
	    original = file.read() 
	      
	encrypted = fernet.encrypt(original) 
	  
	with open('nba.csv', 'wb') as encrypted_file: 
	    encrypted_file.write(encrypted) 

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