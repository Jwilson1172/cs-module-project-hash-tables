def replace_many(s: str, iter: list) -> str:
    """Takes a string and replaces each term in iter within that string

    Args:
        s (str): string containing items to be replaced
        iter (list): list of strings to find in the passed string

    Returns:
        str: string after replacing terms
    """
    for i in iter:
        s = s.replace(i, '')
    return s


def word_count(s):
    # get the passed variable ready for counting by replacing
    # the stop words and spliting the string into tokens

    # NOTE WARNING OCCURES RUNNING THIS LINE BECAUSE '\ ' IS AN INVALID EXCAPE
    # SEQ. howeve this isn't how it's being used in the literal string so im
    # not going to worry about it. it does come up as a warning while running
    # pytest though 
    s = replace_many(s, '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(' '))
    s = s.lower().split()

    # iterate through the list of tokens incrementing the dict everytime we
    # encounter duplicates
    d = {}
    for i in s:
        # check if in cache else add to cache
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


if __name__ == "__main__":
    print(word_count("Hello   Hello"))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(
        word_count(
            'This is a test of the emergency broadcast network. This is only a test.'
        ))
