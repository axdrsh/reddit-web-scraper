import requests
from bs4 import BeautifulSoup

print("enter a subreddit name:")
x = input("r/")
print('''
      Hot (1)
      Top posts (2)
      New (3)
''')
y = int(input(">> "))

url1 = f"https://old.reddit.com/r/{x}/hot/"
url2 = f"https://old.reddit.com/r/{x}/top/?sort=top&t=all"
url3 = f"https://old.reddit.com/r/{x}/new/"

if y == 1:
   url = url1
elif y == 2:
    url = url2
elif y == 3:
    url = url3
else:
    url = f"https://old.reddit.com/r/{x}/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all('div', class_='thing')
post_data = []
for post in posts:
    title = post.find('a', class_='title').text  # Extract post title
    author_tag = post.find('a', class_='author')
    author = author_tag.text if author_tag else "Unknown"  # Handle missing author
    comments = post.find('a', class_='comments').text if post.find('a', class_='comments') else "0"  # Extract number of comments
    score = post.find('div', class_='score unvoted').text if post.find('div', class_='score unvoted') else "0"  # Extract score

    post_data.append({
        'Title': title,
        'Author': author,
        'Comments': comments,
        'Score': score,
    })

for data in post_data:
    print(data)