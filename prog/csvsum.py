#!/usr/bin/env python3

import sys
import csv

def csvsum(csv_reader_object, column):
    
    column_sum = 0
    
    for row in csv_reader_object:
        
        try: 
            value = float(row[column])
            column_sum += value
            
        except ValueError:
            
            print(f'ValueError: {row[column]} cannot be converted to a numerical value.')

        except KeyError:
            
            print(f'KeyError: Column "{column}" not found in the current row.')

    print(f'Column: {column}; Sum: {column_sum}')

    return column_sum

if __name__ == '__main__':
    
    try: 
        
        if len(sys.argv) >= 3:
            
            file_name = sys.argv[1]

            total_sum = 0

            for column in sys.argv[2:]:
                
                with open(file_name, 'r') as file:
                    
                    csv_reader_object = csv.DictReader(file)       
                    
                    if not csv_reader_object.fieldnames:
                        print("CSV File is empty.")
                        sys.exit(1)
                    
                    total_sum += csvsum(csv_reader_object, column)

                #try:
                    #column_index = column
                    
                #except ValueError:
                    #print(f'Error: The column argument "{column}" is not a valid integer.')
                    #sys.exit(1)
                
            print(f'Total sum of all columns: {total_sum}')

            sys.exit(0)

        else:
            
            csv_reader_object = csv.DictReader(sys.stdin)
            
            total_sum = 0

            for column in sys.argv[2:]:
                
                #try:
                    #column_index = column
                    
                #except ValueError:
                    #print(f'Error: The column argument "{column}" is not a valid integer.')
                    #sys.exit(1)

                if not csv_reader_object.fieldnames:
                        print("CSV File is empty.")
                        sys.exit(1)
                        
                total_sum += csvsum(csv_reader_object, column)

            print(f'Total sum of all columns: {total_sum}')
   
            sys.exit(0)
            
    except FileNotFoundError:
        print(f'FileNotFoundError: The file "{file_name}" was not found.')
        sys.exit(1)

    except csv.Error as e:
        print(f'CSV Error: {e}')
        sys.exit(1)    

    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(f'Exception Error: {exc_type.__name__} - {exc_value}')
        sys.exit(1)

