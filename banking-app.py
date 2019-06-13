import serializer
import account_class

def App():
  import getpass
  username = input('username: ')
  password = getpass.getpass().encode('utf-8')
  user_account = serializer.get_user_account(username, password)
  bank_account = ''
  try:
    bank_account = account_class.BankAccount(
      user_account['balance'],
      user_account['history'],
      True,
      user_account['username'],
      user_account['password']
    )
  except KeyError:
    raise ValueError('Corrupt Account- Please contact administrator. ')
    exit()
  while(bank_account.loggedIn == True):
    option = input("what would you like to do? ")
    option = option.lower()
    option = option.strip()
    print(menuSelect(bank_account, option))
    serializer.save_user_account(bank_account)

def menuSelect(bank_account, option):
  switch = {
    'balance': bank_account.getBalance,
    'deposit': bank_account.addDeposit,
    'withdraw': bank_account.withdrawBalance,
    'history': bank_account.getHistory,
    'exit': bank_account.logOut
  }
  result = switch.get(option, lambda: 'Invalid Selection! ')
  return result()

App()