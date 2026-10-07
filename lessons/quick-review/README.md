# Ôn nhanh Python, OOP → AI cơ bản

Bộ **14 bài đọc ngắn**, dành cho một lượt ôn lại trước khi đi sâu roadmap. Mỗi bài có giải thích, ví dụ, lỗi hay gặp, câu hỏi có đáp án và bài tập nhỏ. Mục tiêu là nối lại kiến thức và tìm chỗ còn hổng, không học thuộc danh sách thuật ngữ.

## Bắt đầu

1. Đọc [bản ôn nhanh](CHEATSHEET.md) trong khoảng 15–20 phút để nhìn toàn bộ nội dung.
2. Đi theo thứ tự **P01 → P08 → AI01 → AI06**. Mỗi bài dự kiến 10–20 phút đọc; dừng lại tự dự đoán ví dụ trước khi xem đáp án. Tổng một lượt khoảng 3–5 giờ, tùy phần đã nhớ.
3. Với bài còn vướng, làm bài tập thêm 15–30 phút và ghi vào [phiếu tự ôn](REVIEW.md). Không cần hoàn tất các phase Web/DevOps mới đọc AI nhập môn này.

Các khoảng thời gian là gợi ý. Đây là lớp ôn nền của Phase A, C và D; đọc hết **không tự hoàn thành** các phase đó. NumPy/Pandas, frontend, training model và triển khai hệ thống có course sâu riêng trong [roadmap](../../ROADMAP.md).

## Phần 1 · Python và OOP

| Bài | Nội dung cần nhớ | Sau bài này bạn giải thích được |
| --- | --- | --- |
| [P01 · Dữ liệu và object](python/01-data-and-objects.md) | Kiểu, collection, control flow, mutability, copy, equality/identity | Vì sao sửa một list làm biến khác thay đổi |
| [P02 · Hàm và contract](python/02-functions-and-contracts.md) | Tham số, scope, default argument, typing, validation | Hàm nhận gì, trả gì và lỗi theo cách nào |
| [P03 · Module, file và exception](python/03-modules-files-errors.md) | Import, package, JSON, with, raise, error handling | Luồng đọc dữ liệu có lỗi mà không mất dấu nguyên nhân |
| [P04 · OOP trong Python](python/04-oop-basics.md) | Class/object, self, attribute, method, dataclass, dunder | Class khác object và dữ liệu chung khác dữ liệu từng instance |
| [P05 · Thiết kế OOP](python/05-oop-design.md) | Encapsulation, abstraction, inheritance, polymorphism, composition, Protocol | Khi nào kế thừa, khi nào truyền dependency vào object |
| [P06 · Python nâng cao thường gặp](python/06-python-patterns.md) | Iterator/generator, closure, decorator, context manager | Code tạo từng phần tử và code bọc hành vi chạy thế nào |
| [P07 · Async và concurrency](python/07-async.md) | Coroutine/task, event loop, timeout, cancellation | Vì sao async phù hợp thời gian chờ I/O |
| [P08 · Debug, test và môi trường](python/08-debug-test-environment.md) | Traceback, boundary tests, fake, venv, Git | Một test có thật sự phát hiện lỗi hay chỉ chạy được |

## Phần 2 · AI cơ bản

| Bài | Nội dung cần nhớ | Sau bài này bạn giải thích được |
| --- | --- | --- |
| [AI01 · Bản đồ AI](ai/01-ai-map.md) | AI, ML, DL, GenAI, LLM; classification/regression/clustering | Bài toán cần luật, mô hình dự đoán hay mô hình sinh |
| [AI02 · Dữ liệu, học và đánh giá](ai/02-learning-and-evaluation.md) | Feature/label, loss, train/dev/test, overfitting, leakage, metrics | Vì sao điểm cao vẫn có thể là đánh giá sai |
| [AI03 · LLM hoạt động thế nào](ai/03-llm-basics.md) | Token, embedding, attention, Transformer, context, sampling | Model sinh câu trả lời và có thể sai ở đâu |
| [AI04 · Làm việc với AI](ai/04-prompt-context-memory.md) | Instruction/prompt/context/memory, skill/hook, output contract | Cung cấp đúng dữ liệu và kiểm lại kết quả AI |
| [AI05 · Embedding, RAG và fine-tuning](ai/05-embedding-rag.md) | Vector/cosine, retrieval, chunk/index, citation, adaptation | Khi nào đưa tài liệu vào context, khi nào cần học thêm từ dữ liệu |
| [AI06 · Tool, workflow và agent](ai/06-tools-agents.md) | Tool call, loop/harness, permission, evaluation, cost | Ai thực thi hành động và kiểm quyền ở đâu |

## Cách dùng ví dụ

Ví dụ dùng chủ đề **ghi chú học tập và trợ lý tra cứu**, dữ liệu nhỏ do repo tạo. Các khối Python có file tương ứng trong `examples/`; chạy từ thư mục gốc repo bằng Python 3.11 trở lên:

```bash
python3 lessons/quick-review/examples/p01.py
python3 lessons/quick-review/examples/p04.py
python3 lessons/quick-review/examples/ai05.py
```

Không cần cài package hoặc có API key. Các ví dụ AI bằng Python chỉ minh họa metric, vector hoặc cơ chế chạy tool; **không gọi LLM và không huấn luyện model**. Đọc giới hạn ngay trong từng bài để không nhầm demo cơ chế với hệ AI thật.

## Sau lượt ôn

- Phần Python còn vướng: quay lại [Phase A](../../ROADMAP.md#phase-a) và unit tương ứng.
- Muốn học NumPy/Pandas: mở [Python Libraries](../../learning-path/ai-application-engineer/programs/a-python/courses/python-libraries/README.md).
- Muốn thực hành AI hỗ trợ code: học [Phase C](../../ROADMAP.md#phase-c).
- Muốn xây LLM/RAG/agent: học [Phase D](../../ROADMAP.md#phase-d), bổ sung API/database theo đầu vào của course.

[Bài tổng hợp nhỏ](MINI_LAB.md) · [Nguồn và kiểm chứng ví dụ](VERIFICATION.md) · [Roadmap chính](../../ROADMAP.md)
