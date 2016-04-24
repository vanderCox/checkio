def checkio(text):
    text = text.lower()
    lst = list(text)
    cnt = -1
    char = lst[0]
    lst = sorted(lst)
    for it in lst:
        if str(it).isalpha():
            if lst.count(it) > cnt:
                cnt = lst.count(it)
                char = it

    return char

if __name__ == '__main__':
    # assert checkio("Hello World!") == "l", "Hello test"
    # assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")