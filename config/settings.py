from loadenv import EnvEnum


class Secrets(EnvEnum):
    GOOGLE_MAPS_API_KEY: str = ()
    OPENAI_API_KEY: str = ()
    APP_HOST: str = ()
    APP_PORT: str = ()
