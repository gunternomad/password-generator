#!/usr/bin/env python3
import secrets
import string
import argparse
import pyperclip  # optional, for auto-copy

def generate_password(length=20,
                      include_symbols=True,
                      exclude_ambiguous=True):
    """
    Generate a cryptographically secure random password
    """
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = r'!@#$%^&*()_+-=[]{}|;:,.<>?'

    # Remove ambiguous characters if requested (lI1oO0 etc.)
    if exclude_ambiguous:
        ambiguous = 'lI1oO0'
        lowercase = ''.join(c for c in lowercase if c not in ambiguous)
        uppercase = ''.join(c for c in uppercase if c not in ambiguous)
        digits = ''.join(c for c in digits if c not in ambiguous)

    # Build the character pool
    pool = lowercase + uppercase + digits
    if include_symbols:
        pool += symbols

    # Ensure at least one of each required type
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits)
    ]
    if include_symbols:
        password.append(secrets.choice(symbols))

    # Fill the rest
    password += [secrets.choice(pool) for _ in range(length - len(password))]

    # Shuffle it
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)


def main():
    parser = argparse.ArgumentParser(description="Ultra-secure password generator")
    parser.add_argument("-l", "--length", type=int, default=20, help="Password length (default: 20)")
    parser.add_argument("--no-symbols", action="store_false", dest="symbols", help="Exclude symbols")
    parser.add_argument("--allow-ambiguous", action="store_false", dest="no_ambiguous", help="Allow lI1oO0")
    parser.add_argument("--copy", action="store_true", help="Copy to clipboard (requires pyperclip)")

    args = parser.parse_args()

    pwd = generate_password(
        length=args.length,
        include_symbols=args.symbols,
        exclude_ambiguous=args.no_ambiguous
    )

    print(pwd)

    if args.copy:
        try:
            pyperclip.copy(pwd)
            print("Copied to clipboard!")
        except ImportError:
            print("Install pyperclip to use --copy")
        except:
            print("Failed to copy to clipboard")


if __name__ == "__main__":
    main()