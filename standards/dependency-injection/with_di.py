from dependency_injector import containers, providers
from dependency_injection.wire import inject, Provide

class Container(containers.DeclarativeContainer):
    
    config = providers.Configuration()
    
    api_client = providers.Singleton(
        AppClient,
        api_key = config.api_key,
        timeout = config.timeout
    )
    
    service = providers.Factory(
        Service,
        api_client = api_client
    )
    
@inject
def main(service: Service = Provide[Container.service]) ->None:
    pass

if __name__ == "__main__":
    container = Container()
    container.config.api_key.from_env("API_KEY")
    container.config.timeout.from_env("TIMEOUT")
    container.wire(modules=[__name__])
    
    main() # automatice dependency injection
    
    with container.api_client.override(mock.Mock()):
        main()
    