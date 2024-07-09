from abc import ABC, abstractmethod
from typing import Any
import redis

class Task:
    # TODO:  Agregar un id a la tarea y un metodo para representar los valores
    def __init__(self, name:str, description: str):
        self.__name = name
        self.__description = description

    def name(self) -> str:
        return self.__name

    def description(self) -> str:
        return self.__description
        


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
        self.__isConnected = True

    def setCard(self, task: Task):
        #TODO: Establecer un id y usar ese id como clave.
        self.__redis.set(name=task.name(), value=task.description())

    def getCard(self, taskName: str) -> Any:
        return self.__redis.get(taskName)


if __name__ == "__main__":
    store = RedisStore()
    store.connect()
    task: Task = Task(name="Simple task", description="example of simple task" )
    store.setCard(task)
    print(store.getCard("Simple task"))
    
