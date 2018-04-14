# Word_Counter

This project is a personal version of famouse Linux "wc" command, that can be used to provide a total of the number of row,        total of the number of words and total of the number of character which are in a input text. 

## Getting Started
See a basic explenation of word_count works

### Prerequisites

4. And another item.

⋅⋅⋅You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).

⋅⋅⋅To have a line break without a paragraph, you will need to use two trailing spaces.⋅⋅
⋅⋅⋅Note that this line is separate, but within the same paragraph.⋅⋅
⋅⋅⋅(This is contrary to the typical GFM line break behaviour, where

For run this project you need to install python version 3
```
$ sudo apt-get install python3
```
After istallation check your python version 
```
$ python --version
```

This program reply the basic usage of linux "wc" command, the syntax that must be used is the follow: 
```
$ python3 word_counter.py <Your_File> -option
```
   + It is possible to count total number of row in file, with option "-r" 
  ```
  $ python3 word_counter.py <Your_File> -r 
  ```
   
   + It is possible to count total number of word in file, with option "-w" 
  ```
  $ python3 word_counter.py <Your_File> -w 
  ```
   
   + It is possible to count total number of character in file, with option "-c" 
  ```
  $ python3 word_counter.py <Your_File> -c 
  ```
  
   + It is possible to count at same time all statistic, without option 
  ```
  $ python3 word_counter.py <Your_File> 
  ```
   
   + Like Linux "wc" it is possible compute the input text that user insert by keyboard, if we don't specifies any file 
  ```
  $ python3 word_counter.py
  ```



## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc

