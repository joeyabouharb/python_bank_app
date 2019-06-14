def validate_input(input):
  val = 0
  try:
    val = round(float(input), 2)
  except ValueError:
    print('Not a Number Bro! ')
  return val

class BankAccount:
  def __init__(self, balance, history, loggedIn, username):
    self.balance = balance
    self.history = history
    self.loggedIn = loggedIn
    self.username = username

  def logOut(self):
    self.loggedIn = False
    return 'Logging Out. Thanks for using our app!'

  def addDeposit(self):
    deposit = validate_input(input("How much would you like to deposit? "))
    if(deposit < 0 or deposit == 0):
      transaction = 'cannot deposit this amount!'
    else:
      self.balance += deposit
      transaction = f'Deposited ${deposit}, Closing Balance ${self.balance} '
      self.history.append(f'{transaction}')
    return transaction

  def withdrawBalance(self):
    withdraw = validate_input(input("How much would you like to withdraw? "))
    if withdraw < 0 or withdraw == 0:
      transaction = 'Please input valid currency value! '
    elif(self.balance - withdraw < 0 ):
      transaction = f'exceeded balance limit! Current Balance ${self.balance}'
    else:
      self.balance -= withdraw
      transaction = f'Withdrew ${withdraw}, Closing Balance ${self.balance}'
      self.history.append(f'{transaction}')
      
    return transaction

  def getBalance(self):
    self.history.append(f'Viewed Balance: ${round(self.balance, 2)}')
    return f'Current Balance ${self.balance}'

  def getHistory(self):
    history = ''
    for h in self.history:
      history += f'{h}\n'
    return history