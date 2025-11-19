Password Generator

Cryptographically secure password generator written in Python.
Uses the secrets module (not the weak random module).
Guarantees at least one uppercase, one lowercase, one digit, and one symbol.
Excludes confusing characters (lI1oO0) by default.
Full CLI support + optional clipboard copy.

Usage
./password_generator.py [-l LENGTH] [--no-symbols] [--allow-ambiguous] [--copy]

Options
-l N      --length N        Password length, default 20
          --no-symbols      Don't include special characters
          --allow-ambiguous Include lI1oO0 characters
          --copy            Copy password to clipboard (needs pyperclip)

Clipboard support (optional)
pip install pyperclip

No more password123. Ever.

Made with paranoia.
