"""Blog RSS client."""
import html
import re
from xml.etree import ElementTree

import requests

NAMESPACES = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "media": "http://search.yahoo.com/mrss/",
    "dc": "http://purl.org/dc/elements/1.1/",
}


def _clean_html(text):
    """Limpiar etiquetas HTML de un texto."""
    if not text:
        return ""
    cleaned = re.sub(r"<[^>]+>", "", text)
    return html.unescape(cleaned).replace("\xa0", " ").strip()


def _get_text(item, *paths):
    """Obtener texto del primer path encontrado."""
    for path in paths:
        node = item.find(path, NAMESPACES)
        if node is not None and node.text:
            return node.text.strip()
    return ""


def _get_cover_image(item):
    """Obtener imagen de portada desde media/enclosure."""
    media_node = item.find("media:content[@url]", NAMESPACES)
    if media_node is not None:
        return media_node.attrib.get("url", "")

    media_thumbnail = item.find("media:thumbnail[@url]", NAMESPACES)
    if media_thumbnail is not None:
        return media_thumbnail.attrib.get("url", "")

    enclosure = item.find("enclosure[@url]")
    if enclosure is not None:
        return enclosure.attrib.get("url", "")

    return ""


def _extract_tags(item):
    """Extraer etiquetas del item RSS."""
    tags = [{"term": category.text.strip()} for category in item.findall("category") if category.text]
    return tags


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/rss+xml, application/xml, text/xml, */*",
}


def hashnode_posts():
    """Obtener los posts desde RSS."""
    url = "https://blog.rafnixg.dev/rss.xml"
    try:
        response = requests.get(url, timeout=10, headers=HEADERS)
        response.raise_for_status()
        root = ElementTree.fromstring(response.content)
    except (requests.RequestException, ElementTree.ParseError):
        return []

    posts = []
    for item in root.findall("./channel/item"):
        summary = _get_text(item, "description", "content:encoded")
        posts.append(
            {
                "title": _get_text(item, "title"),
                "summary": _clean_html(summary),
                "link": _get_text(item, "link"),
                "published": _get_text(item, "pubDate", "dc:date"),
                "cover_image": _get_cover_image(item),
                "tags": _extract_tags(item),
            }
        )
    return posts

if __name__ == "__main__":
    posts = hashnode_posts()
    for post in posts:
        print(f"Title: {post['title']}")
        print(f"URL: {post['link']}")
        print(f"Brief: {post['summary']}")
        print(f"Published: {post['published']}")
        print(f"Cover Image: {post['cover_image']}")
        print("-" * 40)
