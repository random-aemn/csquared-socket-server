# Program to generate geo-located ship position data using web sockets.

## Assumptions:
- The program will use two files to generate the data:
  -   The first is the header file containing the comma separated values used for generation the JSON keys.
  -   The second file contains the CSV data
  -   It is **essential** to keep the structure of the two files synchronized or the pogram will not work.
 
## Best Practices
Name the header file and data file using the same file prefix.  
e.g. - Name the data file ```rachel-thin.csv``` and the header file ```rachel-thin-header.csv```
When invoking the program, supply a command line argument of ```rachel-thin``` and the code will append the necessary text
to the header file and data file to create both ```rachel-thin-headers.csv``` and ```rachel-thin.csv``` for the header file
and data file respectively.

## Imports
```pip install aiofiles```

## Invoke the program as follows:
```python server.py ./data/rachel-thin```


## [AIS Data Dictionary](https://github.com/random-aemn/csquared-socket-server/blob/main/ais-dat-dictionary.md)

