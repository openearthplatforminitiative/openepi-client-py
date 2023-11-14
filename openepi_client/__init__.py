from pydantic_settings import BaseSettings


class OpenEpiSettings(BaseSettings):
    api_root_url: str = "https://api-test.openepi.io"


openepi_settings = OpenEpiSettings()
