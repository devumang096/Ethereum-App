from django.shortcuts import render
import requests

def home(request):
    if request.method == 'POST':
        ethereum_address = request.POST['ethereum_address']
        api_key = 'N5C5GTJQEHY52PQF9PSSQ74KI275BF6AXP'

        # Fetch the balance
        balance_url = f'https://api.etherscan.io/api?module=account&action=balance&address={ethereum_address}&tag=latest&apikey={api_key}'
        balance_response = requests.get(balance_url)
        balance_data = balance_response.json()
        balance = balance_data.get('result')

        # Fetch the five most recent transactions
        transactions_url = f'https://api.etherscan.io/api?module=account&action=txlist&address={ethereum_address}&startblock=0&endblock=99999999&sort=desc&apikey={api_key}'
        transactions_response = requests.get(transactions_url)
        transactions_data = transactions_response.json()
        transactions = transactions_data.get('result')
        recent_transactions = []
        if transactions:
            for tx in transactions[:5]:
                tx_hash = tx.get('hash')
                from_address = tx.get('from')
                to_address = tx.get('to')
                value = float(tx.get('value', 0)) / 1e18  # Convert wei to Ether

                transaction_data = {
                    'hash': tx_hash,
                    'from': from_address,
                    'to': to_address,
                    'value': value
                }
                recent_transactions.append(transaction_data)

        context = {
            'ethereum_address': ethereum_address,
            'balance': balance,
            'recent_transactions': recent_transactions
        }
        return render(request, 'eth_app/home.html', context)

    return render(request, 'eth_app/home.html')
