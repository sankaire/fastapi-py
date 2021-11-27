from fastapi import FastAPI

# instance
app = FastAPI()


@app.get("/")
def root():
    return ({"message": "Welcome to my api!!"})


#path operation
@app.get("/post")
def get_post():
    return {"data": "This is your post"}
