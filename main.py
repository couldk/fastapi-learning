from fastapi import FastAPI

#创建fastapi实例
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/hellow")
async def get_hellow():
    return {"msg": "Hello FastApi"}

@app.get("/user/hellow")
async def study():
    return {"msg": "我正在学习 FastApi"}

@app.get("/book/{id}")
async def get_book(id: int):
    return {"id": id ,"title":f"这是第{id}本书"}

@app.get("/user/{useer_id}")
async def get_userId(useer_id: int):
    return {"useer_id": useer_id ,"name":f"普通用户{useer_id}"}
