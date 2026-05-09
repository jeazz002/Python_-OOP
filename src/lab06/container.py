from typing import TypeVar, Generic, Callable, Optional, List, Iterator, Protocol, Any

class Displayable(Protocol):
    def display(self) -> str: ...

class Scorable(Protocol):
    def score(self) -> float: ...

T = TypeVar('T')
R = TypeVar('R')

class TypedCollection(Generic[T]):
    def __init__(self, item_type: type[T]) -> None:
        """
        :param item_type: Ожидаемый тип хранимых объектов (для runtime-проверки).
        """
        self._item_type: type[T] = item_type
        self._items: List[T] = []

    def add(self, item: T) -> None:
        """Добавляет элемент с проверкой типа."""
        if not isinstance(item, self._item_type):
            raise TypeError(f"Ожидается {self._item_type}, получен {type(item)}")
        self._items.append(item)

    def remove(self, item: T) -> None:
        if item not in self._items:
            raise ValueError("Элемент не найден в коллекции")
        self._items.remove(item)

    def get_all(self) -> List[T]:
        return self._items.copy()

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)

    def __getitem__(self, index: int) -> T:
        return self._items[index]

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> List[R]:
        return [transform(item) for item in self._items]

    def sort_by(self, key_func: Callable[[T], Any], reverse: bool = False) -> 'TypedCollection[T]':
        self._items.sort(key=key_func, reverse=reverse)
        return self

    def filter_by(self, predicate: Callable[[T], bool]) -> 'TypedCollection[T]':
        new_coll = TypedCollection(self._item_type)
        for item in self._items:
            if predicate(item):
                new_coll.add(item)
        return new_coll

    def apply(self, func: Callable[[T], None]) -> 'TypedCollection[T]':
        for item in self._items:
            func(item)
        return self

    def __str__(self) -> str:
        if not self._items:
            return "Коллекция пуста"
        return "\n".join(str(item) for item in self._items)