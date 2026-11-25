# PassGuard

A command-line Python tool that rates how strong a password is (Weak, Medium or Strong) and gives specific tips to improve it.

## Legal & Ethical Note

Scanning or attacking systems you do not own or do not have written permission to test is illegal. This project only runs on my own machine and only checks passwords that I type in myself. Never use it, or any security tool, against other people's accounts or systems.

## Features

- Checks password length (8, 12 and 16+ characters)
- Checks for lowercase letters, uppercase letters, digits and symbols
- Gives a clear tip for every missing rule
- Compares against a list of common passwords and flags them as Weak immediately
- Catches small variations of common passwords (for example `Password1!`)
- Uses `getpass`, so the password is hidden while typing
- Never prints or saves the password. Only the rating and tips are shown

## Requirements

- Python 3.8 or newer
- No extra libraries needed (uses only the Python standard library)

## How to Run

1. Download or clone this repository
2. Open a terminal in the project folder
3. Run:

```
python passguard.py
```

4. Type a password (nothing appears on screen while you type, this is intentional) and press Enter
5. Press Enter on an empty line to quit

## Example Results

| Password tested | Rating |
|---|---|
| `abc123` | Weak |
| `Password1!` | Weak (common password variation) |
| `Tr33-House-Blue-Mango` | Strong |

## How It Works

Each rule is its own small function that returns points:

- `check_length(pw)`: 0 to 3 points depending on length
- `check_lowercase(pw)`, `check_uppercase(pw)`, `check_digit(pw)`, `check_symbol(pw)`: 1 point each
- `is_common(pw, common)`: checks the common-password list
- `rate_password(pw, common)`: adds the points (maximum 7) and maps the total to Weak, Medium or Strong

## Known Limitations

- This is a rule-based checker. It counts character types and length, it does not measure how guessable a password really is.
- A password like `Aaaaaaaa1!aaaaaaaa` can score Strong even though it is repetitive and weak.
- The common-password list is small (25 entries). A real tool would use a much larger list.
- Real-world tools such as zxcvbn estimate guessability instead of counting rules.

## Project Files

```
passguard/
├── passguard.py
├── common_passwords.txt
└── README.md
```

## What I Learned

- What makes passwords weak: short length, low variety and predictability
- Python strings, conditions and functions
- Reading input safely with `getpass`
- The legal and ethical rules around security testing

## Author

saadmode
