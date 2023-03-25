import hashlib
SIGN = '2005cc'
class EncDeEnc:
    def __init__(self, deEncrypted=''):
        self.deEnc = deEncrypted
    def hash_encrypt(self):
        enc = hashlib.sha256(self.deEnc.encode()).hexdigest()
        return enc


def mine(transaction_data):
    array_transaction_data = transaction_data.split('/')
    if len(array_transaction_data) > 3:
        array_transaction_data.pop()
    i = 0

    while True:
        if len(array_transaction_data) > 3:
            array_transaction_data.pop()

        array_transaction_data.append(str(i))
        new_transaction_data = '/'.join(array_transaction_data)
        encryption_on_data = EncDeEnc(deEncrypted=new_transaction_data).hash_encrypt()

        if encryption_on_data.startswith(SIGN):
            new_transaction_data += f'/~~{encryption_on_data}'
            return new_transaction_data
        else:
            i += 1
string = input('String: ')
print()
print(mine(string))
input('press any key to continue...')
