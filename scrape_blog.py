rm scrape_blog.py
cat > scrape_blog.py << 'EOF'
import requests
from bs4 import BeautifulSoup

url = 'https://blog.python.org/blog/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

titles = soup.find_all('h3')

for title in titles:
    title_text = title.text.strip()
    
    link_tag = title.find('a') or title.find_parent('a')
    link = link_tag['href'] if link_tag else None
    if link and link.startswith('/'):
        link = 'https://blog.python.org' + link
    
    next_elem = title.find_next()
    author_date = next_elem.text.strip() if next_elem else None
    
    summary_elem = next_elem.find_next() if next_elem else None
    summary = summary_elem.text.strip() if summary_elem else None
    
    print("Title:", title_text)
    print("Author/Date:", author_date)
    print("Link:", link)
    print("Summary:", summary)
    print("-" * 50)
EOF

