#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f'Token({self.type}, {self.value})'

class Lexer:
    def __init__(self, source_code):
        self.tokens = []
        self.source_code = source_code

    def tokenize(self):
        tokens = re.findall(r'\".*?\"|\w+|[;=]', self.source_code)
        for token in tokens:
            if token == 'str' or token == 'int':
                self.tokens.append(Token('DATATYPE', token))
            elif token == '=':
                self.tokens.append(Token('ASSIGNMENT', token))
            elif token.isdigit():
                self.tokens.append(Token('INTEGER', token))
            elif re.match(r'\".*\"', token):
                self.tokens.append(Token('STRING', token[1:-1]))
            else:
                self.tokens.append(Token('IDENTIFIER', token))
        self.tokens.append(Token('END_STATEMENT', ';'))

    def get_tokens(self):
        return self.tokens
    


# In[3]:


def main():
    source_code = '''
    str name_member_1 = "Mohid Abdul Rehman";
    int roll_member_1 = 19122056;
    str name_member_2 = "M. Hashir Rasheed";
    int roll_member_2 = 19122055;
    '''
    lexer = Lexer(source_code)
    lexer.tokenize()
    tokens = lexer.get_tokens()

    # Count tokens
    token_count = len(tokens)

    # Output tokens in a terminal-friendly format
    for token in tokens:
        print(f'Type: {token.type:<12} Value: {token.value}')

    # Output token count
    print("\nToken count:", token_count)

if __name__ == '__main__':
    main()


# In[ ]:




