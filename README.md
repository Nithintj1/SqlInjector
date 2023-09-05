# SQL Injection Scanner

This is a simple Python script for testing SQL injection vulnerabilities in a web application. It takes a target URL with a parameter vulnerable to SQL injection and checks it with a set of predefined payloads.

## Usage

1. **Prerequisites**:
   - Python 3.x installed
   - Install the required libraries by running: `pip install -r requirements.txt`

2. **Run the Scanner**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the `sql_injection_scanner.py` script.
   - Run the script by executing: `python sql_injection_scanner.py`
   - You will be prompted to enter the target URL, including the vulnerable parameter.

3. **Results**:
   - The script will test the target URL with a set of SQL injection payloads.
   - If it detects a potential SQL injection vulnerability, it will print a message indicating the payload that triggered it.

4. **Ethical Considerations**:
   - Ensure you have proper authorization before scanning a website for vulnerabilities. Unauthorized scanning can be illegal and unethical.

## Example

Here's an example of how to use the script:

```shell
$ python sql_injection_scanner.py
Enter the target URL (e.g., http://example.com/vulnerable.php?id=): http://example.com/vulnerable.php?id=
Potential SQL Injection detected with payload: 1' OR '1'='1
Potential SQL Injection detected with payload: 1' OR '1'='1' --
