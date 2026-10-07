# Example from python/05-oop-design.md; keep in sync with the lesson.
from abc import ABC, abstractmethod

class Retriever(ABC):
    @abstractmethod
    def search(self, query: str) -> list[str]:
        """Nhận query đã chuẩn hóa; không có kết quả thì trả list rỗng."""
        raise NotImplementedError

class MemoryRetriever(Retriever):
    def __init__(self, notes: list[str]):
        self._notes = list(notes)

    def search(self, query: str) -> list[str]:
        return [note for note in self._notes if query in note.lower()]

class EmptyRetriever(Retriever):
    def search(self, query: str) -> list[str]:
        return []

class NoteService:
    def __init__(self, retriever: Retriever):
        self._retriever = retriever

    def find(self, query: str) -> list[str]:
        if not query.strip():
            raise ValueError("query must not be blank")
        return self._retriever.search(query.strip().lower())

service = NoteService(MemoryRetriever(["Python OOP", "SQL joins"]))
assert service.find(" OOP ") == ["Python OOP"]
assert NoteService(EmptyRetriever()).find("oop") == []
print("P05 OK: interchangeable retrievers")
