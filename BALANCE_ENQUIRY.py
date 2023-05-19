from django.shortcuts import render
from web3 import Web3

def index(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        balance = fetch_balance(address)
        transactions = fetch_transactions(address)
        return render(request, 'index.html', {'balance': balance, 'transactions': transactions})
    return render(request, 'index.html')

def fetch_balance(address):
    # Use a web3 library to fetch the current balance for the given Ethereum address
    # Replace this with your own implementation
    web3 = Web3()
    balance = web3.eth.get_balance(address)
    return balance

def fetch_transactions(address):
    # Use a web3 library to fetch the recent transactions for the given Ethereum address
    # Replace this with your own implementation
    web3 = Web3()
    transactions = web3.eth.get_transactions(address, limit=5)
    return transactions
