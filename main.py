import requests
import time
import random

# Variables
cookies = input("Enter FB Cookies: ")
time_delay = int(input("Enter Time Delay (seconds): "))
haters_name = input("Enter Haters Name: ")
post_id = int(input("Enter Post ID (numeric): "))

# Load comments from file
def load_comments():
    comments_file_path = input("Enter Comments File Path: ")
    try:
        with open(comments_file_path, 'r') as f:
            comments = [line.strip() for line in f.readlines()]
        return comments
    except FileNotFoundError:
        print("File not found!")
        return []

# Send comment
def send_comment(comment):
    url = f"https://www.facebook.com/{post_id}/comments"
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Cookie': cookies
    }
    data = {
        'comment_text': comment
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print(f'Comment sent: {comment}')
    else:
        print(f'Error sending comment: {comment}. Status code: {response.status_code}')
        remove_comment(comment)

# Remove comment from file
def remove_comment(comment):
    with open('/storage/emulated/0/np.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    with open('/storage/emulated/0/np.txt', 'w') as f:
        for line in lines:
            if line != comment:
                f.write(line + '\n')

# Main function
def main():
    comments = load_comments()
    for comment in comments:
        send_comment(comment)
        time.sleep(time_delay)
        if random.random() < 0.5:
            print(f'Haters gonna hate: {haters_name}')

if __name__ == '__main__':
    main()
