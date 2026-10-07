# Example from python/04-oop-basics.md; keep in sync with the lesson.
from dataclasses import dataclass, field

@dataclass
class StudyNote:
    title: str
    tags: list[str] = field(default_factory=list)

    def add_tag(self, tag: str) -> None:
        if not isinstance(tag, str) or not tag.strip():
            raise ValueError("tag must be non-empty text")
        normalized = tag.strip()
        if normalized not in self.tags:
            self.tags.append(normalized)

    @classmethod
    def from_title(cls, title: str) -> "StudyNote":
        return cls(title=title.strip())

first = StudyNote.from_title("  Python  ")
second = StudyNote("OOP")
first.add_tag("language")
assert first.tags == ["language"]
assert second.tags == []
assert first == StudyNote("Python", ["language"])
assert first is not StudyNote("Python", ["language"])
print("P04 OK:", first)
