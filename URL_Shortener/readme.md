# URL Shortener

Short URLs are easy to remember or type, so they are very popular in the field of digital marketing and promotions.

-----

## Code Break:

```python
from __future__ import with_statement
import contextlib

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import sys
```

The script starts by importing necessary modules. It uses the `urllib` module to encode URL parameters and make HTTP requests.

```python
def make_tiny(url):
    request_url = "http://tinyurl.com/api-create.php?" + urlencode({"url": url})
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode("utf-8")
```

Defines a function `make_tiny` that takes a URL, constructs a request URL with the TinyURL API, and then sends a request to TinyURL. The response is read, decoded, and returned.

```python
def main():
    for tinyurl in map(make_tiny, sys.argv[1:]):
        print(tinyurl)

if __name__ == "__main__":
    main()
```

The `main` function is responsible for processing command-line arguments. It iterates through the URLs passed as arguments, calls `make_tiny` for each URL, and prints the corresponding shortened URL.

If you run this script from the command line and provide one or more URLs as arguments, it will output the corresponding TinyURLs for those URLs. For example:

```bash
python script.py https://example.com https://another-url.com
```

The output will be the TinyURLs for the provided URLs.

-----