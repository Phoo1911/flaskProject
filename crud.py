from models import Transaction

# In-memory storage for transactions (a list)
transaction_list = []

def add_transaction(amount, transaction_type, description):
    transaction_id = len(transaction_list) + 1  # Generate an ID based on the list length
    transaction = Transaction(transaction_id, amount, transaction_type, description)
    transaction_list.append(transaction)
    return transaction.to_dict()

def get_transactions():
    return [transaction.to_dict() for transaction in transaction_list]

def delete_transaction(transaction_id):
    for transaction in transaction_list:
        if transaction.transaction_id == transaction_id:
            transaction_list.remove(transaction)
            return True
    return False

