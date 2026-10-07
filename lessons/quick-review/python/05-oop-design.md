# P05 · Encapsulation, inheritance, polymorphism và composition

[Mục lục](../README.md) · [Bài trước](04-oop-basics.md) · [Bài sau](06-python-patterns.md)

**Mục tiêu:** hiểu bốn ý tưởng OOP và chọn cách ghép code đơn giản. **Thời lượng đọc:** khoảng 20 phút.

## Bốn ý tưởng qua cùng một ví dụ

| Ý tưởng | Ý nghĩa | Ví dụ tra cứu ghi chú |
| --- | --- | --- |
| Encapsulation | Gom state/hành vi và kiểm soát cách thay đổi để giữ invariant | Thay nội dung qua method có validation |
| Abstraction | Người dùng giao diện chỉ cần biết contract cần thiết | Gọi `search(query)` mà không cần biết dữ liệu ở file hay DB |
| Inheritance | Kiểu con kế thừa/mở rộng hành vi kiểu cha | Hai retriever cùng tuân thủ giao diện Retriever |
| Polymorphism | Cùng một thao tác, nhiều implementation phù hợp contract | Service gọi search trên một retriever bất kỳ phù hợp |

`_name` là quy ước non-public; `__name` dùng name mangling, không phải hàng rào bảo mật. `property` cho phép giao diện giống attribute nhưng có getter/setter để bảo vệ quy tắc. Đừng xem các cơ chế này như authorization.

**Composition** là “có một”: service có một retriever. **Inheritance** là quan hệ kiểu con có thể thay thế kiểu cha đúng contract. Nếu cần đổi cách lưu dữ liệu, truyền retriever vào service thường dễ kiểm thử hơn để service kế thừa database client.

## Ví dụ inheritance + composition, hoàn toàn không gọi AI

```python
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
```

[File chạy được](../examples/p05.py). `NoteService` không đổi khi đổi implementation. Đây là dependency injection qua constructor. Input query được giả định là chuỗi ở ví dụ này; boundary nhận JSON cần kiểm kiểu riêng.

## ABC, duck typing và Protocol

`ABC`/`abstractmethod` giúp khai báo lớp trừu tượng và ngăn tạo instance khi còn abstract method chưa cài. Duck typing dựa vào hành vi object cung cấp. `typing.Protocol` mô tả structural interface cho công cụ kiểm kiểu: class có method phù hợp không nhất thiết kế thừa Protocol. Annotation không tự kiểm đầy đủ contract lúc chạy.

SOLID chỉ cần nhớ mục đích trước: **S** chia trách nhiệm; **O** mở rộng qua giao diện phù hợp; **L** kiểu con giữ contract; **I** giao diện vừa đủ cho bên dùng; **D** phụ thuộc abstraction. Đây là hướng dẫn thiết kế, không phải yêu cầu tạo năm tầng class cho mỗi bài.

## Tự kiểm

1. Nếu một retriever trả None khi không tìm thấy, nó có thay thế implementation trên được không?
2. Service và retriever là “is-a” hay “has-a”?
3. Class con override search nhưng không kế thừa code tìm kiếm có còn đa hình không?

<details>
<summary>Đáp án ngắn</summary>

1. Không đúng contract list rỗng; caller có thể lỗi. 2. Has-a, composition. 3. Có; đa hình nằm ở giao diện/hành vi thay thế được, không đòi dùng chung implementation.

</details>

**Bài tập 20 phút:** thêm `ExactRetriever` so khớp toàn bộ nội dung; giữ nguyên service. Giải thích vì sao không dùng inheritance từ `NoteService` để làm việc này.

**Nguồn:** [abc](https://docs.python.org/3/library/abc.html), [Protocols](https://docs.python.org/3/library/typing.html#typing.Protocol), [Dependency Injection](https://martinfowler.com/articles/injection.html). Đi sâu theo [A.2](../../../ROADMAP.md#a-2).
