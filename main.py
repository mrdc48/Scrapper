import requests
from bs4 import BeautifulSoup

url = "https://www.seagate.com/kr/ko/support/products/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

anchor_tags = soup.find_all("a")

for anchor in anchor_tags:
  link = anchor.get("href")
  if link:
    try:
      response = requests.head(link)  # Use HEAD request for efficiency
      if response.status_code == 404:
        print("Broken link: {link}")
      else:
        print(f"Link is working: {link}")
    except requests.exceptions.RequestException as e:
      print(f"Error checking link {link}: {e}")
  else:
    print("Link without href attribute:", anchor)
