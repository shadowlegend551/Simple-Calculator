from tokenizer import *
from shuntingyard import *
from calculator import *

def main():
    while True:
        tokenized = tokenize(input('enter calculation: ').replace(' ',''))
        reverse_polish_notation = shunting_yard(tokenized)
        calculated_val = calculation(reverse_polish_notation)
        print(calculated_val)


if __name__ == '__main__':
    main()