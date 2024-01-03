from abc import ABC, abstractmethod


class Observable(ABC):

    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def update_observers(self, *args, **kwargs):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, *args, **kwargs):
        pass

