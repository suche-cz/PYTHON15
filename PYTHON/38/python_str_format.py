
email = 'emai@test.cz'


text = f'Vážený uživateli {email}, váš účet byl aktivován'
text
'Vážený uživateli emai@test.cz, váš účet byl aktivován'
text = 'Vážený uživateli ' + email + ', váš účet byl aktivován'

text
'Vážený uživateli emai@test.cz, váš účet byl aktivován'
text = 'Vážený uživateli %s, váš účet byl aktivován' % email
text
'Vážený uživateli emai@test.cz, váš účet byl aktivován'
text = 'Vážený uživateli %s, váš účet byl %s aktivován' % email
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    text = 'Vážený uživateli %s, váš účet byl %s aktivován' % email
TypeError: not enough arguments for format string
text = 'Vážený uživateli %s, váš účet byl %s aktivován' % email, 'xyz'
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    text = 'Vážený uživateli %s, váš účet byl %s aktivován' % email, 'xyz'
TypeError: not enough arguments for format string
text = 'Vážený uživateli %s, váš účet byl %s aktivován' % (email, 'xyz')
text
'Vážený uživateli emai@test.cz, váš účet byl xyz aktivován'
text = 'Vážený uživateli {0}, váš účet byl {1} aktivován'.format(email, 'xyz')
text
'Vážený uživateli emai@test.cz, váš účet byl xyz aktivován'
text = 'Vážený uživateli {0}, váš účet byl {1} aktivován {0} {0}'.format(email, 'xyz')
text
'Vážený uživateli emai@test.cz, váš účet byl xyz aktivován emai@test.cz emai@test.cz'
text = 'Vážený uživateli {user_mail}, váš účet byl {random_text} aktivován {user_email}'.format(user_mail=email, random_text='xyz')
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    text = 'Vážený uživateli {user_mail}, váš účet byl {random_text} aktivován {user_email}'.format(user_mail=email, random_text='xyz')
KeyError: 'user_email'
text = 'Vážený uživateli {user_mail}, váš účet byl {random_text} aktivován {user_mail}'.format(user_mail=email, random_text='xyz')
text
'Vážený uživateli emai@test.cz, váš účet byl xyz aktivován emai@test.cz'
