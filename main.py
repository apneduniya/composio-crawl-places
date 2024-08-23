from composio_crewai import ComposioToolSet, Action
from langchain_openai import ChatOpenAI
from crewai import Agent, Task, Crew
import dotenv
import json
from helpers import parse_json_garbage


dotenv.load_dotenv()  # Load env variables

llm = ChatOpenAI(model="gpt-4o")  # Initialize the language model
composio_toolset = ComposioToolSet()  # Initialize the composio toolset

# get the URL from the user
url = str(input("Enter the URL: "))

# Scrape the URL
scrape_action = composio_toolset.execute_action(action=Action.FIRECRAWL_SCRAPE, params={"url": url})

if not scrape_action['successfull']: # Checking if the scraping was successful
    print("Error scraping the URL", scrape_action['error'])
    exit()

scrape_data = scrape_action["data"]["response"]["data"]["content"] # Content of the website

# Initialize the location extracter agent
location_extracter_agent = Agent(
    role="Location Extracter Agent",
    goal="""A detailed summary of the location scraped from the website in JSON format.""",
    backstory="""You are an AI agent responsible for summarizing the location scraped from the website. 
        You need to summarize the location like name, address, place, address, website, phone number etc. as much as possible in JSON format.""",
    verbose=True,
    llm=llm,
    cache=False,
)

# Task to extract the location data from the website
extract_task = Task(
    description=f"""Summarize this content scraped from the website into detailed json containing all the possible data of the location mentioned in the website in JSON format.
    The format of the JSON should be like this:
    {{
        "name": "The name of the location",
        "address": "The address of the location",
        "place": "The place of the location",
        "website": "The website of the location",
        "phone": "The phone number of the location",
        ...
    }}

    Content of the website: ${scrape_data}""",
    agent=location_extracter_agent,
    expected_output="A json object containing all the possible data of the location mentioned in the website.",
    async_execution=True
)

# Initialize the crew
crew = Crew(
    agents=[location_extracter_agent],
    tasks=[extract_task],
    verbose=True,
)

result = crew.kickoff() # Execute the crew

# Parse the result into a json object using the parse_json_garbage() function, 
# so that even if the response is not a valid json, 
# it will extract the valid json present in the response
result_json = parse_json_garbage(result.raw)

print(json.dumps(result_json, indent=4))


# If you want to SAVE THE RESULT TO A FILE, uncomment the following line
# with open("result.json", "w") as f:
#     f.write(json.dumps(result_json, indent=4))