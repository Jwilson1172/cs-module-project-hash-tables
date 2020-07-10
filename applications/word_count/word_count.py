def word_count(s):
    ignored = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(' ')
    # removing all of the puncuation by removing them with the string's replace
    # function
    for i in ignored:
        s.replace(i, '')
    s = s.split(' ')
    return s


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(
        word_count(
            'This is a test of the emergency broadcast network. This is only a test.'
        ))
