# OpenAI API Text Summaraiasation

This is a rudementary code sample for text summaraisation using openai api.It uses the openai's text-davinci-002
model for summraisation.

[OpenAI API Reference](https://beta.openai.com/docs/api-reference/introduction)

[Text Summraisation Playground](https://beta.openai.com/playground/p/default-summarize)

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd open_ai_text_summraisation
   ```

4. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file into `src` folder

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

8. Run the script in src folder

   ```bash
   $ python summraisation.py
   ```

9. You can feed your input text within """ your text """ at `prompt` variable in summarisation file.

10. You can generate the summaraisation with different temperture setting ranging [0-1]. SUggested setting in between 0.5 to 0.7. 
