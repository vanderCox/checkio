def checkio(data):
    digit = False
    upper = False
    lower = False
    if len(data) > 9:
        for x in data:
            if x.isdigit():
                digit = True
            if x.islower():
                lower = True
            if x.isupper():
                upper = True
            if digit & upper & lower:
                return True
        return False
    else:
        return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
