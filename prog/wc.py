#!/usr/bin/env python3

import sys
import re

def wc(file_name, lines, flags):
    
    lines_count = len(lines)

    words = []
    for line in lines:
        words.extend(line.split())
    
    words_count = len(words)
    
    characters_count = sum(len(word) for word in words)

    if flags: 

        result = ''

        if 'l' in flags: 
            result += f'{lines_count}\t'

        if 'w' in flags: 
            result += f'{words_count}\t'

        if 'c' in flags: 
            result += f'{characters_count}\t'

        result += f'{file_name}'

        print(result)

    elif file_name == 'stdin': 
        
        print(f'{lines_count}\t{words_count}\t{characters_count}')

    else: 

        print(f'{lines_count}\t{words_count}\t{characters_count}\t{file_name}')

if __name__ == '__main__':

    try:  
        
        if len(sys.argv) >= 2:
            
            flags = []
            files_dict = {}
            
            for arg in sys.argv[1:]:

                if re.match(r'^-[lwc]+$', arg):
                    flags.extend(arg[1:])
                    continue
                    
                try:
                    with open(arg, 'r') as file:
                        files_dict[arg] = file.readlines()

                except FileNotFoundError:
                    files_dict[''] = arg
            
            for file_name, lines in files_dict.items(): 
                
                wc(file_name, lines, flags)
            
            sys.exit(0)

        else: 
            
            lines = sys.stdin.readlines()
            wc('stdin', lines, None)

    except FileNotFoundError:
            print(f"FileNotFoundError: The file '{arg}' was not found.")
            sys.exit(1)
                
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)   
