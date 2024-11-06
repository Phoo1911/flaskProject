class Transaction:
    def __init__(self, transaction_id, amount, transaction_type, description):
        self.transaction_id = transaction_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.description = description  

    def to_dict(self):
        return {
            'transaction_id': self.transaction_id,
            'amount': self.amount,
            'type': self.transaction_type,
            'description': self.description  
        }
