#!/usr/bin/python3

import re
                
def calc(A, B):
    int_pattern = re.compile(r"\d+")

    if isinstance(A, bool):
        return -1
    if isinstance(A, int):
        a = A
    elif isinstance(A, str) and int_pattern.fullmatch(A.strip()):
        a = int(A)
    else:
        return -1

    if isinstance(B, bool):
        return -1
    if isinstance(B, int):
        b = B
    elif isinstance(B, str) and int_pattern.fullmatch(B.strip()):
        b = int(B)
    else:
        return -1

    if not (1 <= a <= 999 and 1 <= b <= 999):
        return -1

    return a * b
        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
