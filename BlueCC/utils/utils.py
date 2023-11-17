from urllib.parse import urlparse, parse_qs


def is_safe_url(url, allowed_hosts):
    url_info = urlparse(url)
    return url_info.netloc in allowed_hosts
