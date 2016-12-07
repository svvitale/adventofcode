from hashlib import md5

door_id = 'reyedfim'
#door_id = 'abc'
password = {}
idx = 0

while len(password) < 8:
    hash_value = md5((door_id + str(idx)).encode()).hexdigest()

    if hash_value.startswith('00000'):
        try:
            position = int(hash_value[5])
        except ValueError:
            idx += 1
            continue

        if position in password or position > 7:
            idx += 1
            continue

        password[position] = hash_value[6]
        print(len(password), repr(password))

    idx += 1

for key in sorted(password):
    print(password[key], end='')
