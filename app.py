from fastapi import FastAPI

app = FastAPI()
users_list = [
        {"name": "John Doe", "active": True},
        {"name": "Inna Inna", "active": False}
    ]

@app.get("/")
async def root():
    print("User requested root URL")
    return {"message": "Hello world!"}

@app.get("/users/")
async def users(active: int = 1):
    print("User requested user URL")
    if active == 1:
        active_users = [x for x in users_list if x["active"]]
        return {"data": active_users}
    return {"data": users_list}
