# Secure ATM System

A fully secured ATM system implemented in Python with user authentication and encrypted PIN storage.

## Features
- Secure user authentication with SHA-256 hashed PINs.
- Balance inquiry, deposit, and withdrawal functionalities.
- User-friendly console interface.
- Secure password input using `getpass.getpass()`.
- Persistent data storage using JSON.

## Requirements
- Python 3.x

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/secure-atm.git
   cd secure-atm
   ```
2. Run the script:
   ```sh
   python secure_atm.py
   ```

## Usage
1. Register a new account.
2. Log in using your account number and PIN.
3. Choose from available options:
   - Check balance
   - Deposit money
   - Withdraw money
   - Logout

## File Structure
```
secure-atm/
│-- secure_atm.py  # Main script
│-- users.json      # Stores user data securely
│-- README.md       # Documentation
```

## Security Considerations
- PINs are hashed using SHA-256 for secure storage.
- User inputs are protected using `getpass.getpass()` to prevent shoulder surfing.

## Contributing
Feel free to fork this repository and submit pull requests with improvements!

## License
This project is licensed under the MIT License.
