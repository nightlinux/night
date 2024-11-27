import requests

def fetch_metadata(repo_url):
    metadata_url = f"{repo_url}/metadata.list"
    response = requests.get(metadata_url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"HTTP request failed. Status code: {response.status_code}")

def download_package(package_url, save_path):
    response = requests.get(package_url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    else:
        raise Exception(f"HTTP request failed. Status code: {response.status_code}")

def parse_metadata(metadata_content):
    packages = []
    for line in metadata_content.strip().split('\n'):
        name, version, url = line.split('|')
        packages.append({
            "name": name,
            "version": version,
            "url": url
        })
    return packages


