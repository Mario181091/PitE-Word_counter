# Word_Counter

This project is a personal version of famouse Linux "wc" command, that can be used to provide a total of the number of row,        total of the number of words and total of the number of character which are in a input text. 

## Getting Started
See a basic explenation of word_count works

**Prerequisites**
* For run this project is important to have python version 3 or upper
  Install it with:
  ```
   $ sudo apt-get install python3
  ```
  now check your version: 
  ```
  $ python --version
  ```

**Basic usage**
* See basic usage of word_count; this project is develope to emulate Linux "wc", so the functionalities are the same of it.
  The syntax of word counter is the follow:
  ```
   $ python3 word_counter.py <Your_File> -option
  ```
  
 * It is possible to count total number of row in file, add option "-r" 
   ```
   $ python3 word_counter.py <Your_File> -r 
   ```
   
 * It is possible to count total number of word in file, add option "-w" 
   ```
   $ python3 word_counter.py <Your_File> -w 
   ```
   
 * It is possible to count total number of character in file, with option "-c" 
   ```
   $ python3 word_counter.py <Your_File> -c 
   ```
  
 * It is possible to compute at same time all statistic, without option 
   ```
   $ python3 word_counter.py <Your_File> 
   ```
   
 * It is possible compute the input text that user insert by keyboard, if no file is specified
   ```
   $ python3 word_counter.py
   ```

## Results
Personal word counter have good performance also with large file. 
* output of test with file almost 2GB, with computional time:
   ```
   (18997956, 246973425, 1196871213)
   
   real	0m18.464s
   user	0m17.980s
   sys	0m0.456s

   ```
## Authors

* **Mario Egidio Carricato** - *Erasmus student AGH* - 
