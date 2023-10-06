from fastapi import FastAPI
import openai
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/chat/{message}")
async def chat(message: str):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": message}])
    return {"message": completion.choices[0].message.content}