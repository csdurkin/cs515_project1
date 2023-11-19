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

    for key, value in flattened_json_object.items():
        print(f'{base_object}.{key} = "{value}"')


if __name__ == '__main__':
    
    try:
    
        if len(sys.argv) == 2:
            
            file_name = sys.argv[1]

            with open(file_name, 'r') as file:
                json_object = json.load(file)
            
            gron(json_object, 'json')

        elif len(sys.argv) == 4:
            
            base_object = sys.argv[2]
            file_name = sys.argv[-1]

            with open(file_name, 'r') as file:
                json_object = json.load(file)
            
            gron(json_object, base_object)

        else: 
            
            json_object = json.load(sys.stdin)
            gron(json_object)

        sys.exit(0)

    except FileNotFoundError:
        print(f"FileNotFoundError: The file '{file_name}' was not found.")
        sys.exit(1)

    except json.JSONDecodeError:
        print(f'JSONDecodeError: JSON not available in {file_name}.')
        sys.exit(1)

    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)   

    

    
