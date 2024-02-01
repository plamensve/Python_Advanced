import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbol(Exception):
    pass


EMAIL_NAME = 4
DOMAINS = ('com', 'bg', 'org', 'net')

email = input()
while email != 'End':

    name = email.split('@')  # Check for the length of the name before the @ symbol
    length_of_name = len(name[0])  # Check for the length of the name before the @ symbol
    count_at_symbol = email.count('@')  # Check for the count of the '@' symbol in the input.txt
    domain = email.split('.')  # domain[-1] Check for used domain extension

    if length_of_name <= EMAIL_NAME:
        raise NameTooShortError('Name must be more than 4 characters')

    elif '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')

    elif count_at_symbol > 1:
        raise MoreThanOneAtSymbol('Email should contain only 1 @ symbol')

    elif domain[-1] not in DOMAINS:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    pattern = r'^([a-z][a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$'  # We check the entire structure of the input.txt
    matches = re.findall(pattern, email)

    if not matches:
        print(f'Email is invalid')
        exit()
    else:
        print(f'Email is valid')
        exit()

"""
Може да има пропуски в регекса - ако откриете такива, моля да ми ги оставите като коментар.
Разбирам, че може само с регекс да се валидира имейла. Разбирам, че може и без него да напраивм същото - идеята ми е да
Приложа Try-Except знанията и да си припомня части от регекса - как се структурира, как се използва и т.н.
Благодаря за отделеното време и внимание!
"""
