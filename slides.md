---
theme: default
colorSchema: dark
background: assets/tim-gouw-1K9T5YiZ2WU-unsplash-darklow.jpg
title: No if statement for that
class: text-center pb-80
drawings:
  persist: false
transition: slide-left
comark: true
duration: 35min
---

# **No `if` Statement for That**

Simple, reliable LLM solutions to hard problems — with **LangChain**, **LangGraph**, and the **Anthropic API**

<div class="abs-br m-6 text-4xl">
  <div style="color: #7FC8FF" class="slidev-icon-btn">
      <simple-icons:langchain/>
  </div>
  <div style="color: #7FC8FF" class="slidev-icon-btn">
      <simple-icons:langgraph/>
  </div>
  <div style="color: #FF00FF" class="slidev-icon-btn">
    <bx:plus/>
  </div>
  <div class="slidev-icon-btn">
    <simple-icons:anthropic/>
  </div>
  <div style="color: #FFFF00" class="slidev-icon-btn">
    <bx:infinite/>
  </div>
  <div style="color: #FF0000" class="slidev-icon-btn">
    <bx:bxs-heart-circle/>
  </div>
</div>

<!--
Hi.. I'm Shane - if you know me then great (maybe?).. if not then that's the next slide.

This is - "No If Statement for That" .. a talk on LangChain, LangGraph, and leveraging the Anthropic API as well as some Anthropic partner models through a few demos.

The premise here is — as software developers we are faced with the challenge of building logic  that seems simple enough - but is much harder and more expensive to implement than inspiration lead us to believe.

So often enough — there is no if statement for that...  That is this talk.
-->

---
transition: fade
layout: image-right
image: /assets/me.jpg
---

# **Who am I?**
I'm just me.

Software developer with a focus on building LLM-powered applications and exploring spec-driven development.

Long history in traditional software development (over 20 years of experience in various domains including health tech
and consulting).

Husband and dad.  Eight-year-old child as seen in the picture (foot only).

<!--
As pictured here, this is me. I've been a software developer for quite a while, well over 20 years, and have a huge history in systems engineering as well as creating Software-as-a-Service solutions. I love Linux. I love Python. I love all sorts stuff.

I'm also a husband and a dad, and you can see the 8-year-old's part of the picture here, just the foot though. He thought that was pretty funny and loves to do it often.

In my current role at a health tech startup, we are working through quite a few things related to AI, including how to automate things and then also how to automate software development itself using various methodologies. I'm deep in it enough that it seemed like a good idea for me to do a talk for you all today.
-->

---
transition: slide-up
layout: two-cols-header
layoutClass: gap-4
---

# **What `if`?**

 … models aren’t just for building software.

::left::

## Logic can be hard to build — even if you have an LLM build it.

Ordinary language problems — normalizing messy names, deduping records, enriching a search index — are deceptively expensive the conventional way: brittle rules, regex, custom dictionaries, labeled data. Simple to describe, but a full project to build and maintain over time and keep relevant.

::right::

## Putting models into the pipeline.

What if Haiku ran embedded in the pipeline as the daily driver — quietly handling the high-volume normalization and tagging at every step — with Sonnet or Opus reserved for the cases that need deeper reasoning? The expensive build becomes a model call with a schema, woven into the process rather than bolted on.

<!--
Sometimes the cost of building logic the conventional way is high, even for seemingly simple tasks. This is where LLMs can provide a more efficient solution.

Ordinary language problems like normalizing messy names, cleaning records, or enriching a search index can be deceptively expensive to solve.

... and we have to ask ourselves now that LLMs can handle complex logic, how should we rethink the way we build and maintain software solutions to handle these ordinary but complex language tasks?

For instance - one that we will dive in to right away has to deal with name normalization in authorization or onboarding processes where we are given un-sanitized or inaccurate details... yet need to conform and resolve the name into a standardized format.
-->

---
transition: slide-up
---

# **What is LangChain?**
 … yet another chain thing to think about.

Open-source framework for building LLM apps. Provides reusable components (prompts, models, parsers, retrievers, 700+
integrations) composed into linear chains via LCEL (prompt | model | parser).

- Retrieval Augmented Generation (RAG)
- Structured extraction
- Summarization
- Simple chatbots — single-pass
- Predictable workflows and actions

LCEL Example:

```python {*}{lines:true}
chain = prompt | model | output_parser
crazy_chain = prompt1 | model_fast | StrOutputParser() | prompt2 | model_creative | StrOutputParser()
```

<div class="abs-bl m-6">
  <img src="/assets/langchain-dark.svg" alt="LangChain" style="height: 32pt;" />
</div>

<div class="abs-br m-6 text-4xl">
  <div class="slidev-icon-btn">
      <devicon:python/>
  </div>
  <div class="slidev-icon-btn">
      <devicon:nodejs/>
  </div>
</div>

<!--
Simply put.. LangChain is an open source framework for building applications with large language models (LLMs), providing reusable components and tools to create complex workflows and integrations.

I've been using it for RAG (Retrieval Augmented Generation) scenarios, where it helps integrate external knowledge sources into LLM workflows for more accurate and context-aware responses.

Lately I've been leveraging it a LOT for structured extraction... where I've been creating strict JSON schemas defining what a markdown file should contain.. and in what order.. and use structured extraction to ensure nothing is missed as summarization and analysis is done to do the work.
-->

---
transition: slide-up
---

# **What is LangGraph?**
… yet another graph thing to think about.

An orchestration layer built on LangChain for stateful workflows. Models work together as nodes/edges in a graph with optional cycles/loops, shared state, retries, and human-in-the-loop pauses.

- Agents
- Multi-agent systems
- Dynamic graph fan out / fan in
- Retry/quality-gate logic
- Anything needing loops or durability.

Runs locally and in standardized runtime environments like LangGraph Platform, AWS Bedrock AgentCore, and beyond.

<div class="abs-bl m-6">
  <img src="/assets/langgraph-dark.svg" alt="LangGraph" style="height: 32pt;" />
</div>

<div class="abs-br m-6 text-4xl">
  <div class="slidev-icon-btn">
      <devicon:python/>
  </div>
  <div class="slidev-icon-btn">
      <devicon:nodejs/>
  </div>
</div>

<!--
Once we need to make these chains a bit more durable and enable more complex workflows with retries and leverage fan in/out patterns and loops, LangGraph provides the orchestration layer to manage it.

Langgraph can run as part of your service runtime (Python, Node, whatever...) or operate as a hosted service.

You get started here by describing, in code, what a graph connections look like following node and edge based definitions and can involve custom logic into the described graph that can ultimately fail or bring in the great "Eval Loop" or "AI Ops" that bring interactions into the process for quality control, workflow requirements, and what have you.
-->

---
transition: slide-up
layout: two-cols-header
layoutClass: gap-4
---

# **The Anthropic API**
… more than just model access.

It starts with the Messages API for model calls — but ships with the production tooling around it, so the hard parts come built-in.

::left::

### Model access

- Messages API
- Extended thinking
- Structured outputs

::right::

### Server provided tools

- Web search & web fetch
- Sandboxed code execution
- Memory tools

<div class="abs-bl m-6">
  <img src="/assets/Anthropic logo - Ivory.svg" alt="Anthropic" style="height: 24pt;" />
</div>

<div class="abs-br m-6 text-4xl">
  <div class="slidev-icon-btn">
      <emojione:thinking-face/>
  </div>
  <div class="slidev-icon-btn">
      <emojione:building-construction/>
  </div>
  <div class="slidev-icon-btn">
      <emojione:gear/>
  </div>
  <div class="slidev-icon-btn">
      <emojione:magnifying-glass-tilted-left/>
  </div>
  <div class="slidev-icon-btn">
      <devicon:json/>
  </div>
</div>

<!--
Software like Claude Code and Cloud Desktop and Cowork and so on typically use Anthropic API endpoints to access models, but not everyone knows that the APIs provide a lot of tools.

You might have seen tools when using Claude Code where it's doing things like running bash or running a web search or something similar to that. More often than you'd think, that is a remote tool execution and not a local one.

For the folks that are leveraging Anthropics APIs through SDKs or through off-the-shelf software, often that integration will intentionally enable remote tool execution like web fetch and web search - which is supported by specific teams at Anthropic responsible for providing the infrastructure allowing models to act as regular web users - as well as all the agreements that often need to be set up to enable servers at Anthropic to reach most popular web sites and services.

There are a few other tools.. and this list is by no means comprehensive.
-->

---
transition: fade
layout: two-cols
layoutClass: gap-4
---

::left::

# **LangChain + ChatAnthropic**
First-class Anthropic API support with remote tool execution.

<div style="--slidev-code-font-size: 9px; --slidev-code-line-height: 11px;">

```python {*}{lines:true}
import json

from langchain_anthropic import ChatAnthropic

haiku = ChatAnthropic.model_validate(
    {
        "model": "claude-haiku-4-5-20251001",
        "temperature": 0,
    }
)

result = haiku.invoke("Is this thing on?")

print(result.text)
```

```text {*}{lines:true}
Yep, I'm here and ready to help! What's on your mind?
```

</div>

::right::

- 🤖 Full model suite
- 📝 Variable context window
- 🛠️ Server-side tool calling
- 🏗️ Structured output
- 🎟️ Token-level streaming
- 🔀 Fully asynchronous
- 🖼️ Image input

<!--
Here is a little source code and then a bit of a primer on what exactly LangChain is able to leverage that Anthropic provides.
-->

---
layout: cover
background: assets/citybackground-cyan.jpg
transition: fade
class: pb-80
---

# **Questions so far?**

<div class="abs-br mr-8">
  <img src="/assets/idk.png" style="height: 280pt;" />
</div>

---
transition: slide-up
---

# **Onboarding Name Normalization**
Given the following limited parameters  we need to attempt to extract and normalize name information into our platforms
standard for a full name as well as extracts for first and last name:

```json
{First} ({M.}) {Last} ({Valid suffixes})
```

```
Shane R. Spencer
Dale Earnhardt Jr.
William Henry Gates III
```

Integration provided parameters:

- Full Name <span style="color:#555555">(Optional)</span>
- First Name
- Last Name <span style="color:#555555">(Optional)</span>
- Email Address

<!--
Okay, so here is a common enough issue that is very difficult to solve using regular expressions or natural language processing tools that often comes up for SaaS. I've also found some of these platforms that enable social integrations, like being able to log in with LinkedIn or Facebook.

(( riff on data exchange ))

So I love theoretically solving this through LLMs and leveraging a lesser-used one that Anthropic provides called Haiku to do some of this work because it is super fast and more than capable of handling some of the work that I'm about to demo.
-->

---
transition: slide-up
layout: two-cols
layoutClass: gap-4
---

::left::

# **Key Considerations**

- Our user schema is focused on western style name definitions which are aligned closely with many enterprise and SaaS
  standards.
- We will want to support a “Full Name” which is user editable and not always composed of the first and last name.
- The “Full Name” should be reasonable and not encourage excessive suffixes.
- Needs to be a fast analysis and should leverage zippier models.
- The output of the LLM invocation should be structured toward our user schema.

::right::

<div style="--slidev-code-font-size: 8px; --slidev-code-line-height: 11px;">

```python {*|3,5,9,11,15,17,21,23|3,4,9,10,15,16,21,22|28-30}{lines:true}
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
    "required": [
      "full_name", "first_name", "last_name", "email_address"
    ],
    "title": "Schema",
    "type": "object",
}
```

</div>

<div class="text-center">
<small>Named Entity Recognition (NER) enablement through JSONSchema</small>
</div>

<!--
Key considerations.

User schema is focused on Western-style names, which aligns pretty well with enterprise and SaaS standards.

We are going to make an assumption that we will have a full name being passed back to us, which could not actually be full.

We're going to have some weird suffixes.

We're going to have some weird prefixes.

It can't take forever to get feedback from a model doing the cleanup.

We will want to leverage the structured data tool at Anthropic to ensure we are complying with our data standard. We will use named entity recognition (NER) or concepts that are very similar to that to ensure that the descriptions and limits in the schema are adhered to and leveraged during the evaluation process.
-->

---
transition: slide-up
---

<div style="--slidev-code-font-size: 8px; --slidev-code-line-height: 11px;">

```python {*}{lines:true}
from textwrap import dedent

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
```

```python {*}{lines:true}
user_prompt = dedent(
    """\
    Provided email: spencersr@gmail.com

    Potential full name: Shane R. Spencer III Esq. pH.D.
    Potential first name: Shaneypoo
    Potential last name:

    Please respond with a normalized full name, first name, and last name based on the above information.
    """
)
```

</div>

---
transition: slide-up
---

<div style="--slidev-code-font-size: 8px; --slidev-code-line-height: 11px;">

```python {*}{lines:true}
import json
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.callbacks import StdOutCallbackHandler

structured_haiku = haiku.with_structured_output(schema)

result = structured_haiku.invoke(
    [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt),
    ],
    config={"callbacks": [StdOutCallbackHandler()]}
)

print(json.dumps(result, indent=2))
```

Result:

```shell {*}{lines:true}
❯ uv run ./normalize_name_demo.py
> Entering new RunnableSequence chain...
> Entering new JsonOutputKeyToolsParser chain...
> Finished chain.
> Finished chain.
{
  "full_name": "Shane R. Spencer III",
  "first_name": "Shane",
  "last_name": "Spencer",
  "email_address": "spencersr@gmail.com"
}
```

</div>

---
transition: fade
---

**Normalized Name Extraction** (Full Demo Script)

<div style="--slidev-code-font-size: 8px; --slidev-code-line-height: 11px;">

```python {*}{lines:true,maxHeight:'24em'}
# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "langchain",
#     "langchain-anthropic",
# ]
# ///


import json
from textwrap import dedent

from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.callbacks import StdOutCallbackHandler

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
```

</div>

---
layout: cover
background: assets/citybackground-orange.jpg
transition: fade
class: pb-80
---

# **But wait!** Isn’t that<br/>**ZeroShot** prompting?

# What about<br/>**FewShot** and<br/> **ManyShot**?

<div class="abs-br mr-10">
  <img src="/assets/correction.png" style="height: 280pt;" />
</div>

---
transition: slide-up
---

## ZeroShot vs. FewShot/ManyShot prompting

Short and sweet... FewShot adds in examples of good/bad prompts to guide the model towards the desired output.

<div style="--slidev-code-font-size: 8px; --slidev-code-line-height: 11px;">

```python {*}{lines:true}
examples = [
    HumanMessage(
        content=dedent(
            """\
            Provided email: bobber@gmail.com

            Potential full name: Bobby
            Potential first name: Bob
            Potential last name: Smith

            Please respond with a normalized full name, first name, and last name based on the above information.
            """
        )
    ),
    AIMessage(content='{"full_name": "Bob Smith", "first_name": "Bob", "last_name": "Smith", "email_address": "bobber@gmail.com"}'),
    # ... MANY MANY MORE EXAMPLES
]

result = structured_haiku.invoke(
    [
        SystemMessage(content=system_prompt),
        *examples,
        HumanMessage(content=user_prompt),
    ],
    config={"callbacks": [StdOutCallbackHandler()]},
)
```

</div>

---
transition: slide-up
layout: two-cols
layoutClass: gap-4
---

::left::

# **LangChain + VoyageAIEmbedding + Vector Stores**
Anthropic partner model for embedding generation and integration with vector stores for efficient Retrieval-Augmented
Generation (RAG).

VoyageAI provides embedding models like:

- `voyage-4-large`
- `voyage-4`
- `voyage-4-lite`
- `voyage-code-3`
- `voyage-finance-2`
- `voyage-law-2`

::right::

<div style="--slidev-code-font-size: 9px; --slidev-code-line-height: 11px;">

```python {*}{lines:true}
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_voyageai import VoyageAIEmbeddings

voyageai = VoyageAIEmbeddings.model_validate(
    {
        "model": "voyage-4-large"
    }
)

vector_store = InMemoryVectorStore(embedding=voyageai)

documents = [
    Document(page_content="See spot run."),
    Document(page_content="The quick brown fox jumps over the lazy dog."),
    Document(page_content="Jack and Jill went up the hill to fetch a pail of water."),
    Document(page_content="Mary had a little lamb, its fleece was white as snow."),
    Document(page_content="Twinkle, twinkle, little star, how I wonder what you are."),
    Document(page_content="Baa, baa, black sheep, have you any wool?"),
]

vector_store.add_documents(documents=documents)

for result, score in vector_store.similarity_search_with_score("little star", k=2):
    print(result.page_content)
    print(score)
```

```text {*}{lines:true}
Twinkle, twinkle, little star, how I wonder what you are.
0.46529671405143924
Mary had a little lamb, its fleece was white as snow.
0.24701678083647283
```

</div>

---
transition: slide-up
layout: two-cols-header
layoutClass: gap-4
---

# **What is "Embedding"?**
An embedding is a numerical representation of data, such as text, in a high-dimensional vector space. Embeddings capture the semantic meaning of the data, allowing similar items to be compared and retrieved efficiently using vector operations.

::left::

| Input |
| - |
| `The king was wise.` |
| `The queen reigned.` |
| `a faithfull dog.` |
| `a cat napping.` |

::right::

| Word | Embedding |
| - | - |
| `QUEEN` -> | \[0.12, -0.34, 0.56, -0.78\, ..., 0.67] |
| `WISE` -> | \[0.10, -0.32, 0.54, -0.76\, ..., 0.65] |
| `NAPPING` -> | \[0.09, -0.31, 0.53, -0.75\, ..., 0.64] |
| ... | ... |
| `KING` -> | \[0.11, -0.33, 0.55, -0.77\, ..., 0.66] |

---
transition: slide-up
layout: image-right
image: assets/Gemini_Generated_Image_i465jhi465jhi465.png
---

# **No really... What is "Embedding"?**
I don't have the maths.

Really.. this is just vector math (maths?) which is way... way... above my pay grade.

I can however go over how to optimize information before processing embedding data on a text stream so that document
based vectors stores operate more efficiently.

*In theory.*

<div class="abs-br pr-60">
  <img src="/assets/studyhard.png" style="height: 320pt;" />
</div>


---
transition: slide-up
---

<div style="--slidev-code-font-size: 9px; --slidev-code-line-height: 11px;">

```python {*}{lines:true}
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_voyageai import VoyageAIEmbeddings

voyageai = VoyageAIEmbeddings.model_validate(
    {
        "model": "voyage-4-large"
    }
)

vector_store = InMemoryVectorStore(embedding=voyageai)

# Load "Alice's Adventures in Wonderland" int separate lines (not as paragraphs)
lines = open("alice_in_wonderland.txt").read().splitlines()

# Sanitize lines by removing empty ones and give each line a unique ID.
lines = [line for line in lines if line.strip()]
line_ids = [str(i) for i in range(len(lines))]
lines_by_id = {line_id: line for line_id, line in zip(line_ids, lines)}

# Add each line as separate documents in the vector store and associate each document with its unique ID.
documents = [Document(page_content=line) for line_id, line in lines_by_id.items()]

vector_store.add_documents(documents=documents, ids=line_ids)

for result, score in vector_store.similarity_search_with_score("alice argues with a caterpillar", k=5):
    print(repr(result), score)
```

```text {*}{lines:true}
Document(id='791', metadata={}, page_content='Alice felt a little irritated at the Caterpillar’s making such _very_') 0.5804435614733033
Document(id='796', metadata={}, page_content='good reason, and as the Caterpillar seemed to be in a _very_ unpleasant') 0.53776820761672
Document(id='773', metadata={}, page_content='“What do you mean by that?” said the Caterpillar sternly. “Explain') 0.5251984448904545
Document(id='777', metadata={}, page_content='“I don’t see,” said the Caterpillar.') 0.5034927410008277
Document(id='849', metadata={}, page_content='“That is not said right,” said the Caterpillar.') 0.5034492832061114
```

</div>

---
transition: slide-up
---

# How to enrich the embedding process?
No code edition.

- Process the last 50 lines together and create a rolling window "Document" that:
  - Performs X to English translation that also transforms words against a graded text corpus (10th grade reading level, 4th
    grade, ...)
  - Expands concepts into a shared terminology or ontology.
    - Could be as simple as combining common words with their synonyms available in the graded text corpus.
  - Composes into a single document containing:
    - A summary of what has happened up until this last line in the rolling window of text.
    - The actual line both as is AND as transformed against the selected corpus.

Very useful for driving software development and research tasks as a way to handle document selection quickly and pull
in only relevant context for an operation or deep dive.

---
transition: slide-up
---

# How to improve the searching process?
You've got to know when to hold 'em, know when to fold 'em

- For all search terms we need to expand them similarly to how we enriched and normalized the embeddings by using an LLM
  to process the term.
  - Potentially fan out several sets of search terms to get multiple result streams going.
- Ensure that the matchers (post filtering) contain a reduced set of terms.
- Overselect (want 5.. select the top 50)
- Filter the overselection (could be an LLM process).

Ideally this would be able to efficiently search all of popular fiction in Project Gutenberg without having to load it
into context.

All of the above can be defined as a graph and executed using LangGraph in order to parallelize LLM operations and then
filter results into the final selection process.

---
layout: cover
background: assets/citybackground-cyan.jpg
transition: fade
class: pb-80
---

# **Thank you.. and now on to questions and possible answers time...**

<div class="abs-br mr-8">
  <img src="/assets/doublethumbs.png" style="height: 280pt;" />
</div>
