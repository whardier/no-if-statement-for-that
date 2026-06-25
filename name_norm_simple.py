import json
from textwrap import dedent

from langchain_anthropic import ChatAnthropic
from langchain_core.callbacks import StdOutCallbackHandler
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

haiku = ChatAnthropic.model_validate(
    {
        "model": "claude-haiku-4-5-20251001",
        "temperature": 0,
    }
)

schema = {
    "properties": {
        "full_name": {
            "description": "The full name of the person",
            "maxLength": 150,
            "title": "Full Name",
            "type": "string",
        },
        "first_name": {
            "description": "The first name of the person",
            "maxLength": 50,
            "title": "First Name",
            "type": "string",
        },
        "last_name": {
            "description": "The last name of the person",
            "maxLength": 50,
            "title": "Last Name",
            "type": "string",
        },
        "email_address": {
            "description": "The email address of the person",
            "maxLength": 255,
            "title": "Email Address",
            "type": "string",
        },
    },
    "required": ["full_name", "first_name", "last_name", "email_address"],
    "title": "Schema",
    "type": "object",
}


system_prompt = dedent(
    """\
    You are a helpful assistant that extracts the given and family name from a full name and leverages the email address to help with the extraction
    if needed.  The potential name, given name, and family name may be inaccurate and should not be fully trusted. Please run a multi-step reasoning
    process to determine the most likely name, family name, and given name.

    - Women may no longer use their maiden name in some cultures.
    - Hyphenated names may be common in some cultures and may or may not indicate a family name.
    - Preserve middle initials in the full name but ensure it is not part of the following if you determine a middle initial is present.  Use the
      provided name parts and email to help.
        - Full Name
        - First name
        - Last name
    - Any middle initials should have a period after the initial.
    - Non family specific suffixes should be stripped.
    - Family specific suffixes like Jr., Sr., III, IV, etc. should be preserved.
        - Try to normalize any conflicts.
    """
)

user_prompt = dedent(
    """\
    Provided email: spencersr@gmail.com

    Potential full name: Shane R. Spencer III Esq. pH.D.
    Potential first name: Shaneypoo
    Potential last name:

    Please respond with a normalized full name, first name, and last name based on the above information.
    """
)

structured_haiku = haiku.with_structured_output(schema)

result = structured_haiku.invoke(
    [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt),
    ],
    config={"callbacks": [StdOutCallbackHandler()]},
)

print(json.dumps(result, indent=2))


examples = [
    HumanMessage(
        content=dedent(
            """\
            Provided email: spencersr@gmail.com

            Potential full name: Shane R. Spencer III Esq. pH.D.
            Potential first name: Shaneypoo
            Potential last name:

            Please respond with a normalized full name, first name, and last name based on the above information.
            """
        )
    ),
    AIMessage(
        content=dedent(
            """\
            {
                "full_name": "Shane R. Spencer III",
                "first_name": "Shane",
                "last_name": "Spencer",
                "email_address": "spencersr@gmail.com"
            }
            """
        )
    ),
    # ... MANY MANY MORE EXAMPLES
]

structured_haiku = haiku.with_structured_output(schema)

result = structured_haiku.invoke(
    [
        SystemMessage(content=system_prompt),
        *examples,
        HumanMessage(content=user_prompt),
    ],
    config={"callbacks": [StdOutCallbackHandler()]},
)

print(json.dumps(result, indent=2))
