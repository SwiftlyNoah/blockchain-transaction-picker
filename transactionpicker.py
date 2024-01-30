transactions_list = [{'ID': 1, 'Data': 'Sent 5 BTC', 'Fee' : 0.1}
                     , {'ID': 2, 'Data': 'Sent 7 BTC', 'Fee' : 0.001}
                     , {'ID': 3, 'Data': 'Sent 0.5 BTC', 'Fee' : 0.02}
                     , {'ID': 4, 'Data': 'Sent 0.7 BTC', 'Fee' : 0.2}
                     , {'ID': 5, 'Data': 'Sent 1.7 BTC', 'Fee' : 0.0004}
                     , {'ID': 6, 'Data': 'Sent 1.4 BTC', 'Fee' : 0.00375}
                     , {'ID': 7, 'Data': 'Sent 7.3 BTC', 'Fee' : 0.001}
                     , {'ID': 8, 'Data': 'Sent 1.67 BTC', 'Fee' : 0.002}
                     , {'ID': 9, 'Data': 'Sent 5.7 BTC', 'Fee' : 0.09}
                     , {'ID': 10, 'Data': 'Sent 3.7 BTC', 'Fee' : 0.12}
                     , {'ID': 11, 'Data': 'Sent 7.5 BTC', 'Fee' : 0.33}
                     , {'ID': 12, 'Data': 'Sent 3.1 BTC', 'Fee' : 0.23}
                     , {'ID': 13, 'Data': 'Sent 4.6 BTC', 'Fee' : 0.24}
                     , {'ID': 14, 'Data': 'Sent 5.2 BTC', 'Fee' : 0.048}
                     , {'ID': 15, 'Data': 'Sent 7.5 BTC', 'Fee' : 0.08}
                     , {'ID': 16, 'Data': 'Sent 1.37 BTC', 'Fee' : 0.4}
                     , {'ID': 17, 'Data': 'Sent 9.1 BTC', 'Fee' : 0.06}
                     , {'ID': 18, 'Data': 'Sent 2.5 BTC', 'Fee' : 0.000008}
                     , {'ID': 19, 'Data': 'Sent 2.6 BTC', 'Fee' : 0.1234}
                     , {'ID': 20, 'Data': 'Sent 2.2 BTC', 'Fee' : 0.045}
                     , {'ID': 21, 'Data': 'Sent 6.8 BTC', 'Fee' : 0.0042}
                     , {'ID': 22, 'Data': 'Sent 9.3 BTC', 'Fee' : 0.0001}
                     , {'ID': 23, 'Data': 'Sent 4.3 BTC', 'Fee' : 0.008}]

from flask import Flask, jsonify
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
    all_combinations = combinations(transactions_list, 10)
    total_fees = [sum(item['Fee'] for item in combo) for combo in all_combinations]
    second_highest_total = sorted(list(set(total_fees)), reverse=True)[1]
    response = {'SecondHighestTotal': second_highest_total}
    return jsonify(response), 200

app.run(host='0.0.0.0', port=5001)
