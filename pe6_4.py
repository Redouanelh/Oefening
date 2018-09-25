def new_password(newpassword):
    if len(newpassword) >= 6 and oldpassword != newpassword:
        print('Wachtwoord veranderd.')
    else:
        print('Wachtwoord kan niet veranderd worden.')

oldpassword = 'blabla030'

Wachtwoord = input('Voer uw nieuwe wachtwoord in.: ')

new_password(Wachtwoord)


