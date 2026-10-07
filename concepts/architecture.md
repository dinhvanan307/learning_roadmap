# Thiết kế phần mềm và pattern

[Danh mục concept](../docs/CONCEPTS.md) · [Roadmap](../ROADMAP.md)

**Học trong:** [A1](../learning-path/ai-application-engineer/programs/a-python/courses/python-programming/README.md), [B2](../learning-path/ai-application-engineer/programs/b-fullstack/courses/fastapi/README.md), [D1](../learning-path/ai-application-engineer/programs/d-ai-systems/courses/llm-integration/README.md), [D3](../learning-path/ai-application-engineer/programs/d-ai-systems/courses/agents/README.md).

Các mức ưu tiên là lựa chọn của roadmap cho phạm vi ứng dụng này; không phải bảng xếp hạng độ phổ biến trên thị trường.

| Concept | Hiểu ngắn gọn | Khi dùng | Câu hỏi tự kiểm | Mức |
| --- | --- | --- | --- | --- |
| Separation of concerns | Tách trách nhiệm để thay đổi và kiểm thử từng phần dễ hơn. | Chia I/O, logic nghiệp vụ và API. | Sửa persistence có buộc sửa thuật toán xử lý dữ liệu? | CORE |
| Cohesion và coupling | Mức liên quan nội bộ module và mức phụ thuộc giữa module. | Chọn ranh giới code. | Thay một rule kéo theo bao nhiêu module không liên quan? | CORE |
| Composition và inheritance | Ghép hành vi từ object khác hoặc kế thừa quan hệ kiểu. | Tái sử dụng code có thay thế implementation. | Quan hệ thật sự là is-a hay chỉ cần gọi một dependency? | CORE |
| Interface, protocol và contract | Thỏa thuận hành vi gồm input/output/lỗi, không chỉ chữ ký hàm. | Thay provider, repository hoặc mock. | Hai implementation có giữ cùng quy tắc timeout/error? | CORE |
| Dependency injection | Cung cấp dependency từ ngoài thay vì tự tạo cứng trong logic. | Test và đổi provider/database. | Có thể chạy logic với fake dependency mà không chạm mạng? | PRACTICE |
| Adapter và provider abstraction | Chuyển giao diện bên ngoài về contract ứng dụng cần. | Nhiều model provider. | Field usage/stream/error được chuẩn hóa hay bị mất nghĩa? | PRACTICE |
| Repository và service layer | Gom truy cập dữ liệu và điều phối nghiệp vụ vào ranh giới phù hợp. | API có DB và transaction. | Transaction boundary ở đâu, có bị chia nhỏ sai? | PRACTICE |
| Strategy và factory | Tách thuật toán thay được và cách tạo object theo cấu hình. | Chọn chunker, retriever hoặc model adapter. | Một hàm đơn giản đã đủ hay thật sự cần pattern? | AWARENESS |
| DRY, KISS và YAGNI | Tránh lặp kiến thức; giữ giải pháp dễ hiểu; chưa xây phần chưa cần. | Kiểm soát độ phức tạp trong project học. | Abstraction mới giải quyết thay đổi nào đã có? | CORE |
| SOLID | Nhóm nguyên tắc về trách nhiệm, mở rộng, thay thế kiểu, interface và phụ thuộc. | Thảo luận trade-off thiết kế hướng đối tượng. | Có ví dụ cụ thể cải thiện code, hay chỉ thuộc chữ viết tắt? | AWARENESS |
| Modular monolith và microservices | Module trong một deployment khác service giao tiếp qua network. | Chọn ranh giới triển khai. | Chi phí vận hành phân tán có được vấn đề thực tế biện minh? | AWARENESS |
| ADR | Bản ghi bối cảnh, lựa chọn, phương án khác và hệ quả của quyết định. | Thay DB, model, kiến trúc. | Reviewer đọc lại có hiểu vì sao lúc đó chọn như vậy? | PRACTICE |

## Nguồn đối chiếu

[Martin Fowler Dependency Injection](https://martinfowler.com/articles/injection.html), [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/), [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow).

Bảng là diễn giải phục vụ học tập; bài thực hành và câu hỏi tự kiểm là thiết kế của repo. Đọc đúng phần được chỉ trong unit, sau đó giải thích bằng code hoặc ví dụ thay vì học thuộc bảng.
