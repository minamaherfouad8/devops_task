#!/usr/bin/env python3
import sys
import re

# Simple regex for FQDN emails (requires a TLD like .com, .org, etc., rejecting localhost)
EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def process_users(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.", file=sys.stderr)
        sys.exit(1)

    for index, line in enumerate(lines):
        line = line.strip()
        # Skip empty lines or the header row
        if not line or line.lower().startswith("name,"):
            continue

        # Split by comma and strip whitespaces from each element
        parts = [part.strip() for part in line.split(',')]
        
        # Ensure we have at least name, email, and id fields
        if len(parts) < 3:
            name = parts[0] if len(parts) > 0 else f"Line {index+1}"
            print(f"Warning: {name} has missing parameters (ID or Email is absent).", file=sys.stderr)
            continue

        name, email, user_id = parts[0], parts[1], parts[2]

        # 1. Validate Email (Must exist and be a routable FQDN)
        if not email or not re.match(EMAIL_REGEX, email):
            print(f"Warning: {name} has an invalid or non-routable email address ('{email}').", file=sys.stderr)
            continue

        # 2. Validate User ID (Must exist and be a positive integer)
        if not user_id or not user_id.isdigit():
            print(f"Warning: {name} has an invalid or missing user ID ('{user_id}').", file=sys.stderr)
            continue

        # 3. Determine if odd or even
        id_num = int(user_id)
        parity = "even" if id_num % 2 == 0 else "odd"

        # 4. Print valid output
        print(f"The {id_num} of {email} is {parity} number.")

if __name__ == "__main__":
   
        
    process_users(sys.argv[0])
