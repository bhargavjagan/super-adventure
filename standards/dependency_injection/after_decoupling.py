import os

class AppClient:

    def __init__(self, api_key: str, timeout : int ) -> None:
        self.api_key = api_key
        self.timeout = timeout

class Service:
    def __init__(self, api_client: AppClient) -> None:
        self.api_client : AppClient = api_client

def main(service: Service):
    pass

if __name__ == "__main__":
    api_key : str = os.getenv("API_KEY")
    timeout : int = int(os.getenv("TOKEN"))
    main(
        Service(
            AppClient(
                api_key=api_key,
                timeout = timeout
            )
        )
    )
    