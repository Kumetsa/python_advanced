import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class TooManyAtSymbolsError(Exception):
    pass


class NameCanBeOnlyAlphaNumbericalError(Exception):
    pass


VALID_DOMAINS = r"\.(com|bg|org|net)$"

while True:
    email = input("Enter your email:")
    name = email.split("@")[0]
    match = re.search(VALID_DOMAINS, email)

    if email == "End":
        break

    if email.count("@") > 1:
        raise TooManyAtSymbolsError("Maximum one @ symbol allowed.")

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if len(name) < 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if not name.isalnum():
        raise NameCanBeOnlyAlphaNumbericalError("Name must be only alphanumeric symbols.")

    if not match:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org,.net")

    print("Email is valid")
