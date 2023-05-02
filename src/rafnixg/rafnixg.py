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
        self.about = "Experienced software developer with 10+ years of expertise in designing, developing and implementing web systems across various sectors. Backend specialist skilled in Python, Linux, and Git. Passionate about continuous learning and open-source technology."


    def __str__(self):
        return f"{self.name} (@{self.username}) - {self.position}"

    def display(self):
        """Display personal card"""
        console = Console()

        table = Table(
            show_header=False,
            title=str(self),
            highlight=True,
            title_style="bold magenta",
        )
        table.add_column("Attribute", style="bold", width=16)
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
