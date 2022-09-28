import os
import openai
import configobj


config = configobj.ConfigObj('.env')
apikey = config['OPENAI_API_KEY']
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = apikey
#prompt = input("""Enter your text here>""")

response = openai.Completion.create(
  model="text-davinci-002",
  #prompt="Summarize this for a second-grade student:\n\nAs an AP developer I would like to implement a lambda function that will capture the ODS data related to a CI and put it into a CSV file and finally send it to the Big Panda for correlation operation. The Lambda will perform few cleanup and data preprocessing before sending it to the BigPanda.",
  prompt = """Of all the reasons Python is a hit with developers, one of the biggest is its broad and ever-expanding selection of third-party packages. Convenient toolkits for everything from ingesting and formatting data to high-speed math and machine learning are just an import or pip install away.

But what happens when those packages don’t play nice with each other? What do you do when different Python projects need competing or incompatible versions of the same add-ons? That’s where Python virtual environments come into play.""",
  temperature=0.1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
print()
print("*" * 60)
print(response["choices"][0]["text"])
print()
print("*" * 60)
