# AI-assisted SDLC và quản lý công việc

[Danh mục concept](../docs/CONCEPTS.md) · [Roadmap](../ROADMAP.md)

**Học trong:** [C1](../learning-path/ai-application-engineer/programs/c-ai-sdlc/courses/ai-coding/README.md), [C2](../learning-path/ai-application-engineer/programs/c-ai-sdlc/courses/spec-driven/README.md), [E1](../learning-path/ai-application-engineer/programs/e-research/courses/project-research/README.md), [F1](../learning-path/ai-application-engineer/programs/f-product/courses/product-delivery/README.md).

Các mức ưu tiên là lựa chọn của roadmap cho phạm vi ứng dụng này; không phải bảng xếp hạng độ phổ biến trên thị trường.

| Concept | Hiểu ngắn gọn | Khi dùng | Câu hỏi tự kiểm | Mức |
| --- | --- | --- | --- | --- |
| Instruction | Quy tắc/hướng dẫn điều khiển hành vi trong một phạm vi. | Giới hạn task và quy ước repo cho coding assistant. | Instruction có nói rõ scope và output? | CORE |
| Prompt | Yêu cầu đưa vào model cho một lần tương tác, có thể chứa instruction và dữ liệu. | Yêu cầu phân tích/sửa code. | Có ví dụ đúng/sai và tiêu chí nghiệm thu chưa? | PRACTICE |
| Context | Thông tin model đang được cung cấp: hội thoại, file, dữ liệu truy xuất, tool results. | Chọn thông tin liên quan cho task. | Có đủ contract nhưng tránh dữ liệu không liên quan? | CORE |
| Memory | Thông tin được lưu để dùng về sau, thường do ứng dụng/công cụ quản lý. | Sở thích, quyết định và trạng thái dài hạn. | Thông tin cũ có thời điểm, nguồn và cách sửa/xóa? | AWARENESS |
| Skill | Gói hướng dẫn/tài nguyên tái sử dụng cho một loại công việc; cách nạp tùy công cụ. | Chuẩn hóa thao tác review hoặc xử lý tài liệu. | Đây là workflow hay thay đổi weights của model? | AWARENESS |
| Hook | Hành động gắn với sự kiện trong lifecycle của công cụ. | Chạy kiểm tra hoặc bổ sung kiểm soát sau/trước một bước. | Hook này chạy lúc nào, có quyền gì, lỗi thì sao? | AWARENESS |
| Tool | Giao diện để chương trình/model yêu cầu một hành động thực thi. | Đọc file, query DB, gọi API. | Tool đọc và tool ghi có cùng mức quyền không? | CORE |
| Requirement và acceptance criteria | Nhu cầu và điều kiện có thể quan sát để chấp nhận kết quả. | Trước thiết kế/coding. | Người khác có kiểm được đúng/sai từ mô tả? | PRACTICE |
| Specification và design | Spec mô tả hành vi/ràng buộc; design chọn cách thực hiện. | Chuyển yêu cầu thành implementation. | Có vô tình coi công nghệ là nhu cầu người dùng? | PRACTICE |
| SDLC và spec-driven development | Chu trình phát triển và cách giữ spec gắn với thay đổi/kiểm chứng. | Feature từ brief đến release. | Spec, code và tests còn khớp sau khi sửa? | PRACTICE |
| Spec Kit và AWS AI-DLC | Hai ví dụ phương pháp/công cụ hỗ trợ quy trình có AI, với phạm vi riêng. | So sánh cách tổ chức công việc. | Không gọi đây là chuẩn bắt buộc cho mọi đội. | AWARENESS |
| Agile, Scrum, backlog và DoD | Agile là định hướng thích nghi; Scrum là framework; backlog/DoD hỗ trợ quản lý giá trị và chất lượng. | Lập kế hoạch và review increment. | Buổi review có output, feedback và quyết định thực tế? | AWARENESS |
| Unit, integration và E2E tests | Các phạm vi kiểm tra từ logic nhỏ đến ranh giới tích hợp và luồng đầy đủ. | Chọn kiểm tra phù hợp loại lỗi. | Mock toàn bộ DB có chứng minh SQL thực sự chạy đúng không? | PRACTICE |
| Regression và test oracle | Kiểm lại hành vi từng đúng; oracle xác định expected độc lập. | Review code AI và sửa bug. | Test có thể fail khi bug tồn tại hay chỉ lặp logic implementation? | PRACTICE |
| Code review và provenance | Xem diff/behavior và ghi nguồn đóng góp của con người/công cụ. | PR, portfolio và đánh giá năng lực. | Giải thích được code được chấp nhận và phần mình sở hữu? | PRACTICE |

## Nguồn đối chiếu

[Claude Code Skills](https://code.claude.com/docs/en/skills), [Claude Code Hooks](https://code.claude.com/docs/en/hooks), [GitHub Spec Kit](https://github.com/github/spec-kit), [AWS AI-DLC](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/), [Scrum Guide](https://scrumguides.org/scrum-guide.html), [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow), [GitHub Actions](https://docs.github.com/en/actions/get-started/understand-github-actions).

Bảng là diễn giải phục vụ học tập; bài thực hành và câu hỏi tự kiểm là thiết kế của repo. Đọc đúng phần được chỉ trong unit, sau đó giải thích bằng code hoặc ví dụ thay vì học thuộc bảng.
