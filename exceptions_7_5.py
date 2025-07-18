import sys


def is_good_password_1(string: str) -> bool:
    if len(string) >= 9:
        if not (string.isalpha() or string.isdigit()):
            if not (string.isupper() or string.islower()):
                if string.lower() != string.upper():
                    return True

    return False


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(string: str) -> bool:
    if len(string) < 9:
        raise LengthError
    if string == string.upper() or string == string.lower() or not any(map(str.isalpha, string)):
        raise LetterError
    if not any(map(str.isdigit, string)):
        raise DigitError

    return True

for psw in sys.stdin:
    try:
        is_good_password(psw.strip())
        print('Success!')
    except LengthError:
        print('LengthError')
    except LetterError:
        print('LetterError')
    except DigitError:
        print('DigitError')

