class FakeHashService():
    def __init__(self):
        pass
    def hash(self, password):
        return password +'HASEHD'

    def check(self, password, hashed):
        if(hashed == password + 'HASHED'):
            return True
        else:
         return False