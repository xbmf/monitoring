import abc


class IConnectionProvider(abc.ABC):
    @abc.abstractmethod
    def connect(self):
        pass


class IManager(abc.ABC):
    @abc.abstractmethod
    def read_one(self, query, params=()) -> dict:
        pass

    @abc.abstractmethod
    def execute_update(self, query, params=()) -> int:
        pass

    @abc.abstractmethod
    def clean(self, inital_sql):
        pass
