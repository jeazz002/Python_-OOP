from typing import TypeVar, Generic, Callable, Optional, List, Iterator, Any

T = TypeVar('T')
R = TypeVar('R')

class TypedCollection(Generic[T]):

    def __init__(self) -> None:
        self._items: List[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def remove(self, item: T) -> None:
        if item not in self._items:
            raise ValueError("Элемент не найден")
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