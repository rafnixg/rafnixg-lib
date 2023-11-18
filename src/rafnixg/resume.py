"""Resume module."""
import requests


class Profile:
    """Profile class."""

    def __init__(
        self,
        network: str,
        username: str,
        url: str,
    ):
        """Constructor."""
        self.network = network
        self.username = username
        self.url = url


class Basics:
    """Basics class."""

    def __init__(
        self,
        name: str,
        label: str,
        image: str,
        email: str,
        url: str,
        summary: str,
        location: dict,
        profiles: list[Profile],
    ):
        """Constructor."""
        self.name = name
        self.label = label
        self.image = image
        self.email = email
        self.url = url
        self.summary = summary
        self.location = location
        self.profiles = profiles


class Work:
    """Work class."""

    def __init__(
        self,
        company: str,
        position: str,
        website: str,
        start_date: str,
        end_date: str,
        summary: str,
        highlights: list[str],
        location: str,
    ):
        """Constructor."""
        self.company = company
        self.position = position
        self.website = website
        self.start_date = start_date
        self.end_date = end_date
        self.summary = summary
        self.highlights = highlights
        self.location = location


class Education:
    """Education class."""

    def __init__(
        self,
        institution: str,
        area: str,
        study_type: str,
        start_date: str,
        end_date: str,
    ):
        """Constructor."""
        self.institution = institution
        self.area = area
        self.study_type = study_type
        self.start_date = start_date
        self.end_date = end_date


class Certificate:
    """Certificate class."""

    def __init__(
        self,
        title: str,
        date: str,
        awarder: str,
        url: str,
    ):
        """Constructor."""
        self.title = title
        self.date = date
        self.awarder = awarder
        self.url = url


class Skill:
    """Skill class."""

    def __init__(
        self,
        name: str,
        level: str,
        keywords: list[str],
    ):
        """Constructor."""
        self.name = name
        self.level = level
        self.keywords = keywords


class Language:
    """Language class."""

    def __init__(
        self,
        language: str,
        fluency: str,
    ):
        """Constructor."""
        self.language = language
        self.fluency = fluency


class Reference:
    """Reference class."""

    def __init__(
        self,
        name: str,
        reference: str,
    ):
        """Constructor."""
        self.name = name
        self.reference = reference


class Resume:
    """Resume class."""

    def __init__(self):
        """Constructor."""
        self.json_path = "https://resume.rafnixg.dev/resume.json"
        self.raw_data = self.read_json()
        self.basics = self.get_basics()
        self.work = self.get_work()
        self.education = self.get_education()
        self.skills = self.get_skills()
        self.languages = self.get_languages()
        self.references = self.get_references()

    def read_json(self) -> dict:
        """Leer el feed desde un archivo JSON HTTP.
        Returns:
            feed (dict): Diccionario con los datos del feed.
        """
        response = requests.get(self.json_path)
        if response.status_code != 200:
            raise ValueError("Invalid JSON file")
        return response.json()

    def to_dict(self):
        """Convertir a diccionario."""
        return self.__dict__

    def get_basics(self):
        """Get basics."""
        basics = self.raw_data.get("basics")
        return Basics(
            name=basics.get("name", ""),
            label=basics.get("label", ""),
            image=basics.get("image", ""),
            email=basics.get("email", ""),
            url=basics.get("url", ""),
            summary=basics.get("summary", ""),
            location=basics.get("location", ""),
            profiles=basics.get("profiles", []),
        )

    def get_work(self):
        """Get work."""
        return [
            Work(
                company=work.get("name", ""),
                position=work.get("position", ""),
                website=work.get("url", ""),
                start_date=work.get("startDate", ""),
                end_date=work.get("endDate", ""),
                summary=work.get("summary", ""),
                highlights=work.get("highlights", []),
                location=work.get("location", ""),
            )
            for work in self.raw_data.get("work", [])
        ]

    def get_education(self):
        """Get education."""
        return [
            Education(
                institution=education.get("institution", ""),
                area=education.get("area", ""),
                study_type=education.get("studyType", ""),
                start_date=education.get("startDate", ""),
                end_date=education.get("endDate", ""),
            )
            for education in self.raw_data.get("education", [])
        ]

    def get_certificates(self):
        """Get certificates."""
        return [
            Certificate(
                title=certificate.get("name", ""),
                date=certificate.get("startDate", ""),
                awarder=certificate.get("issuer", ""),
                url=certificate.get("url", ""),
            )
            for certificate in self.raw_data.get("certificates", [])
        ]

    def get_skills(self):
        """Get skills."""
        return [
            Skill(
                name=skill.get("name", ""),
                level=skill.get("level", ""),
                keywords=skill.get("keywords", []),
            )
            for skill in self.raw_data.get("skills", [])
        ]

    def get_languages(self):
        """Get languages."""
        return [
            Language(
                language=language.get("language", ""),
                fluency=language.get("fluency", ""),
            )
            for language in self.raw_data.get("languages", [])
        ]

    def get_references(self):
        """Get references."""
        return [
            Reference(
                name=reference.get("name", ""),
                reference=reference.get("reference", ""),
            )
            for reference in self.raw_data.get("references", [])
        ]

    def get_resume(self):
        """Get resume."""
        return {
            "basics": self.basics,
            "work": self.work,
            "education": self.education,
            "skills": self.skills,
            "languages": self.languages,
            "references": self.references,
        }
