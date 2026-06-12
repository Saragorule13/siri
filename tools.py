import subprocess
import webbrowser
import json
from rapidfuzz import process 


with open("apps.json", "r") as f:
    APPS = json.load(f)

ALIASES = {
    "vscode": "code",
    "vs code": "code",
    "visual studio code": "code",
    "chrome": "chrome",
    "spotify": "spotify"
}

def open_app(name):
    try:
        app_name = name.lower()
        app_name = ALIASES.get(app_name, app_name)

        if app_name not in APPS:
            match = process.extractOne(
                app_name,
                APPS.keys()
            )

            if match and match[1] > 70:
                app_name = match[0]
            else:
                return f"{app_name} is not installed."

        subprocess.Popen(APPS[app_name])
        return f"Opening {app_name}..."

    except Exception as e:
        return f"Error opening {name}: {str(e)}"

def open_website(url):
    try:
        if not url.startswith("http"):
            url = "https://" + url
        webbrowser.open(url)
        return f"Opening {url}..."
    except Exception as e:
        return f"Error opening {url}: {str(e)}"