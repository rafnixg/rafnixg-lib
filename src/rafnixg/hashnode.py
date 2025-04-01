"""Hashnode API client.
This module provides a client for interacting with the Hashnode API using GraphQL."""
import requests

def _transform_posts(posts_data):
    """Transformar los posts en una lista de diccionarios.
    Args:
        posts_data (list): Lista de posts de Hashnode.
    Returns:
        list: Lista de posts transformados.
    """
    return [
        _transform_post(post["node"])
        for post in posts_data["data"]["publication"]["posts"]["edges"]
    ]

def _transform_post(post_data):
    """Transformar el post en un diccionario.
    Args:
        post_data (dict): Post de Hashnode.
    Returns:
        dict: Post transformado.
    """
    return {
        "title": post_data["title"],
        "summary": post_data["brief"],
        "link": post_data["url"],
        "published": post_data["publishedAt"],
        "cover_image": post_data["coverImage"]["url"],
    }

def hashnode_posts():
    """Obtener los posts de Hashnode usando GraphQL."""
    query = """
query Publication {
  publication(host: "blog.rafnixg.dev"){
    posts(first:0){
      edges {
        node {
          slug
          title
          url
          brief
          publishedAt
          coverImage{
            url
          }
          content {
            markdown
          }
        }
      }
    }
  }
}
"""
    url = "https://gql.hashnode.com/"
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "query": query,
    }
    response = requests.post(url, headers=headers, json=data, timeout=10)
    if response.status_code == 200:
        return _transform_posts(response.json())
    else:
        return []

if __name__ == "__main__":
    posts = hashnode_posts()
    for post in posts:
        print(f"Title: {post['title']}")
        print(f"URL: {post['link']}")
        print(f"Brief: {post['summary']}")
        print(f"Published: {post['published']}")
        print(f"Cover Image: {post['cover_image']}")
        print("-" * 40)
