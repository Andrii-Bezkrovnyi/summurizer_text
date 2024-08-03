from fastapi import FastAPI, Request
import uvicorn
import os
from langchain.chains.summarize import load_summarize_chain
from langchain_openai import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from dotenv import load_dotenv

load_dotenv()
API_KEY = ""
# Add OpenAI api key
openai_api_key = os.getenv("OPENAI_API_KEY", API_KEY)

app = FastAPI()


@app.post("/summarizer")
async def summarize(request: Request):
    # Download text data from json file
    data = await request.json()
    # Get text data from json file
    text_from_json = data.get("text", "")
    # Split the text
    spitting_text = CharacterTextSplitter()
    texts = spitting_text.split_text(text_from_json)
    # Create multiple documents
    docs = [Document(page_content=text) for text in texts]
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106", openai_api_key=openai_api_key)
    # Create chain
    chain = load_summarize_chain(llm, chain_type='map_reduce')
    result = chain.invoke(docs)

    return {"summary": result["output_text"]}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
