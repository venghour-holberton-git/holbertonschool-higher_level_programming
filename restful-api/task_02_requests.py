import requests
import csv

def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")
    data = None
    if r.status_code == 200:
        data = r.json()
        for d in data:
            print(d["title"])

def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        j = r.json()
        data = [{"id": item["id"],
                 "title": item["title"],
                 "body": item["body"]
                 } 
                 for item in j
                ]
        with open("posts.csv", "w", newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

if __name__ == "__main__":
    fetch_and_save_posts()