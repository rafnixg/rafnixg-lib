"""RafnixG - Personal Card"""
from rich.console import Console
from rich.table import Table


class RafnixG:
    """RafnixG - Personal Card"""
    def __init__(self):
        self.username = "rafnixg"
        self.name = "Rafnix Guzmán"
        self.position = "Python Software Developer"
        self.web = "https://rafnixg.dev"
        self.blog = "https://blog.rafnixg.dev"
        self.cv = "https://rafnixg.dev/resume"
        self.github = "https://github.com/rafnixg"
        self.twitter = "@rafnixg"
        self.code = {
            "backend": [
                "Python",
                "Odoo",
                "FastAPI",
                "Flask",
                "Django",
            ],
            "database": ["PostgreSQL", "MySQL", "SQLite3", "Mongo DB", "Redis"],
            "devops": [
                "Docker",
                "Linux",
                "Jenkins",
                "GitHub Actions",
                "AWS",
                "Proxmox",
                "LXC",
            ],
            "frontend": ["HTML", "CSS", "JavaScript", "ReactJS", "Svelte", "Boostrap"],
            "tools": [
                "GIT",
                "GitHub",
                "GitLab",
                "Pandas",
                "Jupyter notebook",
                "SQLAlchemy",
                "Celery",
                "Nginx",
            ],
            "misc": ["Firebase", "TDD", "SCRUM", "SOLID", "gRPC", "ML", "Tech Writer"],
        }
        self.architecture = ["SPA", "MVC", "Serverless", "microservices"]

    def __str__(self):
        return f"{self.name} | {self.position}"

    def display(self):
        """Display personal card"""
        console = Console()

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Attribute", style="dim", width=16)
        table.add_column("Value")

        for key, value in self.__dict__.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    table.add_row(sub_key, ", ".join(sub_value))
            elif isinstance(value, list):
                table.add_row(key, ", ".join(value))
            else:
                table.add_row(key, value)
        
        console.print(table)