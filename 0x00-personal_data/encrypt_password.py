#!/usr/bin/env python3

"""
Defines functions for hashing passwords and checking their validity using bcrypt.
"""

import bcrypt

def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt.

    Args:
        password (str): The password to be hashed.

    Returns:
        bytes: The hashed password.
    """

    # Encode the password as bytes
    password_bytes = password.encode()

    # Generate a salt for hashing
    salt = bcrypt.gensalt(rounds=12)  # Higher rounds value for stronger security

    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    # Return the hashed password
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks whether a password matches a hashed password.

    Args:
        hashed_password (bytes): The hashed password.
        password (str): The plain text password to be checked.

    Returns:
        bool: True if the passwords match, False otherwise.
    """

    # Encode the plain text password as bytes
    password_bytes = password.encode()

    # Check if the hashed password matches the provided password
    is_valid_password = bcrypt.checkpw(password_bytes, hashed_password)

    # Return the result of the password check
    return is_valid_password
