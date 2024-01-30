transactions_list = [
    {'ID': 1, 'Amount': 5, 'Fee': 0.35},
    {'ID': 2, 'Amount': 7, 'Fee': 0.33},
    {'ID': 3, 'Amount': 0.5, 'Fee': 0.23},
    {'ID': 4, 'Amount': 0.7, 'Fee': 0.14},
    {'ID': 5, 'Amount': 1.7, 'Fee': 0.37},
    {'ID': 6, 'Amount': 1.4, 'Fee': 0.39},
    {'ID': 7, 'Amount': 7.3, 'Fee': 0.1},
    {'ID': 8, 'Amount': 1.67, 'Fee': 0.34},
    {'ID': 9, 'Amount': 5.7, 'Fee': 0.28},
    {'ID': 10, 'Amount': 3.7, 'Fee': 0.34},
    {'ID': 11, 'Amount': 7.5, 'Fee': 0.3},
    {'ID': 12, 'Amount': 3.1, 'Fee': 0.27},
    {'ID': 13, 'Amount': 4.6, 'Fee': 0.2},
    {'ID': 14, 'Amount': 5.2, 'Fee': 0.14},
    {'ID': 15, 'Amount': 7.5, 'Fee': 0.12},
    {'ID': 16, 'Amount': 1.37, 'Fee': 0.28},
    {'ID': 17, 'Amount': 9.1, 'Fee': 0.29},
    {'ID': 18, 'Amount': 2.5, 'Fee': 0.33},
    {'ID': 19, 'Amount': 2.6, 'Fee': 0.31},
    {'ID': 20, 'Amount': 2.2, 'Fee': 0.13},
    {'ID': 21, 'Amount': 6.8, 'Fee': 0.32},
    {'ID': 22, 'Amount': 9.3, 'Fee': 0.13},
    {'ID': 23, 'Amount': 4.3, 'Fee': 0.33}
]

from flask import Flask, jsonify, request
from itertools import combinations

app = Flask(__name__)

@app.route('/get_transactions', methods=['GET'])
def get_transactions():
    response = {'Transactions': transactions_list}
    return jsonify(response), 200

@app.route('/get_ten_highest_fees', methods=['GET'])
def get_ten_highest_fees():
    sorted_transactions = sorted(transactions_list, key=lambda x: x['Fee'], reverse=True)
    response = {'Transactions': sorted_transactions[:10]}
    return jsonify(response), 200

@app.route('/get_ten_lowest_fees', methods=['GET'])
def get_ten_lowest_fees():
    sorted_transactions = sorted(transactions_list, key=lambda x: x['Fee'])
    response = {'Transactions': sorted_transactions[:10]}
    return jsonify(response), 200

@app.route('/get_next_highest_total', methods=['GET'])
def get_next_highest_total():
    sorted_transactions = sorted(transactions_list, key=lambda x: x['Fee'])
    transactions = transactions_list[:9] + [transactions_list[10]]
    total_fees = sum(item['Fee'] for item in transactions)
    response = {'SecondHighestTotal': total_fees}
    return jsonify(response), 200

@app.route('/get_transaction', methods=['GET'])
def get_transaction():
    transaction_id = request.args.get('id', type=int)
    transaction = next((item for item in transactions_list if item['ID'] == transaction_id), None)
    if transaction:
        response = {'Transaction': transaction}
        return jsonify(response), 200
    else:
        return jsonify({'error': 'Transaction not found'}), 404

@app.route('/get_greediest_transaction', methods=['GET'])
def get_worst_value():
    worst_value_transaction = None
    worst_ratio = float('inf')

    for transaction in transactions_list:
        if transaction['Amount'] > 0:
            ratio = transaction['Fee'] / transaction['Amount']
            if ratio < worst_ratio:
                worst_ratio = ratio
                worst_value_transaction = transaction

    if worst_value_transaction:
        response = {
            'WorstValueRatio': worst_ratio,
            'Transaction': worst_value_transaction
        }
        return jsonify(response), 200
    else:
        return jsonify({'error': 'No valid transactions found'}), 404


app.run(host='0.0.0.0', port=5001)
