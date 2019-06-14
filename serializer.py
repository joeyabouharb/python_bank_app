import json
import bcrypt
from pathlib import Path

def password_check(password):
  if (any(char.isupper() for char in password)
  and any(char.islower() for char in password) 
  and any(char.isdigit() for char in password)
  and len(password) >= 7):
    return password
  else:
    import getpass
    return password_check(getpass.getpass('Enter a password with at least one digit, one capital letter, lower case and 7 character length: '))



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
  password = password_check(password)
  hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
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
  return password


def get_user_account(username, password):
  bank = Path("bankaccount.json")
  if bank.is_file() == False:
    print('Please Create an account! ')
    exit()
  accounts = get_all_accounts()
  for account in accounts:
    hashed_pw = account['password'].encode('utf-8')
    if (bcrypt.checkpw(password.encode('utf-8'), hashed_pw) == True
    and username == account['username']):
      name = account['username']
      print(f'Welcome {name}\n')
      return account
  print('incorrect details!')
  exit()

def save_user_account(user_account):
  password = ''
  accounts = []
  bank = Path('bankaccount.json')
  if(bank.is_file() == False):
    print('this ain\'t it chief! ')
    exit()
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
