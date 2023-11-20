Connor Durkin
Stevens Login: cdurkin@stevens.edu

GitHub: https://github.com/csdurkin/cs515_project1

Project Time Estimate: 12 - 16 Hours

Emphasis on Estimate: Apologies. I did not realize that this would come up as measurement to provide, so I did not accurately track. Over a few days, I implemented the prog codes and felt confident. Then, I realized I had no idea how to do the tests and felt much less confident. I spent many hours in the final day trying to test my code and implement fixes. 

How Code was Tested: 

    As I write this, I've yet to correctly implement the test files (basic.in, basic.out, basic.arg.out, test.py, test.yml). Accepting I may not be able to figure this out, I wanted to try to test my codes using commands on the terminal. 
    
    I ran the program in the terminal and tested using the files "test.json", "text.csv", and "test.txt" where appropriate. I then updated these files before running subsequent tests. I also used stdin.
    
        ALL tests and results are listed below. 
            
Any Bugs or Issues You could Not Resolve:

    I admit that I felt false confidence, as my program seemed to be well implemented before needing to write the test files and harness. I now feel very confused on these, and therefore, they are not implemented at the time I write this, which is 9 p.m. on Sunday. Perhaps I will have a stroke of genius before midnight and this confusion will be resolved. 
    
    In an effort to focus my energies where points were most available, I've focused on this README.md file. I also am running tests using command lines, and correct my program codes accordingly. I am recording the tests and results in these files.
    
    - WC: I did find that to run the stdin for the wc.py, I needed to rely on the '<<<' operator to ensure correct output. I did in my code try to handle taking in the stdin by using the arg, and feeding this into the dict with an empty key (''), but this did not seem to resolve it correctly. There are no issues when the '<<<' is used in the command line.

An Example of a Difficult Issue or Bug and How You Resolved It:

    - Python 3 Interperter: I was running into the issue where my operating system was not using python3 autoamtically when runnning the command lines. Therefore, I added the line '#!/usr/bin/env python3' to the top of each of my programs.
    
    - Gron: For the input that uses stdin for gron.py, the json seemed like it could not appear on multiple lines. Only jsons that are written on a single line were being accepted and run by the program. I first tried to resolve this by using json_input = ' '.join(sys.stdin.readlines()), and my goal was to take a multiline input and concat the values onto a single line. In the end, I realized it was a simple syntax error. When I was inputing jsons one multiple lines, I was forgetting to add the quotes ('') before and after the arg. Once I added these, the function was able to accept multiline jsons. 

    -CSVSUM: I had trouble accessing the column names for a long period of time. In the end, I was incorrectly converting the type to be 'int', assuming this was the only correct option. I needed to remove this conversion and allow the columns to be named according to how they appear in the header. I also incorrectly believed the header would be included in the count, again an error associated with thinking it needed to be an integer. I thought every sum was off by one row, until I came to understand the purpose of the header and column names.

Three Extensions

1. Extension: More advanced wc: multiple files

    The program, wc.py, handles multiple files by first looping through all arguments provided in the command line, excluding the call to function. (Code: for arg in sys.argv[1:]:). Using a regular expression, this loop will catch any arguments that are meant as a flag. In addition, this loop with uses all others args as the keys within a related dictionary. The .readlines() function is used to create the values for this dictionary.
    
    Thereafter, each key and value is pulled form the dictionary (using items()) and these are passed into the wc function along with the pulled flags. Therefore, the wc function prints the counts for each file inputed and does so with the appropriate flags.
    
2. More advanced wc: flags to control output

    As mentioned above, the flags are founded using a regular expression within the first loop through the input values. The use of two loops will slow the function; however, this implementation allows the flags and file names to be inputted in any order. 

3. More advanced gron: control the base-object name

    In gron.py, the length of the command-line argument is checked, and subsequently, certain actions are taken based on the result (namely if there are two or four arguments). The latte case incidates that a custom base object name should be used. In this case, the base object and file name's are pulled using indexing. Then each is fed into the gron function, which places the base object name within the returned paths. Note, that if there are two arugments, 'json' is fed as the base object name into gron.py
     
GRON TESTS

    INPUT FILE (test.json) TESTS

        ===Test One===
        
            {
              "name": "Connor Durkin",
              "age": 31,
              "city": "Jersey City",
              "is_student": true
            }

            Test One Result:
        
            json.name = "Connor Durkin"
            json.age = "31"
            json.city = "Jersey City"
            json.is_student = "True"
        
        ===Test Two===
        
            {
              "name": "Connor Durkin",
              "age": 31,
              "Address": {
                "City": "Jersey City",
                "State": "New Jersey",
                "Zip": 7307
              },
              "isStudent": true
            }

            Test Two Result: 
        
            json.name = "Connor Durkin"
            json.age = "31"
            json.Address.City = "Jersey City"
            json.Address.State = "New Jersey"
            json.Address.Zip = "7307"
            json.isStudent = "True"

        ===Test Three===
            
            {
              "Connor Durkin": ["31", "Jersey City, NJ, 07307", "Student"],
              "Jane Doe": ["25", "Hoboken, NJ, 07030", "Student"]
            }
        
            Test Three Result:
            
            json.Connor Durkin[0] = "31"
            json.Connor Durkin[1] = "Jersey City, NJ, 07307"
            json.Connor Durkin[2] = "Student"
            json.Jane Doe[0] = "25"
            json.Jane Doe[1] = "Hoboken, NJ, 07030"
            json.Jane Doe[2] = "Student"

        ==Test Four===
        
            {
              "name": null,
              "address": null,
              "isStudent": null
            }

            Test Four Result:
        
            json.name = "None"
            json.address = "None"
            json.isStudent = "None"
            
        ===Test Five===
            
            {}
        
            Test Five Result: 
            
            json: Empty JSON
            

    STDIN TESTS
    
    
        ===Test One===
        
            python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/gron.py '{"name": "Connor Durkin", "age": 31, "city": "Jersey City", "is_student": true}'
            
            Test One Result: 
            
            json.name = "Connor Durkin"
            json.age = "31"
            json.city = "Jersey City"
            json.is_student = "True"
                        
            
        ===Test Two===
        
            python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/gron.py '{"name": "Connor Durkin", "age": 31, "Address": {"City": "Jersey City", "State": "New Jersey", "Zip": 7307}, "isStudent": true}'
            
            Test Two Result:
             
            json.name = "Connor Durkin"
            json.age = "31"
            json.Address.City = "Jersey City"
            json.Address.State = "New Jersey"
            json.Address.Zip = "7307"
            json.isStudent = "True"
        
        ===Test Three===
        
            python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/gron.py '{"Connor Durkin": ["31", "Jersey City, NJ, 07307", "Student"], "Jane Doe": ["25", "Hoboken, NJ, 07030", "Student"]}'
       
            Test Three Result: 
            
            json.Connor Durkin[0] = "31"
            json.Connor Durkin[1] = "Jersey City, NJ, 07307"
            json.Connor Durkin[2] = "Student"
            json.Jane Doe[0] = "25"
            json.Jane Doe[1] = "Hoboken, NJ, 07030"
            json.Jane Doe[2] = "Student"
   
        ===Test Four===
        
            python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/gron.py '{"name": null, "address": null, "isStudent": null}

            Test Four Result: 
            
            json.name = "None"
            json.address = "None"
            json.isStudent = "None"

        ===Test Five===
        
            python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/gron.py '{}'
            
            Test Five Result:
            
            json: Empty JSON


    EXTENSION TESTS (INPUT FILES)
    
        ===TEST ONE===
    
            python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/gron.py --obj o /Users/cdurkin/Desktop/test.json
            
            {
                "name": "Connor Durkin",
                "age": 31,
                "city": "Jersey City",
                "is_student": true
            }

            TEST ONE RESULT: 
            
            o.name = "Connor Durkin"
            o.age = "31"
            o.city = "Jersey City"
            o.is_student = "True"
                

        ===Test Two===
        
            python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/gron.py --obj o /Users/cdurkin/Desktop/test.json

        
            {
              "name": "Connor Durkin",
              "age": 31,
              "Address": {
                "City": "Jersey City",
                "State": "New Jersey",
                "Zip": 7307
              },
              "isStudent": true
            }

            Test Two Result: 
        
            o.name = "Connor Durkin"
            o.age = "31"
            o.Address.City = "Jersey City"
            o.Address.State = "New Jersey"
            o.Address.Zip = "7307"
            o.isStudent = "True"

        ===Test Three===
        
            python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/gron.py --obj o /Users/cdurkin/Desktop/test.json

            
            {
              "Connor Durkin": ["31", "Jersey City, NJ, 07307", "Student"],
              "Jane Doe": ["25", "Hoboken, NJ, 07030", "Student"]
            }
        
            Test Three Result:
            
            o.Connor Durkin[0] = "31"
            o.Connor Durkin[1] = "Jersey City, NJ, 07307"
            o.Connor Durkin[2] = "Student"
            o.Jane Doe[0] = "25"
            o.Jane Doe[1] = "Hoboken, NJ, 07030"
            o.Jane Doe[2] = "Student"

        ==Test Four===
        
            python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/gron.py --obj o /Users/cdurkin/Desktop/test.json

            {
              "name": null,
              "address": null,
              "isStudent": null
            }

            Test Four Result:
        
            o.name = "None"
            o.address = "None"
            o.isStudent = "None"

        ===Test Five===
            
            python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/gron.py --obj o /Users/cdurkin/Desktop/test.json
            
            {}
        
            Test Five Result: 
            
            o: Empty JSON

    EXTENSION TESTS (STD IN)
    
        ===Test One===
        
            python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/gron.py --obj o '{"name": "Connor Durkin", "age": 31, "city": "Jersey City", "is_student": true}'
            
            Test One Result: 
            
            o.name = "Connor Durkin"
            o.age = "31"
            o.city = "Jersey City"
            o.is_student = "True"
                                    
            
        ===Test Two===
        
            python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/gron.py --obj o '{"name": "Connor Durkin", "age": 31, "Address": {"City": "Jersey City", "State": "New Jersey", "Zip": 7307}, "isStudent": true}'
            
            Test Two Result:
             
            o.name = "Connor Durkin"
            o.age = "31"
            o.Address.City = "Jersey City"
            o.Address.State = "New Jersey"
            o.Address.Zip = "7307"
            o.isStudent = "True"
            
        
        ===Test Three===
        
            python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/gron.py --obj o '{"Connor Durkin": ["31", "Jersey City, NJ, 07307", "Student"], "Jane Doe": ["25", "Hoboken, NJ, 07030", "Student"]}'
       
            Test Three Result: 
            
                o.Connor Durkin[0] = "31"
                o.Connor Durkin[1] = "Jersey City, NJ, 07307"
                o.Connor Durkin[2] = "Student"
                o.Jane Doe[0] = "25"
                o.Jane Doe[1] = "Hoboken, NJ, 07030"
                o.Jane Doe[2] = "Student"
                       
        ===Test Four===
        
            python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/gron.py --obj o '{"name": null, "address": null, "isStudent": null}'

            Test Four Result: 
            
            o.name = "None"
            o.address = "None"
            o.isStudent = "None"

        ===Test Five===
        
            python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/gron.py --obj o '{}'
            
            Test Five Result:
            
            json: Empty JSON

WC TESTS

    INPUT FILE (test.txt) TESTS
       
        ===Test One===
        
            wc_testone.txt:
        
            python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/wc.py <<< 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.
            Duis aute irure dolor in reprehenderit in voluptate velit esse.
            Cupidatat non proident, sunt in culpa qui officia deserunt mollit.'

    
            Test One Result:
        
            5    49    274    

        
        ===Test Two===
        
            wc_testtwo.txt:
        
            123 456 789
            10 20 30
            40 50 60
            
            Test One Result:
        
            3    9    21    /Users/cdurkin/Desktop/WC_Tests/wc_testtwo.txt


        ===Test Three===
            
            wc_testthree.txt: 

            A

            123 456 789
            10 20 30
            40 50 60


            As

            V
        
            Test Three Result:
            
            12    12    25    /Users/cdurkin/Desktop/WC_Tests/wc_testthree.txt


        ==Test Four===
        
            wc_testfour.txt:  
            
            (EMPTY TXT FILE)

            Test Four Result:
        
            0    0    0    /Users/cdurkin/Desktop/WC_Tests/wc_testfour.txt
            
        ===Test Five===
            
            wc_testfive.txt:  

            $%^&*((*&^
            *&^%$%^&*(
            )(*&
            )(*&^%
        
            Test Five Result: 
            
            5    4    30    /Users/cdurkin/Desktop/WC_Tests/wc_testfive.txt

    EXTENSION: MULTIPLE INPUT FILES
       
        ===Test One===
        
            Command: $ /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/wc.py Users/cdurkin/Desktop/WC_Tests/wc_testtwo.txt /Users/cdurkin/Desktop/WC_Tests/wc_testthree.txt
            
            
            Test One Result:
        
            3    9    21    /Users/cdurkin/Desktop/WC_Tests/wc_testtwo.txt
            12   12   25    /Users/cdurkin/Desktop/WC_Tests/wc_testthree.txt
        
        ===Test Two===
        
            $ python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/wc.py /Users/cdurkin/Desktop/WC_Tests/wc_testtwo.txt /Users/cdurkin/Desktop/WC_Tests/wc_testthree.txt /Users/cdurkin/Desktop/WC_Tests/wc_testfour.txt

            Test Two Result:

            3    9    21    /Users/cdurkin/Desktop/WC_Tests/wc_testtwo.txt
            12    12    25  /Users/cdurkin/Desktop/WC_Tests/wc_testthree.txt
            0    0    0     /Users/cdurkin/Desktop/WC_Tests/wc_testfour.txt
        

        ===Test Three===
            
            python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/wc.py /Users/cdurkin/Desktop/WC_Tests/wc_testtwo.txt /Users/cdurkin/Desktop/WC_Tests/wc_testtwo.txt /Users/cdurkin/Desktop/WC_Tests/wc_testtwo.txt
        
            Test Three Result:
            
            3    9    21    /Users/cdurkin/Desktop/WC_Tests/wc_testtwo.txt

            *Explanation: As a dictionary is used, only unique file names and values are printed. 
            
    EXTENSION: FLAGS
       
        ===Test One===
        
            Command: $ python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/wc.py -l /Users/cdurkin/Desktop/WC_Tests/wc_testone.txt 
           
            Result: 
            
            5    /Users/cdurkin/Desktop/WC_Tests/wc_testone.txt
            
            
        ===Test Two===
        
            Command: $ python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/wc.py -lw /Users/cdurkin/Desktop/WC_Tests/wc_testtwo.txt
            
            Result:
            
            3    9    /Users/cdurkin/Desktop/WC_Tests/wc_testtwo.txt

        ===Test Three===
        
            Command: $ python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/wc.py -lwc /Users/cdurkin/Desktop/WC_Tests/wc_testthree.txt
            
            Result:
            
            12    12    25    /Users/cdurkin/Desktop/WC_Tests/wc_testthree.txt
            
        ===Test Four===
        
            Command: $ python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/wc.py -lw /Users/cdurkin/Desktop/WC_Tests/wc_testthree.txt /Users/cdurkin/Desktop/WC_Tests/wc_testtwo.txt
            
            Result:
            
            12    12    /Users/cdurkin/Desktop/WC_Tests/wc_testthree.txt
            3    9    /Users/cdurkin/Desktop/WC_Tests/wc_testtwo.txt
            
        ===Test Five===
        
            Command: python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/wc.py -w /Users/cdurkin/Desktop/WC_Tests/wc_testfour.txt 
            
            Result: 
            0    /Users/cdurkin/Desktop/WC_Tests/wc_testfour.txt

    STD IN TESTS

        ===Test One===
        
            Command: python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/wc.py <<<'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.
            Duis aute irure dolor in reprehenderit in voluptate velit esse.
            Cupidatat non proident, sunt in culpa qui officia deserunt mollit.'

            
            Test One Result:
        
            4    41    225    /Users/cdurkin/Desktop/WC_Tests/wc_testone.txt

        
        ===Test Two===
            
            Command: python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/wc.py <<<''
            
            Test One Result:
        
            1    0    0    /Users/cdurkin/Desktop/WC_Tests/wc_testtwo.txt


        ===Test Three===
            
            Command: python3 /Users/cdurkin/Desktop/Durkin_515_ProjectOne/prog/wc.py <<<'123 456 789
            10 20 30
            40 50 60'

            Test Three Result:
            
            3    9    21    /Users/cdurkin/Desktop/WC_Tests/wc_testthree.txt

CSVSUM TESTS

    INPUT FILE (test.csv) TESTS

        ===Test One===
        
            Sum for Column 1
            
            testone.csv:
            
            1
            1
            1
            1
            1
            1
            1
            1
            1
            1
            
            RESULT: 
            
            Column: 1; Sum: 9.0
            Total sum of all columns: 9.0
        
        ===Test Two===
        
            Sum for column One
            
            testtwo.csv:
            
            One
            1
            1
            1
            1
            1
            1
            1
            1
            1
            
            RESULT: 
            Column: One; Sum: 9.0
            Total sum of all columns: 9.0

        ===TEST THREE===
        
            Sum for column 1 and 2 
            
            testthree.csv:
        
            1    2
            1    2
            1    2
            1    2
            1    2
            1    2
            1    2
            1    2
            1    2
            1    2
            
            RESULT:
            Column: 1; Sum: 9.0
            Column: 2; Sum: 18.0
            Total sum of all columns: 27.0

        ===TEST Four===
        
            Sum for column One and 2 
            
            testfour.csv:
        
            One  2
            1    2
            1    2
            1    2
            1    2
            1    2
            1    2
            1    2
            1    2
            1    2
            
            RESULT:
            Column: One; Sum: 9.0
            Column: 2; Sum: 18.0
            Total sum of all columns: 27.0
            
        ===TEST Five===
        
            Sum for column 1
            
            testfive.csv:
        
            (EMPTY CSV)
            
            RESULT:
            CSV File is empty.
