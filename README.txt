Music App
This Python script implements a simple music app with CRUD functionality for managing artifacts (songs). It also includes automated testing tools (Flake8 for linting and Bandit for security testing) to ensure code quality and security. In this context, Heiland et al (2019) used Flake8 and Bandit as part of the software assurance to evaluate python code.

Features
User Authentication: Users can authenticate with a username and password.
CRUD Operations: Users can create, read, update, and delete artifacts (songs).
Encryption: Content of artifacts is encrypted for security.
Automated Testing: Flake8 is used for linting to enforce coding standards, and Bandit is used for security testing to detect common security issues.

Usage
Prerequisites
Python 3.x installed on your system
pip package manager

Installation
Clone the repository:
myounes@myouneslap MINGW64 ~
$ git clone https://github.com/my23007/Module4.git
Cloning into 'Module4'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.

Navigate to the project directory:
cd Module4/
Install dependencies:
pip install flake8
pip install bandit

Running the Application
To run the application and execute the automated tests, use the following command:
python mod4_assign.py

This will run the Flake8 linter and Bandit security testing, followed by executing the main functionality of the music app. Below is a sample output

myounes@myouneslap MINGW64 ~/Module4 (main)
$ python mod4_assign.py
Running Flake8:
mod4_assign.py:6:1: E302 expected 2 blank lines, found 1
mod4_assign.py:11:1: E302 expected 2 blank lines, found 1
mod4_assign.py:15:1: W293 blank line contains whitespace
mod4_assign.py:24:1: W293 blank line contains whitespace
mod4_assign.py:28:1: W293 blank line contains whitespace
mod4_assign.py:33:1: W293 blank line contains whitespace
mod4_assign.py:38:1: W293 blank line contains whitespace
mod4_assign.py:42:1: W293 blank line contains whitespace
mod4_assign.py:44:80: E501 line too long (110 > 79 characters)
mod4_assign.py:53:1: W293 blank line contains whitespace
mod4_assign.py:55:80: E501 line too long (96 > 79 characters)
mod4_assign.py:63:1: W293 blank line contains whitespace
mod4_assign.py:68:1: E302 expected 2 blank lines, found 1
mod4_assign.py:72:1: W293 blank line contains whitespace
mod4_assign.py:79:1: W293 blank line contains whitespace
mod4_assign.py:83:1: W293 blank line contains whitespace
mod4_assign.py:86:1: W293 blank line contains whitespace
mod4_assign.py:89:1: W293 blank line contains whitespace
mod4_assign.py:91:80: E501 line too long (123 > 79 characters)
mod4_assign.py:93:1: W293 blank line contains whitespace
mod4_assign.py:100:1: W293 blank line contains whitespace
mod4_assign.py:105:1: W293 blank line contains whitespace
mod4_assign.py:108:1: W293 blank line contains whitespace
mod4_assign.py:111:1: W293 blank line contains whitespace
mod4_assign.py:114:1: W293 blank line contains whitespace
mod4_assign.py:116:80: E501 line too long (109 > 79 characters)
mod4_assign.py:118:1: W293 blank line contains whitespace
mod4_assign.py:125:1: W293 blank line contains whitespace
mod4_assign.py:130:1: W293 blank line contains whitespace
mod4_assign.py:135:1: E302 expected 2 blank lines, found 1
mod4_assign.py:138:1: W293 blank line contains whitespace
mod4_assign.py:145:1: W293 blank line contains whitespace
mod4_assign.py:148:1: W293 blank line contains whitespace
mod4_assign.py:155:1: W293 blank line contains whitespace
mod4_assign.py:160:1: E302 expected 2 blank lines, found 1
mod4_assign.py:164:80: E501 line too long (130 > 79 characters)
mod4_assign.py:165:80: E501 line too long (105 > 79 characters)
mod4_assign.py:169:1: W293 blank line contains whitespace
mod4_assign.py:172:80: E501 line too long (136 > 79 characters)
mod4_assign.py:173:80: E501 line too long (105 > 79 characters)
mod4_assign.py:177:1: W293 blank line contains whitespace
mod4_assign.py:182:1: E305 expected 2 blank lines after class or function definition, found 1
mod4_assign.py:184:1: W293 blank line contains whitespace
mod4_assign.py:187:1: W293 blank line contains whitespace
mod4_assign.py:189:80: E501 line too long (81 > 79 characters)
mod4_assign.py:192:1: W293 blank line contains whitespace
mod4_assign.py:194:1: W293 blank line contains whitespace
mod4_assign.py:197:1: W293 blank line contains whitespace
mod4_assign.py:199:80: E501 line too long (82 > 79 characters)
mod4_assign.py:200:59: W292 no newline at end of file


Running Bandit:
Run started:2024-05-14 07:27:27.417962

Test results:
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: mod4_assign.py:1:0
1       import subprocess
2       import hashlib
3       from datetime import datetime

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b607_start_process_with_partial_path.html
   Location: mod4_assign.py:164:25
163             print("Running Flake8:")
164             flake8_process = subprocess.Popen(["flake8", "mod4_assign.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
165             flake8_stdout, flake8_stderr = flake8_process.communicate(timeout=30)  # Adjust timeout as needed

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b603_subprocess_without_shell_equals_true.html
   Location: mod4_assign.py:164:25
163             print("Running Flake8:")
164             flake8_process = subprocess.Popen(["flake8", "mod4_assign.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
165             flake8_stdout, flake8_stderr = flake8_process.communicate(timeout=30)  # Adjust timeout as needed

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b607_start_process_with_partial_path.html
   Location: mod4_assign.py:172:25
171             print("\nRunning Bandit:")
172             bandit_process = subprocess.Popen(["bandit", "-r", "mod4_assign.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
173             bandit_stdout, bandit_stderr = bandit_process.communicate(timeout=30)  # Adjust timeout as needed

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b603_subprocess_without_shell_equals_true.html
   Location: mod4_assign.py:172:25
171             print("\nRunning Bandit:")
172             bandit_process = subprocess.Popen(["bandit", "-r", "mod4_assign.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
173             bandit_stdout, bandit_stderr = bandit_process.communicate(timeout=30)  # Adjust timeout as needed

--------------------------------------------------

Code scanned:
        Total lines of code: 121
        Total lines skipped (#nosec): 0
        Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0
                Low: 5
                Medium: 0
                High: 0
        Total issues (by confidence):
                Undefined: 0
                Low: 0
                Medium: 0
                High: 5
Files skipped (0):

[main]  INFO    profile include tests: None
[main]  INFO    profile exclude tests: None
[main]  INFO    cli include tests: None
[main]  INFO    cli exclude tests: None
[main]  INFO    running on Python 3.7.0

Enter username: admin
Enter a password: ········
Enter song title: dff
Enter artist name: sds
User authentication failed.
Enter the ID of the artifact to delete: 56
User authentication failed.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

References:
Heiland, R., Rynge, M., Vahi, K., Deelman, E. and Welch, V., 2019. A Guide for Software Assurance for SWIP.