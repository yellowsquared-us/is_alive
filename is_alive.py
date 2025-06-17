from prefect import flow
from pathlib import Path
import httpx


@flow
def main() -> list[str]:
    response = httpx.get("https://api.yellowsquared.us/health")
    response.raise_for_status()
    assert response.json()["status"] == "healthy"


if __name__ == "__main__":
    # main.from_source(
    #     source=str(Path(__file__).parent),
    #     entrypoint="is_alive.py:main",
    # ).deploy(
    #     name="is_alive",
    #     work_pool_name="api_status"
    # )
    main()