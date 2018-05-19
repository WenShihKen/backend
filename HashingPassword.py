from hashlib import sha256

def hashSafe(password):
    MySalt = "KenYEE"
    return sha256(sha256(password).hexdigest() + MySalt).hexdigest()