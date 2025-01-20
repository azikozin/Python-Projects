import requests
from sites import SITES

def check_username(username):
    for site in SITES:
        url = site["url"].format(username=username)
        try:
            response = requests.get(url, allow_redirects=True)
            
            if site.get("check_redirect"):
                exists = "NOT FOUND" if response.url == site["redirect_url"] else "FOUND"
            else:
                exists = "FOUND" if response.status_code == 200 else "NOT FOUND"
                
            print(f"{site['name']}: {exists} - {url}")
        except:
            print(f"{site['name']}: ERROR checking {url}")

if __name__ == "__main__":
    username = input("Enter username: ")
    check_username(username)