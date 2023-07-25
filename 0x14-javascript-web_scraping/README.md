k 0: File Reader

This is a Node.js script that reads and prints the content of a file. 

## Usage
To use the script, run the following command in the terminal:

```
./0-readme.js <file-path>
```

Where `<file-path>` is the path to the file you want to read. The content of the file will be printed to the console.

If an error occurs during the reading process, the error object will be printed to the console.

## Requirements
- Node.js version 10.14.x or higher
- All files must be executable
- Semistandard compliant code with rules of Standard + semicolons on top
- The first line of all files must be exactly `#!/usr/bin/node`
- All files must end with a new line
- A `README.md` file at the root of the project directory

## Example
Here's an example of running the script on a file called "cisfun":

```
$ cat cisfun
C is super fun!

$ ./0-readme.js cisfun
C is super fun!
```

If the file does not exist or an error occurs during the reading process, the error object will be printed to the console. For example:

```
$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
```

# Task 1: File Writer

This is a Node.js script that writes a string to a file. It takes two arguments, which are the file path and the string to write.

## Usage

To use this script, run the following command in the terminal:

```
./1-writeme.js <file-path> "<string-to-write>"
```

Where `<file-path>` is the path to the file you want to write to and `<string-to-write>` is the string you want to write.

Example:

```
./1-writeme.js my_file.txt "Python is cool"
```

Output:

```
The file "my_file.txt" has been saved.
```

If an error occurs while writing to the file, the error object will be printed to the console.

## Note

- Make sure that the file path and the string to write are enclosed in quotes if they contain spaces.
- All files must be executable.

# Task 2: Status Code

This is a Node.js script that displays the status code of a GET request. It takes one argument, which is the URL to request.

## Usage

To use this script, run the following command in the terminal:

```
./2-statuscode.js <url>
```

Where `<url>` is the URL to request.

Example:

```
./2-statuscode.js https://alx-intranet.hbtn.io/status
```

Output:

```
code: 200
```

If an error occurs while making the request, the error object will be printed to the console.

## Note

- Make sure to include the `http://` or `https://` protocol in the URL.
- All files must be executable.

# Task 3: Star Wars Movie Title

This is a Node.js script that prints the title of a Star Wars movie where the episode number matches a given integer. It takes one argument, which is the movie ID.

## Usage

To use this script, run the following command in the terminal:

```
./3-starwars_title.js <movie-id>
```

Where `<movie-id>` is the ID of the movie whose title you want to retrieve.

Example:

```
./3-starwars_title.js 1
```

Output:

```
A New Hope
```

If an error occurs while making the request, the error object will be printed to the console.

## Note

- The Star Wars API is used to retrieve movie data. Make sure you have an internet connection when running this script.
- All files must be executable.

# Task 4: Star Wars Wedge Antilles

This is a Node.js script that prints the number of movies where the character "Wedge Antilles" is present. It takes one argument, which is the API URL of the Star Wars API films endpoint.

## Usage

To use this script, run the following command in the terminal:

```
./4-starwars_count.js <api-url>
```

Where `<api-url>` is the URL of the Star Wars API films endpoint.

Example:

```
./4-starwars_count.js https://swapi-api.alx-tools.com/api/films
```

Output:

```
3
```

If an error occurs while making the request, the error object will be printed to the console.

## Note

- The character ID for "Wedge Antilles" is hard-coded to 18.
- The script uses the `reduce()` method to count the number of movies where "Wedge Antilles" is present.
- All files must be executable.


