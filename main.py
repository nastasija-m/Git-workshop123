from urllib.request import Request, urlopen

def fetch_random_dad_joke() -> str:

    """
   fatch a dad joke in the develop branch
    """
    req = Request(
        url="https://icanhazdadjoke.com/",
        headers={
            "Accept": "text/plain",
            "User-Agent": "Workshop"
        }
    )
    return urlopen(req).read().decode("utf-8")
print("hi")

print(fetch_random_dad_joke())
