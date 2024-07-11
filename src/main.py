from abc import ABC, abstractmethod
from typing import Any
from surrealdb import Surreal
import asyncio

class Task:
    def __init__(self, title:str, description: str):
        self.__title = title
        self.__description = description

    def title(self) -> str:
        return self.__title

    def description(self) -> str:
        return self.__description

class Store(ABC):
    # Interface for store elements into database
    @abstractmethod
    async def connect(self, ):
        pass

    @abstractmethod
    async def setCard(self, task: Task) -> None:
        pass

    @abstractmethod
    async def getCard(self, title: str) -> Any: 
        pass

class SurrealStore(Store):

    async def connect(self):
        self.db = Surreal("ws://localhost:8000/rpc")
        await self.db.connect()
        await self.db.signin({"user": "root", "pass": "root"})
        await self.db.use("test", "test")

    async def setCard(self, task: Task) -> None:
        """
        Ejemplo de envio de eventos en cada insercion.
        Estos eventos son escuchados por la base de datos
        y pueden ser consumidos desde la misma db o usando un
        sdk de javascript como figura en la documentacion.
        """
        
        data = await self.db.live(table="task", diff=False)
        await self.db.create(f"task:1", {
            "title": task.title(),
            "description": task.description()
            })
        print(data)


    async def getCard(self, title: str) -> Any:
        return await self.db.select(title)

    async def removeCard(self, title: str):
        return await self.db.delete(title)

async def main():
    store = SurrealStore()
    await store.connect()
    task: Task = Task(title="Basic task", description="Other simple task" )
    await store.removeCard("task:1")
    await store.setCard(task)
    print(await store.getCard("task:1"))

if __name__ == "__main__":
    asyncio.run(main())
    exit(0)
    
