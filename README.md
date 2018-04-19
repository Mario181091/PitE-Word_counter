# Word_Counter
[![Build Status](https://travis-ci.org/Mario181091/PitE-Word_counter.svg?branch=master)](https://travis-ci.org/Mario181091/PitE-Word_counter)          [![Coverage Status](https://coveralls.io/repos/github/Mario181091/PitE-Word_counter/badge.svg?branch=master&service=Github)](https://coveralls.io/github/Mario181091/PitE-Word_counter?branch=master&service=Github)   [![HitCount](http://hits.dwyl.io/Mario181091/PitE-Word_counter.svg)](http://hits.dwyl.io/Mario181091/PitE-Word_counter)

This is the first homework of the course "Python in the Enterprise", as requested is implemented a personal version of famous Linux "wc" command, that can be used to provide a total of the number of row,        total of the number of words and total of the number of character which are in a input text. 

## Getting Started

**Prerequisites**
* In order to run this project is important to use python version 3 or upper.                                                    
  Install it with:
  ```
   $ sudo apt-get install python3
  ```
  now check your version: 
  ```
  $ python --version
  ```


**Basic usage**
* This project is developed to emulate Linux "wc" ([Linux Word Counter](https://en.wikipedia.org/wiki/Wc_(Unix)))    
  The syntax of word counter is the follow:
  ```
   $ python3 wc.py <Your_File> -option
  ```
  
 * It is possible to count total number of row in file, adding option "-r" 
   ```
   $ python3 wc.py <Your_File> -r 
   ```
   
 * It is possible to count total number of word in file, adding option "-w" 
   ```
   $ python3 wc.py <Your_File> -w 
   ```
   
 * It is possible to count total number of character in file, adding option "-c" 
   ```
   $ python3 wc.py <Your_File> -c 
   ```
  
 * It is possible to compute at same time all statistic, without options 
   ```
   $ python3 wc.py <Your_File> 
   ```
     
 * It is possible to compute the input text that user insert by keyboard, if no text file is specified
   ```
   $ python3 wc.py
   ```

## Results
Personal word counter reveals good performance also with quite large file. 
* output of computation with file almost 2GB

   ```
   (18997956, 246973425, 1196871213)
   
   real	0m18.464s
   user	0m17.980s
   sys	0m0.456s

   ```
## Authors

* **Mario Egidio Carricato** - *Erasmus student AGH* - [other projects](https://github.com/mario181091)
