import os
import json

app_locations = [
    r"C:\Program Files",
    r"C:\Program Files (x86)"
]

def scan_apps():
    apps = {}
    
    for root_dir in app_locations:
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                if file.lower().endswith(".exe"):
                    app_name = os.path.splitext(file)[0]
                    app_path = os.path.join(root, file)

                    if app_name not in apps:
                        apps[app_name] = app_path
    return apps

def save_registry(apps):
    with open("apps.json", "w") as f:
        json.dump(apps, f, indent=4)

if __name__ == "__main__":

    apps = scan_apps()

    save_registry(apps)

    print(f"Found {len(apps)} applications")