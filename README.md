# PENETRATION-TESTING-TOOLKIT

"COMPANY": CODTECH IT SOLUTIONS

"NAME": CHAUHAN KETAN K

"INTERN ID": CT04DH1934

"DOMAIN": CYBER SECURITY AND ETHICAL HACKING

"DURATION": 4 WEEKS

"MENTOR": NEELA SANTOSH

#DESCRIPTION : This practical involves the development of a Python-based Penetration Testing Toolkit designed to aid ethical hackers and cybersecurity students in identifying common network security weaknesses. The toolkit is built with a modular approach, allowing users to choose between multiple functionalities — primarily a Port Scanner and an SSH Brute-Forcer — from a single interactive menu.

1. Port Scanner Module:
The port scanner scans a target IP address for open TCP ports ranging from 1 to 1024. It uses Python’s built-in socket library to attempt connections to each port. If a connection is successful, the port is marked as open. This helps identify active services on the target system and is useful for reconnaissance in penetration testing.

2. SSH Brute-Forcer Module:
The brute-force module uses the paramiko library to attempt login to an SSH service using a known username and a list of potential passwords. It reads the password list from a file provided by the user. If the correct password is found, it is displayed as a successful login. This simulates a dictionary attack and demonstrates the importance of using strong and unique passwords.

3. Main Menu Interface:
The toolkit features a simple text-based menu that lets the user select the desired operation. This makes the tool user-friendly and interactive. Based on user input, the relevant module is called, executed, and the results are displayed in real time.

4. Use Case:
This tool can be used in educational labs, cybersecurity courses, or beginner-level ethical hacking exercises to demonstrate the principles of reconnaissance and brute-force attacks. It also emphasizes how attackers might exploit weak configurations or insecure systems.

5. Prerequisites:
Python 3.x must be installed.
The paramiko library must be installed using pip install paramiko.
A target IP and a valid password list file are required for the SSH brute-forcer.

6. Disclaimer:
This tool is created for educational and legal testing purposes only. Unauthorized use against systems without permission is strictly prohibited and illegal.

#OUTPUT:

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d02316b9-2fa8-4a74-acdc-3745c3cc1f86" />


