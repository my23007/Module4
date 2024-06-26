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
python mod4_coding_assignment.py

This will run the Flake8 linter and Bandit security testing, followed by executing the main functionality of the music app. Below is a sample output

myounes@myouneslap MINGW64 ~/Module4 (main)
$ python mod4_assign.py
Running Flake8:
mod4_coding_assignment.py:12:1: E302 expected 2 blank lines, found 1
mod4_coding_assignment.py:17:1: E302 expected 2 blank lines, found 1
mod4_coding_assignment.py:21:1: W293 blank line contains whitespace
mod4_coding_assignment.py:32:1: W293 blank line contains whitespace
mod4_coding_assignment.py:36:80: E501 line too long (81 > 79 characters)
mod4_coding_assignment.py:41:1: W293 blank line contains whitespace
mod4_coding_assignment.py:45:1: W293 blank line contains whitespace
mod4_coding_assignment.py:49:1: W293 blank line contains whitespace
mod4_coding_assignment.py:53:1: W293 blank line contains whitespace
mod4_coding_assignment.py:55:80: E501 line too long (110 > 79 characters)
mod4_coding_assignment.py:64:1: W293 blank line contains whitespace
mod4_coding_assignment.py:66:80: E501 line too long (96 > 79 characters)
mod4_coding_assignment.py:74:1: W293 blank line contains whitespace
mod4_coding_assignment.py:79:1: E302 expected 2 blank lines, found 1
mod4_coding_assignment.py:83:1: W293 blank line contains whitespace
mod4_coding_assignment.py:89:1: W293 blank line contains whitespace
mod4_coding_assignment.py:92:1: W293 blank line contains whitespace
mod4_coding_assignment.py:95:1: W293 blank line contains whitespace
mod4_coding_assignment.py:96:80: E501 line too long (123 > 79 characters)
mod4_coding_assignment.py:98:1: W293 blank line contains whitespace
mod4_coding_assignment.py:104:1: W293 blank line contains whitespace
mod4_coding_assignment.py:108:1: W293 blank line contains whitespace
mod4_coding_assignment.py:112:1: W293 blank line contains whitespace
mod4_coding_assignment.py:113:80: E501 line too long (109 > 79 characters)
mod4_coding_assignment.py:115:1: W293 blank line contains whitespace
mod4_coding_assignment.py:121:1: W293 blank line contains whitespace
mod4_coding_assignment.py:125:1: W293 blank line contains whitespace
mod4_coding_assignment.py:129:1: E302 expected 2 blank lines, found 1
mod4_coding_assignment.py:132:1: W293 blank line contains whitespace
mod4_coding_assignment.py:137:1: W293 blank line contains whitespace
mod4_coding_assignment.py:139:1: W293 blank line contains whitespace
mod4_coding_assignment.py:144:1: W293 blank line contains whitespace
mod4_coding_assignment.py:147:1: E302 expected 2 blank lines, found 1
mod4_coding_assignment.py:150:80: E501 line too long (141 > 79 characters)
mod4_coding_assignment.py:155:1: W293 blank line contains whitespace
mod4_coding_assignment.py:157:80: E501 line too long (147 > 79 characters)
mod4_coding_assignment.py:162:1: W293 blank line contains whitespace
mod4_coding_assignment.py:167:1: W293 blank line contains whitespace
mod4_coding_assignment.py:177:80: E501 line too long (104 > 79 characters)
mod4_coding_assignment.py:186:80: E501 line too long (85 > 79 characters)
mod4_coding_assignment.py:189:80: E501 line too long (99 > 79 characters)
mod4_coding_assignment.py:195:80: E501 line too long (102 > 79 characters)
mod4_coding_assignment.py:200:1: W293 blank line contains whitespace
mod4_coding_assignment.py:204:1: E305 expected 2 blank lines after class or function definition, found 1
mod4_coding_assignment.py:206:1: W293 blank line contains whitespace
mod4_coding_assignment.py:209:1: W293 blank line contains whitespace
mod4_coding_assignment.py:214:1: W293 blank line contains whitespace
mod4_coding_assignment.py:216:1: W293 blank line contains whitespace
mod4_coding_assignment.py:218:1: W293 blank line contains whitespace
mod4_coding_assignment.py:219:80: E501 line too long (82 > 79 characters)
mod4_coding_assignment.py:227:1: W391 blank line at end of file


Running Bandit:
Run started:2024-05-14 14:15:11.303081

Test results:
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.8/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: .\mod4_coding_assignment.py:7:0
6	
7	import subprocess
8	import hashlib

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.8/plugins/b607_start_process_with_partial_path.html
   Location: .\mod4_coding_assignment.py:150:25
149	        print("Running Flake8:")
150	        flake8_process = subprocess.Popen(["flake8", "mod4_coding_assignment.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
151	        flake8_stdout, flake8_stderr = flake8_process.communicate(timeout=30)

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.8/plugins/b603_subprocess_without_shell_equals_true.html
   Location: .\mod4_coding_assignment.py:150:25
149	        print("Running Flake8:")
150	        flake8_process = subprocess.Popen(["flake8", "mod4_coding_assignment.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
151	        flake8_stdout, flake8_stderr = flake8_process.communicate(timeout=30)

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.8/plugins/b607_start_process_with_partial_path.html
   Location: .\mod4_coding_assignment.py:157:25
156	        print("\nRunning Bandit:")
157	        bandit_process = subprocess.Popen(["bandit", "-r", "mod4_coding_assignment.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
158	        bandit_stdout, bandit_stderr = bandit_process.communicate(timeout=30)

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.8/plugins/b603_subprocess_without_shell_equals_true.html
   Location: .\mod4_coding_assignment.py:157:25
156	        print("\nRunning Bandit:")
157	        bandit_process = subprocess.Popen(["bandit", "-r", "mod4_coding_assignment.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
158	        bandit_stdout, bandit_stderr = bandit_process.communicate(timeout=30)

--------------------------------------------------

Code scanned:
	Total lines of code: 155
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

[main]	INFO	profile include tests: None
[main]	INFO	profile exclude tests: None
[main]	INFO	cli include tests: None
[main]	INFO	cli exclude tests: None
[main]	INFO	running on Python 3.9.7


Testing Artifact Creation with Checksum and Encryption:
Authenticating user: admin
Authentication successful
User admin is already authenticated
Artifact added successfully.
Artifact 1 exists.
Stored artifact: {'title': 'Test Song', 'artist': 'Test Artist', 'content': '.tnetnoc tset a si sihT', 'creation_date': datetime.datetime(2024, 5, 14, 17, 15, 11, 333790), 'modification_date': datetime.datetime(2024, 5, 14, 17, 15, 11, 333790), 'checksum': 'f74d46f5c58d6d0fac6e1dd341dc44e8881cc40fc2c08daec80ec75b902a42db'}
Expected checksum: f74d46f5c58d6d0fac6e1dd341dc44e8881cc40fc2c08daec80ec75b902a42db
Stored checksum: f74d46f5c58d6d0fac6e1dd341dc44e8881cc40fc2c08daec80ec75b902a42db
Checksum verification passed: True
Expected encrypted content: .tnetnoc tset a si sihT
Stored encrypted content: .tnetnoc tset a si sihT
Encryption verification passed: True
Enter username: admin
Enter a password: ········
Enter song title: testing
Enter artist name: testing
User admin is not authenticated
Authenticating user: admin
Authentication successful
Artifact added successfully.
Enter the ID of the artifact to delete: 123
User admin is already authenticated
Artifact does not exist.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

Limitations:
This is a deviation from the original design proposed in the first assignment, I used my own UML class diagram for simplicity and ease in coding. The original one encompasses many classes and attributes and will complicate the python code, hence I used my simplified version.

References:
Heiland, R., Rynge, M., Vahi, K., Deelman, E. and Welch, V., 2019. A Guide for Software Assurance for SWIP.