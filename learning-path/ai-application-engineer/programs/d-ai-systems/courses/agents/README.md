# D3 · Agent Loop, Harness và MCP

[Program](../../README.md) · [Tiến độ](../../../../../../PROGRESS.md)

**Đầu vào:** D1; D2 nếu agent dùng tìm tài liệu; có API tests.

**Khối lượng:** 35–55 giờ dự kiến, gồm thực hành và review. Học theo năng lực đầu vào; người đã có artifact tương đương có thể xin review để rút phần ôn.

## Course Learning Outcomes

| CLO | Kết quả thể hiện | Đóng góp vào program |
| --- | --- | --- |
| CLO1 | Phân biệt workflow, agent loop, harness, tool và MCP. | PLO1 |
| CLO2 | Xây agent nhỏ có state và tool contract rõ, giới hạn số bước/chi phí. | PLO2 |
| CLO3 | Kiểm resume, lỗi tool, approval và input không tin cậy. | PLO3 |
| CLO4 | So sánh agent với workflow đơn giản trên cùng task set và giải thích lựa chọn. | PLO4 |

## Units và topics

| Unit | Topics chính | Đầu ra |
| --- | --- | --- |
| [1. Loop và harness](units/01.md) | observe/decide/act; workflow vs agent; harness; tool schema; stop condition | Agent nhỏ và trace một nhiệm vụ nhiều bước. |
| [2. State và hành động](units/02.md) | state machine; checkpoint; resume; idempotency; HITL; least privilege; audit trail | State diagram và fault/approval tests. |
| [3. MCP và đo hiệu quả](units/03.md) | MCP host/client/server; tools/resources/prompts; auth boundary; protocol; task success | Tool contract, integration report và bảng so sánh. |

## Bài nộp và đánh giá

Gộp output của các unit thành một milestone của [running project](../../running-project/README.md). Trước review, gửi file/repo+commit, lệnh chạy, fixture và kết quả thật.

- CLO1: giải thích concept qua ví dụ, không chỉ đọc định nghĩa.
- CLO2: demo artifact đúng contract.
- CLO3: chạy ca lỗi/biên; ghi expected và actual.
- CLO4: sửa một biến thể hoặc giải thích trade-off, ghi mức trợ giúp.

Các tiêu chí cụ thể của unit và outcome của course được dùng để kết luận; bốn dòng trên là cách thu bằng chứng, không thay thế nội dung CLO.

## Tài liệu và ghi chú

Nguồn gắn trực tiếp trong mỗi unit; xem thêm [danh mục nguồn](../../../../../../docs/RESOURCES.md). Tạo `docs/` trong course khi có ghi chú, báo cáo hoặc tài liệu được phép lưu; đặt tên theo nội dung/ngày, rồi liên kết từ review. Không sao chép toàn văn tài liệu bên ngoài vào repo.
