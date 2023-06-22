"""
Write an Service that requires a api_client and the api_client required the api_key and timeout from the os variables
"""

import os

class ApiClient:
    
    def __init__(self) -> None:
        self.api_key = os.getenv("API_KEY") # dependency
        self.timeout = os.getenv("TIMEOUT") # dependency


class Service:

    def __init__(self) -> None:
        self.api_client : ApiClient = ApiClient() # dependency

def main() -> None:
    service = Service()

if __name__ == "__main__":
    main()