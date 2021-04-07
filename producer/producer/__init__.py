import abc


class IProducer(abc.ABC):
    @abc.abstractmethod
    def publish(self, message, topic):
        pass
