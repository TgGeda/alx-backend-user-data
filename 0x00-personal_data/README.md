# personal data

Logging and Data Filtering

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [Tasks](#tasks)
  - [Task 0: Regex-ing](#task-0-regex-ing)
  - [Task 1: Log Formatter](#task-1-log-formatter)
  - [Task 2: Create Logger](#task-2-create-logger)
  - [Task 3: Connect to Secure Database](#task-3-connect-to-secure-database)
  - [Task 4: Read and Filter Data](#task-4-read-and-filter-data)
  - [Task 5: Encrypting Passwords](#task-5-encrypting-passwords)
  - [Task 6: Check Valid Password](#task-6-check-valid-password)
- [Contributing](#contributing)
- [License](#license)

## Project Description

This project focuses on logging and data filtering techniques. It involves tasks such as obfuscating sensitive information, creating customized log formatters, connecting to secure databases, reading and filtering data, encrypting passwords, and validating passwords.

The project provides a set of functions, classes, and code snippets to accomplish these tasks efficiently. Each task is described in detail below, along with implementation instructions.

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies listed in the `requirements.txt` file.
3. Set up the necessary environment variables for secure database connection.

## Usage

To use this project, follow the steps below:

1. Import the required modules and classes into your Python script.
2. Configure the necessary settings and credentials for logging and database connections.
3. Implement the specific functions or classes according to your requirements.
4. Run your script and observe the output or perform the desired operations.

## Tasks

This project consists of the following tasks:

### Task 0: Regex-ing

In this task, you need to implement a function called `filter_datum` that obfuscates sensitive information in log messages using regular expressions. The function takes a list of fields to obfuscate, a redaction string, a log message, and a separator character. It replaces occurrences of the specified field values with the redaction string using regular expression substitution.

### Task 1: Log Formatter

This task involves creating a customized log formatter class called `RedactingFormatter`. It inherits from the `logging.Formatter` class and provides a redacted format for log records. The `RedactingFormatter` accepts a list of fields constructor argument, which determines the sensitive fields to be filtered. The format method of the class filters the values in log records using the `filter_datum` function implemented in Task 0.

### Task 2: Create Logger

In this task, you need to implement a function called `get_logger` that creates a logger object for logging user data. The logger is named "user_data" and logs messages up to the `logging.INFO` level. It does not propagate messages to other loggers. The logger is configured with a `StreamHandler` and uses the `RedactingFormatter` from Task 1 as the formatter. The `PII_FIELDS` constant, containing a list of fields considered personally identifiable information (PII), is used to parameterize the formatter.

### Task 3: Connect to Secure Database

This task involves implementing a function called `get_db` that connects to a secure database using the credentials stored as environment variables. The function retrieves the database credentials from the environment variables `PERSONAL_DATA_DB_USERNAME`, `PERSONAL_DATA_DB_PASSWORD`, `PERSONAL_DATA_DB_HOST`, and `PERSONAL_DATA_DB_NAME`. It uses the `mysql-connector-python` module to establish a connection to the MySQL database.

### Task 4: Read and Filter Data

In this task, you need to implement a `main` function that retrieves data from a database table and logs it using the logger created in Task 2. The function obtains a database connection using the `get_db` function from Task 3. It retrieves all rows from the "users" table and formats each row in a filtered format using the `RedactingFormatter` from Task 1. The filtered data is logged with the logger.

### Task 5: Encrypting Passwords

This task involves implementing a function called `hash_password` that securely hashes a password using the `bcrypt` package. The function takes a password as input and returns a salted, hashed password as a byte string. The `bcrypt.hashpw` function is used for performing the hashing.

### Task 6: Check Valid Password

In this task, you need to implement a function called `is_valid` that checks whether a provided password matches a hashed password. The function takes a hashed password (as a byte string) and a password (as a string) as input and returns a boolean indicating whether the password is valid. The `bcrypt.checkpw` functionis used to compare the hashed password with the provided password.

## Contributing

Contributions to this project are welcome. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make the necessary changes and ensure that the code passes all tests.
4. Write clear and concise commit messages.
5. Submit a pull request, describing the changes you have made and explaining their purpose.

Please adhere to the project's code style and follow the guidelines for contributing.

## License

This project is licensed under the [MIT License](LICENSE). You are free to modify and distribute the code as per the terms of the license.
