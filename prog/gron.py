#!/usr/bin/env python3

import sys
import json

def flatten(input_object, input_path = '', input_result = None):

    if input_result is None: 
        input_result = {}

    if isinstance(input_object, dict):
        for key, value in input_object.items():
            update_path = f'{input_path}.{key}' if input_path else key
            flatten(value, update_path, input_result)

    elif isinstance(input_object, list):
        for index, value in enumerate(input_object):
            update_path = f'{input_path}[{index}]'
            flatten(value, update_path, input_result)

    else:
        input_result[input_path] = input_object

    return input_result

def gron(json_object, base_object):

    flattened_json_object = flatten(json_object)

    if not flattened_json_object:
        print(f'{base_object}: Empty JSON')
    
    else: 
        for key, value in flattened_json_object.items():
            print(f'{base_object}.{key} = "{value}"')


if __name__ == '__main__':
    
    try:
    
        if len(sys.argv) == 2:
            
            input_string = sys.argv[1]
            
            if input_string[0] == '{' and input_string[-1] == '}':
                json_object = json.loads(input_string)
                gron(json_object, 'json')
            
            else:
                file_name = input_string
                with open(file_name, 'r') as file:
                    json_object = json.load(file)
                    gron(json_object, 'json')

        elif len(sys.argv) == 4:
            
            base_object = sys.argv[2]
            input_string = sys.argv[-1]

            if input_string[0] == '{' and input_string[-1] == '}':
                json_object = json.loads(input_string)
                gron(json_object, base_object)

            else:
                file_name = input_string
                with open(file_name, 'r') as file:
                    json_object = json.load(file)
                    gron(json_object, base_object)

        else: 
            
            file_name = None
            
            json_input = ' '.join(sys.stdin.readlines())
                        
            if json_input:
                json_object = json.loads(json_input)
                gron(json_object, 'json')
            
            else:
                print('Empty JSON input.')
                
        sys.exit(0)

    except FileNotFoundError:
        print(f'FileNotFoundError: The file "{file_name}" was not found.')
        sys.exit(1)

    except json.JSONDecodeError:
        print(f'JSONDecodeError: JSON not available in {file_name}.')
        sys.exit(1)

    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)
