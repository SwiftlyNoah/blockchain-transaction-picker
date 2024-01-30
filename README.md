# Transaction Picker

A lightweight Flask app that implements basic transaction fee functionality (with some fun twists)

### Build Instructions
- Clone this repo and navigate to its directory
- Open the `TransactionPicker.postman_collection.json` in Postman (optional)
- Run `python transactionpicker.py` to start the flask server
- Make calls to the endpoints at `http://localhost:5001` by using Postman or another method of your choosing

### Endpoints
- `GET` `get_transactions` returns all transactions
- `GET` `get_ten_highest_fees` returns the 10 transactions with the highest fees
- `GET` `get_ten_lowest_fees` returns the 10 transactions with the lowest fees
- `GET` `get_next_highest_total` gets the sum of the second highest total of fees
- `GET` `get_greediest_transaction` returns the transaction with the lowest fee:amount ratio
