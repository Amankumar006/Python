# program 9
# pip install wikipedia-api pydantic

import wikipediaapi
from pydantic import BaseModel
from typing import List


class InstitutionProfile(BaseModel):
    founder: str = "Leland and jane stanford"
    established: int = 1885
    employee_count: int = 0
    branches: List[str] = ["Stanford"]
    summary: str = ""


name = input("enter institution name: ")
wiki = wikipediaapi.Wikipedia(
    user_agent="MyBot/1.0",
    language="en",
)

page = wiki.page(name)
if page.exists():
    profile = InstitutionProfile(
        summary=page.summary[:300],
    )
    print(profile.model_dump_json(indent=2))
else:
    print("wikipedia page does not exists")
