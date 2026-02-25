import hashlib

def privacy_amplification(key):
    key_string = ''.join(map(str, key))

    hash_object = hashlib.sha256(key_string.encode())
    hex_dig = hash_object.hexdigest()

    return hex_dig[:16]   # shorter secure key