# FastAPI Text Summarizer via LangChain

## Setup instrictions:
### 1. Create a virtual environment:

`python -m venv env`

### On Windows use `env\Scripts\activate`

### 2. Install dependencies:
```shell
pip install -r  requirements.txt
```
### 3. Insert your OpenAI API Key.
Create file .env and add there `YOUR_API_KEY` with your OpenAI API Key or add 
this API KEY in the `main.py` file.

## How run the code:
### 1. Run the application:
Run the code: 

`python main.py`

### 2. Test the endpoint:

Send a POST request to http://127.0.0.1:8000/summarizer with a JSON body containing the text to be summarized.

### Test code:
You can run the program test_main.py for testing the code;

```shell
python test_main.py
```
