import abc


class IConsumer(abc.ABC):
    @abc.abstractmethod
    def start(self):
        pass
