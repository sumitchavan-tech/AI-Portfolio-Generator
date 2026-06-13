import re


def extract_links(text):

    github = ""
    linkedin = ""
    portfolio = ""

    urls = re.findall(
        r'https?://[^\s]+',
        text
    )

    for url in urls:

        lower_url = url.lower()

        if "github.com" in lower_url:
            github = url

        elif "linkedin.com" in lower_url:
            linkedin = url

        elif (
            "netlify.app" in lower_url
            or "vercel.app" in lower_url
            or ".com" in lower_url
        ):
            portfolio = url

    return {
        "github": github,
        "linkedin": linkedin,
        "portfolio": portfolio
    }