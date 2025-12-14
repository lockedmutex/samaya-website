import json
import os
from io import BytesIO

import requests
from PIL import Image

REPO_OWNER = "lockedmutex"
REPO_NAME = "samaya"
API_URL = f"https://codeberg.org/api/v1/repos/{REPO_OWNER}/{REPO_NAME}/commits"
OUTPUT_DIR = "src/contributors"
IMAGES_DIR = os.path.join(OUTPUT_DIR, "images")
DATA_FILE = os.path.join(OUTPUT_DIR, "contributors.js")

os.makedirs(IMAGES_DIR, exist_ok=True)


def fetch_contributors():
    print(f"Fetching commits from {API_URL}...")
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        commits = response.json()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

    contributors_map = {}

    for commit in commits:
        if "author" in commit and commit["author"]:
            author = commit["author"]
            username = author.get("login")
            avatar_url = author.get("avatar_url")

            if username:
                if username not in contributors_map:
                    contributors_map[username] = {
                        "username": username,
                        "avatar_url": avatar_url,
                        "profile_url": f"https://codeberg.org/{username}",
                        "contributions": 0,
                    }
                contributors_map[username]["contributions"] += 1

    return list(contributors_map.values())


def process_images(contributors):
    processed_list = []

    for user in contributors:
        username = user["username"]
        avatar_url = user["avatar_url"]

        filename = f"{username.lower()}.avif"
        local_path = os.path.join(IMAGES_DIR, filename)
        web_path = f"./contributors/images/{filename}"

        print(f"Processing image for {username}...")

        try:
            img_response = requests.get(avatar_url)
            img_response.raise_for_status()

            img = Image.open(BytesIO(img_response.content))

            if img.size[0] > 128 or img.size[1] > 128:
                img = img.resize((128, 128), Image.Resampling.LANCZOS)

            img.save(local_path, "AVIF", quality=80)

            user["local_image"] = web_path
            processed_list.append(user)

        except Exception as e:
            print(f"Failed to process image for {username}: {e}")
            user["local_image"] = avatar_url
            processed_list.append(user)

    return processed_list


def sort_contributors(contributors):
    def sort_key(user):
        if user["username"].lower() == "lockedmutex":
            return float("inf")
        return user["contributions"]

    return sorted(contributors, key=sort_key, reverse=True)


def save_js(contributors):
    js_content = f"window.SAMAYA_CONTRIBUTORS = {json.dumps(contributors, indent=4)};"

    with open(DATA_FILE, "w") as f:
        f.write(js_content)
    print(f"Saved data to {DATA_FILE}")


def main():
    contributors = fetch_contributors()
    if not contributors:
        print("No contributors found.")
        return

    contributors = process_images(contributors)
    contributors = sort_contributors(contributors)
    save_js(contributors)


if __name__ == "__main__":
    main()
