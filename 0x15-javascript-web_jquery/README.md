# Updating HTML Element Style with Vanilla JavaScript

This is a simple JavaScript script that updates the text color of the `<header>` element to red (#FF0000) without using jQuery. 

## General Requirements

* Allowed editors: vi, vim, emacs
* All files will be interpreted on Chrome (version 57.0)
* All files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should be semistandard compliant with the flag `--global $: semistandard *.js --global $`
* You are not allowed to use `var`
* HTML should not reload for each action: DOM manipulation, update values, fetch data…

## How to Use

To use this script, follow these steps:

1. Create a new file called `0-script.js` in your project directory.
2. Copy the script from this repository and paste it into `0-script.js`.
3. Create a new HTML file called `index.html` in your project directory.
4. Add the following code to your `index.html` file:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>My Website</title>
  </head>
  <body>
    <header> 
      My Header
    </header>
    <footer>
      My Footer
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
```
5. Open `index.html` in your web browser.
6. The text color of the `<header>` element should now be red.

## Explanation

The script uses `document.querySelector()` to select the `<header>` element, and then sets its `style.color` property to '#FF0000', which is red. The use of `const` instead of `var` is in compliance with the requirements, and ensures that the `header` variable cannot be reassigned.

## Author

Fasika Fikadu