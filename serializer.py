import json

def get_user_account(username, password):
  import bcrypt
  from pathlib import Path
  bank = Path("bankAccount.json")
  if bank.is_file() == False:
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    data = {
    "bank_account": {
      "balance": 0,
      "history": [],
      "username": username,
      "password": hashed.decode('utf-8')
      }
    }
    with open('bankAccount.json', 'w+', encoding='utf-8') as json_file:
      json.dump(data, json_file, ensure_ascii=False, indent=2)

  with open('bankAccount.json') as json_file:
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
  with open('bankAccount.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=2)
    return True