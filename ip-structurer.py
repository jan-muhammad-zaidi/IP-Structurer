#!/usr/bin/python
import re

def clean_ip_list(ip_list):
    cleaned_ips = []

    for ip in ip_list:
        ip = ip.strip()
        if ip:
            cleaned_ips.append(ip)

    return cleaned_ips

def main():
    input_file_path = '/root/CustomTool/IPs.txt'
    output_file_path = '/root/CustomTool/structured_ips.txt'

    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
            # Use regular expression to extract IP addresses
            ip_list = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', content)

        cleaned_ips = clean_ip_list(ip_list)

        with open(output_file_path, 'w') as file:
            for ip in cleaned_ips:
                file.write(ip + '\n')

        print(f"Structured IPs written to {output_file_path}")

    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
