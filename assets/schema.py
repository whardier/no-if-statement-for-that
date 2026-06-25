from typing import Annotated

from pydantic import BaseModel, Field


class Schema(BaseModel):
    full_name: Annotated[
        str, Field(description="The full name of the person", max_length=150)
    ]
    first_name: Annotated[
        str, Field(description="The first name of the person", max_length=50)
    ]
    last_name: Annotated[
        str, Field(description="The last name of the person", max_length=50)
    ]
    email_address: Annotated[
        str, Field(description="The email address of the person", max_length=255)
    ]


if __name__ == "__main__":
    import json

    print(json.dumps(Schema.model_json_schema(), indent=2))
