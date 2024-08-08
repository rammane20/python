class LowBalanceException(Exception):
    pass

class Op:
    def __init__(self , balance = 0 ):
        self.balance = balance 

    def add(self , amount):
        
        if amount < balance:
            raise LowBalanceException("LowBalanceException error is generated")
        return   
try:
    number = Op(100)
    print(number.add())
except LowBalanceException:
    print("LowBalanceException error is generated")        
