import serializer
import account_class

def get_options():
  opts = [
    'balance',
    'deposit',
    'withdraw',
    'history',
    'exit'
  ]
  options = 'Available options: '
  for option in opts:
    options += f'\n{option}'
  return options

def App():
  input_ = input('Create New Account ? (y/n) ')
  import getpass
  username = input('username: ')
  password = getpass.getpass()
  if(input_ == 'y'):
    password = serializer.create_new_account(username, password)
  user_account = serializer.get_user_account(username, password)
  bank_account = ''
  try:
    bank_account = account_class.BankAccount(
      user_account['balance'],
      user_account['history'],
      True,
      user_account['username']
    )
  except KeyError:
    raise ValueError('Corrupt Account- Please contact administrator. ')
    exit()
  options = get_options()
  print(f'{options}\n')
  while(bank_account.loggedIn == True):

    option = input("what would you like to do? ")
    option = option.lower()
    option = option.strip()
    output = menuSelect(bank_account, option)
    print(f'{output}\n')
    serializer.save_user_account(bank_account)

def invalid_selection():
  options = get_options()
  return f'Invalid Selection! \n{options}'

def menuSelect(bank_account, option):
  switch = {
    'balance': bank_account.getBalance,
    'deposit': bank_account.addDeposit,
    'withdraw': bank_account.withdrawBalance,
    'history': bank_account.getHistory,
    'exit': bank_account.logOut
  }
  result = switch.get(option, invalid_selection)
  return result()

App()