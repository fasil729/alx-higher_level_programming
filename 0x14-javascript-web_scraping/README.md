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
