import sys
import csv

def csvsum(csv_reader_object, column):

    column_sum = 0
    
    for row in csv_reader_object:
        
        try: 
    
            column_sum += float(row[column])

        except ValueError:
            
            print(f'ValueError: {row[column]} cannot be converted to a numerical value.')

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
                        
                        total_sum += csvsum(csv_reader_object, column)
                
            print(f'Total sum of all columns: {total_sum}')

            sys.exit(0)

        else:
            
            csv_reader_object = csv.DictReader(sys.stdin)
            
            total_sum = 0
            
            for column in sys.argv[2:]:
                
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
        print(f'Error: {e}')
        sys.exit(1)       
        
