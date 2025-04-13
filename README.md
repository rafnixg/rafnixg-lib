# Rafnix Guzmán - Personal Card

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Python Version](https://img.shields.io/badge/Python-%3E=3.9-blue)](https://www.python.org/downloads/)
[![PyPI Version](https://img.shields.io/pypi/v/rafnixg)](https://pypi.org/project/rafnixg/)
[![Build Status](https://github.com/rafnixg/rafnixg-lib/actions/workflows/python-publish.yml/badge.svg)](https://github.com/rafnixg/rafnixg-lib/actions)
[![Downloads](https://img.shields.io/pypi/dm/rafnixg)](https://pypi.org/project/rafnixg/)

## 👋 Introduction

Welcome to **Rafnix Guzmán - Personal Card**, a Python library that provides a personal card, blog post manager, and resume tools for developers. This library is designed to showcase your personal information, blog posts, and resume in a console-friendly format.

Visit my personal website: [rafnixg.dev](https://rafnixg.dev)

![image](https://github.com/user-attachments/assets/4c1c368b-83ca-4ff7-89d0-c131efe60c9f)

---

## 🚀 Features

- **Personal Card**: Display your personal information in a styled console table.
- **Blog Posts**: Fetch and display your latest blog posts from Hashnode.
- **Resume Tools**: Retrieve and display your resume details, including work experience, education, skills, and more.
- **Customizable Links**: Manage and display your personal links.

---

## 🛠 Installation

Install the library using pip:

```bash
pip install rafnixg
```

---

## 📖 Usage

### Display Personal Card

Run the following command to display your personal card:

```bash
rafnixg
```

### Blog Posts

Fetch and display your latest blog posts:

```python
from rafnixg import BlogPosts

blog_posts = BlogPosts()
posts = blog_posts.get_posts()
for post in posts:
    print(post.title, post.link)
```

### Resume Tools

Retrieve and display your resume details:

```python
from rafnixg import Resume

resume = Resume()
resume_data = resume.get_resume()
print(resume_data)
```

---

## 📚 Documentation

### Personal Card

The `RafnixG` class provides a method to display your personal card in the console. It includes attributes like your name, position, and links to your social profiles.

### Blog Posts

The `BlogPosts` class fetches your latest blog posts from Hashnode using the Hashnode GraphQL API. Posts include the title, summary, link, and publication date.

### Resume

The `Resume` class retrieves your resume details from a JSON file hosted online. It includes sections like:

- Basics (name, email, profiles)
- Work experience
- Education
- Skills
- Languages
- References

---

## 🧪 Development

To contribute or run the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/rafnixg/rafnixg-lib.git
   cd rafnixg-lib
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the main script:

   ```bash
   python -m rafnixg
   ```

4. Run tests:

   ```bash
   pytest
   ```

---

## 📦 Deployment

This library is automatically published to PyPI using GitHub Actions. Every new release triggers a build and deployment workflow.

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE).

---

## 🌟 Acknowledgments

- [Rich Library](https://github.com/Textualize/rich) for console styling.
- [Hashnode API](https://hashnode.com/) for blog post integration.
- [Requests Library](https://docs.python-requests.org/) for HTTP requests.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

---

## 📬 Contact

For any inquiries, reach out to me via:

- **Website**: [rafnixg.dev](https://rafnixg.dev)
- **GitHub**: [rafnixg](https://github.com/rafnixg)
- **Twitter**: [@rafnixg](https://twitter.com/rafnixg)
