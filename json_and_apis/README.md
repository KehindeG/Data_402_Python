# JSON and APIs


## JSON
 
#### What does it stand for?
JavaScript Object Notation.
It's a standardized way to represent data. 

#### What is it used for?
JSON is often used to transmit data between a server and a web application, 
but it's also used as a data storage and communication format in many programming 
languages beyond JavaScript.

#### What is it written in?
It is a language-independent data format, so it isn't "written" in any particular 
programming language. 
JSON can be generated and parsed by virtually any programming language since it's 
based on simple text.

#### What data types can it store/use?
* Strings
* Numbers
* Booleans
* Arrays
* Objects
* Null

JSON is built on two structures:<br>
* A collection of key/value pairs. (In various programming languages, this is 
        realized as an object, record, struct, dictionary, hash table, keyed list, or 
        associative array.)<br>
* An ordered list of values. (In most programming languages, this is realized as 
        an array, vector, list, or sequence.)



#### What is the JSON syntax for:
* Name value pairs?
  - Name/value pairs are represented by strings as keys and values separated by a colon. Each pair is separated by a comma.<br>
  ```
   For example: 
  
  {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
  }
  ```
* Objects?
  - Objects are enclosed in curly brackets like this:  `{ } `
  - A JSON object contains zero, one, or more key-value pairs.

* How to separate data objects from one another?
  - In JSON, you separate data objects from one another using commas. Each data object, 
  whether it's an array or an object, is separated by a comma.
* JSON arrays (these are like lists in python)?