from fastapi import FastAPI



apiapp = FastAPI()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(apiapp, host="localhost", port=8000)