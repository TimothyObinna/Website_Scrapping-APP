from re import findall
import requests


# Prompts the user for the URL of the website:
url = input("Enter the URL of the website: ")
site = f"https://www.{url}"

# Download the website's content
response = requests.get(site)
content = response.text

# Extract all links from the website
links = findall(r'<a\s+.*?href=[\'"](.*?)[\'"].*?>', content)

# Search for phone numbers and emails using regular expressions
phone_numbers = findall(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", content)
emails = findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

# Print the extracted data
print(" ")
print("The Website Links:")
for link in links:
    print(link)
    print("")

print("The Phone Numbers:")
for phone_number in phone_numbers:
    print(phone_number)

print("\nThe Emails:")
for email in emails:
    print(email)

# Prompt the user for the filename to save the links to
file_links = input("\nEnter the filename to save the Links to: ")

# converts the file_links to .txt extention
my_link = f"{file_links}.txt"

# Saves the extracted links to file_links
with open(my_link, mode ="w") as f:
    for link in links:
        f.write(link + "\n")

# Prompt the user for the filename to save the Phone Numbers to
file_phonenumber = input("\nEnter the filename to save the Phone Numbers to: ")

# Converts the file_phonenumber to .txt extension
my_phonenumbers = f"{file_phonenumber}.txt"

# Saves the extracted Phone Numbers to file_phonenumber
with open(my_phonenumbers, mode ="w") as f:
    for phone_number in phone_numbers:
        f.write(phone_number + "\n")


# Prompt the user for the filename to save the Emails to
file_email = input("\nEnter the filename to save the Emails to: ")

# Converts the file_email to .txt extension
my_email = f"{file_email}.txt"

# Saves the extracted Emails to file_email
with open(my_email, mode ="w") as f:
    for email in emails:
        f.write(email + "\n")
        
# To save the extracts in one file
all_extracts = input("\nEnter the filename to save all the extracts to: ")

# Converts the all_extracts to .txt extension
my_allextracts = f"{all_extracts}.txt"

# Saves the extracted links to file_links
with open(my_allextracts, mode ="w") as f:
    for link in links:
        f.write(link + "\n")

    for phone_number in phone_numbers:
        f.write(phone_number + " \n")
       
    for email in emails:
        f.write(email + "\n")
        





