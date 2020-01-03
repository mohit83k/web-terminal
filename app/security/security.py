import hashlib 

def sha256_append_salt(key,salt):
	assert type(key) == str
	assert type(salt) == str

	value = key+salt
	return hashlib.sha256(value.encode()).hexdigest()




