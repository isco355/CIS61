def make_withdraw(balance, password):
    """Return a password-protected withdraw function.
    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    attempts= []
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
           return 'Insufficient funds'
        balance = balance - amount
        return balance

    def authenticateTransaction(amount,password_attempt):
        nonlocal balance,password,attempts

        if len(attempts) >=3:
            message = f"Your account is locked. Attempts: {attempts}"
            return message

        if password_attempt == password:
           return withdraw(amount)
        else:
            attempts.append(password_attempt)
            message='Incorrect password'
            return message


    return authenticateTransaction
