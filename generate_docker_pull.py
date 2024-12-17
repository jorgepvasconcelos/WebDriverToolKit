import json

def main():
    browsers_path = "browsers.json"
    with open(browsers_path) as json_file:
        browsers = json.load(json_file)

    images_name = []
    for browser_name, versions in browsers.items():
        for version, version_info in versions["versions"].items():
            images_name.append(version_info["image"])
    lines = []
    for image in images_name:
        lines.append(f"docker pull {image}\n")


    pull_images_path = "pull_images.sh"
    with open(pull_images_path, "w") as file:
        file.writelines(lines)
if __name__ == "__main__":
    main()
