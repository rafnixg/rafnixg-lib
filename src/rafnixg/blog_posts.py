"""Blog Posts module using RSS feed."""
import json
import feedparser


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
        Args:
            feed_path (str): Ruta del archivo RSS.
        """
        self.url = "https://blog.rafnixg.dev/rss.xml"
        self.feed_path = self.url
        self._feed = self.read_feed()
        self.posts = self.get_posts()

    def read_feed(self) -> dict:
        """Leer el feed desde un archivo RSS.
        Returns:
            feed (dict): Diccionario con los datos del feed.
        """
        return feedparser.parse(self.feed_path)

    def get_posts(self) -> list[BlogPost]:
        """Extraer los post del feed.
        Returns:
            posts: Lista de diccionarios con los datos de los post.
        """
        return [
            BlogPost(
                title=post.title,
                summay=post.summary,
                link=post.link,
                published=post.published,
                cover_image=post.cover_image,
                tags=[
                    {
                        "name": tag["term"],
                    }
                    for tag in post.tags
                ]
                if post.get("tags")
                else [],
            )
            for post in self._feed.entries
        ]

    def save_to_json(self):
        """Escribir los posts en un archivo JSON."""
        with open("posts.json", "w", encoding="utf-8") as file:
            json.dump(self.posts.to_dict(), file, indent=4)
