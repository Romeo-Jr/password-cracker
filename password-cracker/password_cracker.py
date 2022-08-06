import hashlib

def crack_sha1_hash(hash, use_salts = False):
    line = -1
    if use_salts == True:
        with open("known-salts.txt", "r") as salt_file:
            salt_data = salt_file.readlines()
            for salt_i in range(len(salt_data)):
                with open("top-10000-passwords.txt", "r") as plain_file:
                    plain_data = plain_file.readlines()
                    for plain_i in range(len(plain_data)):
                        text = salt_data[salt_i].strip() + plain_data[plain_i].strip()
 
                        hashing_data = hashlib.sha1(bytes(text, 'UTF-8')).hexdigest()
                
                        if hashing_data == hash:
                            line += plain_i

        if line == -1:
            return "PASSWORD NOT IN DATABASE"
        else:
            return plain_data[line+1].strip()
            

    elif use_salts == False:
        with open("top-10000-passwords.txt", "r") as file:
            data = file.readlines()
            for i in range(len(data)):
                hashing_data = hashlib.sha1(bytes((data[i].strip()), 'UTF-8')).hexdigest()
                if hash == hashing_data:
                    line += i
        if line == -1:
            return "PASSWORD NOT IN DATABASE"
        else:
            return data[line+1].strip()
            