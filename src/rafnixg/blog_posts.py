"""Blog Posts module using HashNode Client."""
import json
from .hashnode import hashnode_posts

class BlogPost:
    """Blog Post class."""

    def __init__(
        self,
        title: str,
        summay: str,
        link: str,
        published: str,
        cover_image: str,
        tags: list,
    ) -> None:
        """Constructor.
        Args:
            title (str): Título del post.
            summary (str): Resumen del post.
            link (str): Enlace del post.
            published (str): Fecha de publicación del post.
            cover_image (str): Enlace de la imagen de portada.
            tags (list): Lista de etiquetas.
        """
        self.title = title
        self.summary = summay
        self.link = link
        self.published = published
        self.cover_image = cover_image
        self.tags = tags

    def to_dict(self):
        """Convertir a diccionario."""
        return self.__dict__


class BlogPosts:
    """Blog Posts class."""

    def __init__(self):
        """Constructor.
        Inicializa y obtiene los posts.
        """
        self.posts = self.get_posts()


    def get_posts(self) -> list[BlogPost]:
        """Extraer los post del feed.
        Returns:
            posts: Lista de diccionarios con los datos de los post.
        """
        posts = hashnode_posts()
        if not posts:
            return []
        return [
            BlogPost(
                title=post['title'],
                summay=post['summary'],
                link=post['link'],
                published=post['published'],
                cover_image=post['cover_image'],
                tags=[
                    {
                        "name": tag["term"],
                    }
                    for tag in post["tags"]
                ]
                if post.get("tags")
                else [],
            )
            for post in posts
        ]

    def save_to_json(self):
        """Escribir los posts en un archivo JSON."""
        with open("posts.json", "w", encoding="utf-8") as file:
            json.dump(self.posts.to_dict(), file, indent=4)
