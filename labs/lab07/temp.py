
def make_withdraw(balance, password):
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
def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    referece_account=withdraw
    is_authenticate = referece_account(0,old_password)
    allow_new_password=  type(is_authenticate)==int
    new_password_recorded=''
    old_password_recorded=''
    if allow_new_password:
        new_password_recorded = new_password
        old_password_recorded=old_password
    else:
        return is_authenticate

    def joined(amount,password_attempt):
        nonlocal old_password_recorded,new_password_recorded,referece_account
        
        if  password_attempt== new_password_recorded or password_attempt==old_password_recorded :
            return referece_account(amount,old_password_recorded)
        else:
            return referece_account(amount,password_attempt)


    return joined

        
        

        
    

    
    
