import json
import bcrypt
from pathlib import Path

def output_to_file(accounts):
  with open('bankaccount.json', 'w+') as json_file:
    data = {
      "bank_accounts": accounts
    }
    json.dump(data, json_file, ensure_ascii=False, indent=2)


def get_all_accounts():
  accounts = []
  with open('bankaccount.json', 'r') as json_file:
    data = json.load(json_file)
    accounts = data['bank_accounts']
  return accounts

def create_new_account(username, password):
  if(len(password.decode('utf-8')) < 8):
    print('create a password that is larger than 8 characters')
    exit()
  hashed = bcrypt.hashpw(password, bcrypt.gensalt())
  acc = {
      "balance": 0,
      "history": [],
      "username": username,
      "password": hashed.decode('utf-8')
      }
  print('creating new account... ')
  bank = Path("bankaccount.json")
  if bank.is_file() == False:
    accounts = []
  elif bank.is_file() == True:
    accounts = get_all_accounts()
  for account in accounts:
    if(account['username'] == username):
      print('user already exists! ')
      exit()
  accounts.append(acc)
  output_to_file(accounts)
  return acc


def get_user_account(username, password):
  bank = Path("bankaccount.json")
  if bank.is_file() == False:
    print('Please Create an account! ')
    exit()
  accounts = get_all_accounts()
  for account in accounts:
    hashed_pw = account['password'].encode('utf-8')
    if (bcrypt.checkpw(password, hashed_pw) == True
    and username == account['username']):
      name = account['username']
      print(f'Welcome {name}\n')
      return account
  print('incorrect details!')
  exit()

def save_user_account(user_account):
  password = ''
  accounts = []
  with open('bankaccount.json', 'r', ) as json_file:
    data = json.load(json_file)
    accounts = data['bank_accounts']
    for account in accounts: 
      if(user_account.username == account['username']):
        accounts.remove(account)
        acc = {
        "balance": user_account.balance,
        "history": user_account.history,
        "username": user_account.username,
        "password": account['password']
        }
        accounts.append(acc)
  output_to_file(accounts)
  return True
