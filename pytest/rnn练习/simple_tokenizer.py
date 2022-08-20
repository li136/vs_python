"""
Date: 2022-8-14
Author: Zhenwei Shao
Description: A simple demo of tokenizer and detokenizer, which is elaborately
    designed for `shakespeare_sonnets.txt` dataset. Any other usage will need
    specific modification.
"""
import re

rule = re.compile(r'(?P<A>\w+)|(?P<B>(?<=\w)\'\w+)|(?P<C>\'\w+)|(?P<D>--|-)|(?P<L>(?<=\s)")|(?P<R>"(?=[\s,.?!]))|(?P<S>[,.?!:"\n\';])')  # the rule is elaborately defined for `shakespeare_sonnets.txt` dataset
    
def tokenize(text):
    """
    A simple implementation of tokenizer which convert a string into a 
    list of tokens. It works well on `shakespeare_sonnets.txt` dataset.
    The format of a token well be f'{type}{content}', where type is a
    capital letter and content is the a string span of the token.
    """
    scanner = rule.scanner(text)
    tokens = []
    while True:
        ret = scanner.search()
        # ret = scanner.match()
        if ret is None:
            break
        typ = ret.lastgroup
        tok = ret.group()
        tok = typ + tok
        tokens.append(tok)
    return tokens


def detokenize(tokens):
    """
    the reverse operation of `tokenize`
    """
    string = ''
    next_whitespace = False
    for tok in tokens:
        typ, tok = tok[0], tok[1:]
        if typ == 'A':
            if next_whitespace:
                string += ' '
            string += tok
            next_whitespace = True
        elif typ == 'B':
            string += tok
            next_whitespace = True
        elif typ == 'C':
            if len(string) != 0 and string[-1] not in ['\n', ' ', '"']:
                string += ' '
            string += tok
            next_whitespace = True
        elif typ == 'D':
            string += tok
            next_whitespace = False
        elif typ == 'L':
            if len(string) != 0 and string[-1] not in ['\n', ' ']:
                string += ' '
            string += tok
            next_whitespace = False
        elif typ == 'R':
            string += tok
            next_whitespace = True
        elif typ == 'S':
            string += tok
            next_whitespace = True
            if tok in ['\n']:
                next_whitespace = False
        else:
            raise Exception('Unknown token type')
    return string