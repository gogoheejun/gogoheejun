import feedparser
my_blog_rss_url = "https://lovenewthing.tistory.com/rss"
rss_feed = feedparser.parse(my_blog_rss_url)

MAX_POST_NUM = 10
latest_blog_post_list = ""
MAX_POST_NUM = 10

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"

markdown_text = """### Hi there 👋 

📬 Contact Email : victory_yang@naver.com 

👨🏻‍💻 Daily Blog : https://lovenewthing.tistory.com

🤩 Latest Blog Post

 """

readme_text = f"{markdown_text}{latest_blog_post_list}"
with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
