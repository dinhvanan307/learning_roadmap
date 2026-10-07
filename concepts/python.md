# Python và tư duy lập trình

[Danh mục concept](../docs/CONCEPTS.md) · [Roadmap](../ROADMAP.md)

**Học trong:** [A1](../learning-path/ai-application-engineer/programs/a-python/courses/python-programming/README.md), [A2](../learning-path/ai-application-engineer/programs/a-python/courses/python-libraries/README.md).

Các mức ưu tiên là lựa chọn của roadmap cho phạm vi ứng dụng này; không phải bảng xếp hạng độ phổ biến trên thị trường.

| Concept | Hiểu ngắn gọn | Khi dùng | Câu hỏi tự kiểm | Mức |
| --- | --- | --- | --- | --- |
| Mutability và aliasing | Nhiều tên có thể trỏ cùng object; object mutable có thể bị sửa tại chỗ. | Xử lý list/dict và tránh sửa input ngoài ý muốn. | Vì sao copy nông chưa tách list lồng nhau? | CORE |
| Equality và identity | `==` so giá trị theo kiểu; `is` kiểm cùng object. | So sánh dữ liệu và sentinel như None. | Đổi `==` sang `is` có làm test sai? | CORE |
| Scope và closure | Scope quyết định nơi tra tên; closure giữ tham chiếu tới biến vùng bao ngoài. | Factory hàm, callback, decorator. | Giải thích biến được đọc từ đâu trong ví dụ vòng lặp. | CORE |
| Type hints và runtime validation | Annotation mô tả kiểu cho công cụ/người đọc; không tự kiểm mọi input lúc chạy. | Contract hàm và API boundary. | Có type hint rồi, vì sao vẫn phải reject bool ở field số? | CORE |
| Iterator và generator | Iterator tạo phần tử từng bước; generator hỗ trợ viết iterator bằng yield. | Đọc file lớn, pipeline không cần giữ toàn bộ dữ liệu. | Một generator dùng lại sau khi đã duyệt hết sẽ thế nào? | PRACTICE |
| Comprehension | Cú pháp tạo collection hoặc generator từ phép biến đổi/lọc. | Chuẩn hóa dữ liệu ngắn, rõ. | Chọn list hay generator khi cần duyệt hai lần. | CORE |
| Decorator | Hàm bọc hoặc thay thế callable để bổ sung hành vi. | Logging, timing, kiểm contract có chủ đích. | Có giữ được exception và return của hàm gốc? | PRACTICE |
| Context manager | Quy định setup/cleanup quanh một khối thực thi. | File, lock, session, transaction. | Lỗi giữa khối with có giải phóng tài nguyên? | PRACTICE |
| Dataclass và composition | Dataclass giảm mã khai báo dữ liệu; composition ghép object để chia trách nhiệm. | Record, config và service nhỏ. | Khi nào một dict đủ, khi nào cần object? | PRACTICE |
| Exception và error contract | Lỗi có loại và ngữ cảnh; boundary quyết định chuyển lỗi thành phản hồi nào. | Validation và API errors. | Có nuốt lỗi rồi trả dữ liệu tưởng là hợp lệ không? | CORE |
| Module, package, environment | Tổ chức code/import và cô lập dependencies. | Chạy lại project trên máy khác. | Chạy từ thư mục khác có phụ thuộc working directory? | CORE |
| Coroutine, task, event loop | Coroutine có thể tạm dừng tại await; task được event loop lập lịch. | Nhiều thao tác I/O có thời gian chờ. | Khác nhau giữa tạo coroutine và thật sự chạy nó? | CORE |
| Concurrency và parallelism | Concurrency quản lý nhiều việc chồng lấn; parallelism thực thi đồng thời trên tài nguyên tính toán. | Chọn async, thread hoặc process theo workload. | Vì sao async không tự làm phép tính CPU nhanh hơn? | CORE |
| Timeout và cancellation | Giới hạn chờ và truyền tín hiệu hủy, cần cleanup đúng. | Request chậm, stream bị đóng. | Sau hủy còn task hoặc connection bị giữ không? | PRACTICE |
| Fixture, parametrization, mock | Dữ liệu/setup dùng lại, nhiều input cho một hành vi, thay dependency ở boundary. | Test logic độc lập với mạng/provider. | Mock có che mất chính lỗi cần kiểm? | PRACTICE |

## Nguồn đối chiếu

[Python Classes](https://docs.python.org/3/tutorial/classes.html), [Python asyncio Tasks](https://docs.python.org/3/library/asyncio-task.html), [pytest Get Started](https://docs.pytest.org/en/stable/getting-started.html).

[Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html), [Python typing](https://docs.python.org/3/library/typing.html).

Bảng là diễn giải phục vụ học tập; bài thực hành và câu hỏi tự kiểm là thiết kế của repo. Đọc đúng phần được chỉ trong unit, sau đó giải thích bằng code hoặc ví dụ thay vì học thuộc bảng.
