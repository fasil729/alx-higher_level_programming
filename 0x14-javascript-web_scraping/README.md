## Task 0: File Reader

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

# Task 5: Loripsum

This is a Node.js script that gets the contents of a webpage and stores it in a file.

## Usage

To use this script, run the following command in the terminal:

```
./5-request_store.js <url> <file-path>
```

Where `<url>` is the URL of the webpage to request and `<file-path>` is the file path to store the response.

Example:

```
./5-request_store.js http://loripsum.net/api loripsum
```

Output:

```
<contents of the webpage>

```

If an error occurs while making the request or writing to the file system, the error object will be printed to the console.

## Notes

- The file must be UTF-8 encoded.
- The `request()` function is used to make the HTTP request.
- The `fs.writeFile()` function is used to write the response to the file system.


# Task 6: Compute the Number of Completed Tasks by User ID

This script computes the number of completed tasks by user id using the [request ↗](https://www.npmjs.com/package/request) module in Node.js. It takes the API URL as a command line argument and outputs a JSON object showing the number of completed tasks for each user id where at least one task was completed.

To run the script, save it to a file (e.g. `6-completed_tasks.js`), make it executable (`chmod +x 6-completed_tasks.js`), and run it with the API URL as the first argument:

```
./6-completed_tasks.js <API_URL>
```

For example:

```
./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
```

This should output a JSON object showing the number of completed tasks for each user id where at least one task was completed.

Apologies for the confusion. Here's the prompt for Task 7:

## Task 7: Print Characters of a Star Wars Movie

Write a script that prints all characters of a Star Wars movie:

- The first argument is the Movie ID - example: 3 = "Return of the Jedi"
- Display one character name by line
- You must use the Star Wars API
- You must use the module `request`

Example:

```
$ ./100-starwars_characters.js 3
Darth Vader
R2-D2
Luke Skywalker
Han Solo
Leia Organa
Chewbacca
Palpatine
Obi-Wan Kenobi
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Boba Fett
Ackbar
Arvel Crynyd
Mon Mothma
Nien Nunb
Wicket Systri Warrick
Bib Fortuna
C-3PO
Lando Calrissian
```

Note: The output above is just an example. The characters you get depend on the movie ID you passed as argument.

## Task 8: Print Characters of a Star Wars Movie in the Right Order

This script prints all characters of a Star Wars movie using the Star Wars API, in the order of the list "characters" in the /films/ response. The movie ID is taken as a command line argument, and the character names are output one per line.
