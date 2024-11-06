from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for flashing messages

# Sample data structure
transactions = []

@app.route('/')
def index():
    return render_template('index.html', transactions=transactions)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    amount = request.form['transaction_amount']
    type = request.form['transaction_type']
    description = request.form['transaction_description']

    # Add the transaction )
    transactions.append({'amount': amount, 'type': type, 'description': description})

    flash('Transaction added successfully!', 'success')  # Flash message
    return redirect(url_for('index'))


@app.route('/delete_transaction/<int:transaction_id>', methods=['POST'])
def delete_transaction(transaction_id):
    try:
        del transactions[transaction_id]  # Delete the transaction by ID
        flash('Transaction deleted successfully!', 'success')
    except IndexError:
        flash('Error: Transaction not found.', 'error')

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)









