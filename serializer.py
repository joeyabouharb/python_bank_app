import json

def get_user_account(username, password):
  import bcrypt
  from pathlib import Path
  bank = Path("bankaccount.json")
  if bank.is_file() == False:
    print('no user  found...')
    if(len(password.decode('utf-8')) < 8):
      print('create a password that is larger than 8 characters')
      exit()
    print('creating new account... ')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    data = {
    "bank_account": {
      "balance": 0,
      "history": [],
      "username": username,
      "password": hashed.decode('utf-8')
      }
    }
    with open('bankaccount.json', 'w+', encoding='utf-8') as json_file:
      json.dump(data, json_file, ensure_ascii=False, indent=2)
      print('created! ')

  with open('bankaccount.json') as json_file:
    data = json.load(json_file)
    if 'bank_account' not in data:
      raise ValueError("bank account was not found, error occured.")
      exit()
    if 'password' not in data['bank_account'] or 'username' not in data['bank_account']:
      raise ValueError("Corrupt file. Contact admin. ")
      exit()
    hashed_pw = data['bank_account']['password']
    if (bcrypt.checkpw(password, hashed_pw.encode('utf-8')) == False
    or username != data['bank_account']['username']):
      print('incorrect details!')
      exit()
    name = data['bank_account']['username']
    print(f'Welcome {name}')
    return data['bank_account']

def save_user_account(user_account):
  data = {
    "bank_account": {
      "balance": user_account.balance,
      "history": user_account.history,
      "username": user_account.username,
      "password": user_account.password,
    }
  }
  with open('bankaccount.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=2)
    return True