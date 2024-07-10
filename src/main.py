from abc import ABC, abstractmethod
from typing import Any
import uuid
import json
from datetime import datetime
import redis

class Task:
    # TODO:  Agregar un id a la tarea y un metodo para representar los valores
    def __init__(self, name:str, description: str):
        self.__name = name
        self.__description = description
        self.__id = f"Card:${uuid.uuid4()}"
        self.__creation_date = datetime.now().strftime("%d/%m/%y %H:%M:%S")

    def id(self) -> str:
        return self.__id

    def name(self) -> str:
        return self.__name

    def description(self) -> str:
        return self.__description

    def toJson(self):
        """
        HACK: Este parser puede ser util cuando necesitemos
        persistir la informacion en formato json en redis.
        """
        dumped_value = {
                "Task": {
                    "id": self.__id,
                    "title": self.__name,
                    "description": self.__description,
                    "creationDate": self.__creation_date
                    }
                }
        return json.dumps(dumped_value, sort_keys=True)
        

class Store(ABC):
    """
    Interface for store elements into database
    """
    @abstractmethod
    def connect(self, host: str, port: int) -> None:
        pass

    @abstractmethod
    def setCard(self, task: Task) -> None:
        pass

    @abstractmethod
    def getCard(self, taskName: str) -> Any: 
        return ""

class RedisStore(Store):

    def connect(self, host: str = "localhost", port: int = 6379) -> None:
        """
        This method should be executed before all others methods
        """
        self.__redis = redis.Redis(host=host, port=port, decode_responses=True)   

    def setCard(self, task: Task):
        self.__redis.set(name = task.id(), value= task.toJson())

    def getCard(self, taskName: str) -> Any:
        return self.__redis.get(taskName)


if __name__ == "__main__":
    store = RedisStore()
    store.connect()
    task: Task = Task(name="Basic task", description="Other simple task" )
    store.setCard(task)
    print(store.getCard("Basic task"))
    
