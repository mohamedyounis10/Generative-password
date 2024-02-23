## Random Password Generator

This Python script generates a random password based on user input and certain criteria. Below is a brief overview of how it works:

### Requirements
- Python 3.x

### How to Use
1. Run the script.
2. Enter the desired number of characters for your password when prompted.
3. The script ensures that the password has at least 8 characters, prompting the user to input again if the specified length is less than 8.
4. The script generates a password using a combination of lowercase letters, uppercase letters, digits, and punctuation.
5. The generated password is displayed to the user.

### Description
- The script imports the `string` and `random` modules to utilize pre-defined character sets and shuffle functions.
- It prompts the user to input the desired length of the password.
- Error handling is implemented to ensure that only numerical inputs are accepted, and the password length is at least 8 characters.
- The script shuffles each character set to ensure randomness.
- The password is constructed by selecting characters from each set according to predefined proportions.
- Finally, the password is displayed to the user.

### Example
```
$ python password_generator.py
How many characters do you want for your password?: 12
sx;DfGh3jI4L
```
