from hashlib import md5

door_id = 'reyedfim'
password = ''
idx = 0

while len(password) < 8:
    hash_value = md5((door_id + str(idx)).encode()).hexdigest()

    if hash_value.startswith('00000'):
        password += hash_value[5]

    idx += 1

print(password)
