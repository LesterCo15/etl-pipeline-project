from urllib.parse import urlencode, urljoin

def build_url(base_url, limit=None, offset=None):
    """
    Build a dynamic URL with optional limit and offset parameters.
    
    Args:
        base_url (str): The base API URL (e.g., "https://pokeapi.co/api/v2/pokemon")
        limit (int, optional): Number of items to fetch.
        offset (int, optional): Offset for pagination.
    
    Returns:
        str: Full URL with query parameters.
    """
    params = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset

    if params:
        return f"{base_url}?{urlencode(params)}"
    return base_url