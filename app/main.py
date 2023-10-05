from fastapi import FastAPI
import openai
app = FastAPI()


@app.get("/")
async def root():
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
    return {"message": completion.choices[0].message.content}
