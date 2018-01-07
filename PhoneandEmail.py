import pyperclip, re

def get_ph_numbers(text):
    ph = re.compile(r'''\d{3}[.-]\d{3}[.-]\d{3}''')
    return ph.findall(text)

def get_mail_id(text):
    mail_id = re.compile(r'''[A-Za-z0-9_]+@[a-zA-Z]+\.[a-zA-Z.]{2,6}''')
    return mail_id.findall(text)

text = str(pyperclip.paste())
print(text)

if text:
    phone_nums = get_ph_numbers(text)
    mail_ids = get_mail_id(text)

    print('\n'.join(phone_nums))
    print('\n'.join(mail_ids))
else:
    print("Please enter a valid text")

