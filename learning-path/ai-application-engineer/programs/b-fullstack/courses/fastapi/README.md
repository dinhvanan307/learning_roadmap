# B2 · Internet Basics và FastAPI

[Program](../../README.md) · [Tiến độ](../../../../../../PROGRESS.md)

**Đầu vào:** B1 và async trong A1.

**Khối lượng:** 40–60 giờ dự kiến, gồm thực hành và review. Học theo năng lực đầu vào; người đã có artifact tương đương có thể xin review để rút phần ôn.

## Course Learning Outcomes

| CLO | Kết quả thể hiện | Đóng góp vào program |
| --- | --- | --- |
| CLO1 | Mô tả DNS, TLS, HTTP, process/port và contract request/response. | PLO1 |
| CLO2 | Xây REST API có validation, pagination, persistence và dependency injection. | PLO2 |
| CLO3 | Kiểm authn/authz, request lặp, timeout và stream bị hủy. | PLO3 |
| CLO4 | Debug lỗi từ curl đến database và giải thích khi nào GraphQL/SSE phù hợp. | PLO4 |

## Units và topics

| Unit | Topics chính | Đầu ra |
| --- | --- | --- |
| [1. HTTP và contract](units/01.md) | DNS; TCP/TLS; port; process; HTTP methods/status; headers; REST; OpenAPI | API spec, curl examples và test contract. |
| [2. Auth và persistence](units/02.md) | authentication/authorization; session/token; object-level access; ORM; DI; idempotency | Ma trận quyền và positive/negative API tests. |
| [3. Giao tiếp và lỗi mạng](units/03.md) | timeout; retry/backoff; connection pool; pagination; SSE/WebSocket; GraphQL schema | Demo stream, test timeout/cancel và bảng lựa chọn giao tiếp. |

## Bài nộp và đánh giá

Gộp output của các unit thành một milestone của [running project](../../running-project/README.md). Trước review, gửi file/repo+commit, lệnh chạy, fixture và kết quả thật.

- CLO1: giải thích concept qua ví dụ, không chỉ đọc định nghĩa.
- CLO2: demo artifact đúng contract.
- CLO3: chạy ca lỗi/biên; ghi expected và actual.
- CLO4: sửa một biến thể hoặc giải thích trade-off, ghi mức trợ giúp.

Các tiêu chí cụ thể của unit và outcome của course được dùng để kết luận; bốn dòng trên là cách thu bằng chứng, không thay thế nội dung CLO.

## Tài liệu và ghi chú

Nguồn gắn trực tiếp trong mỗi unit; xem thêm [danh mục nguồn](../../../../../../docs/RESOURCES.md). Tạo `docs/` trong course khi có ghi chú, báo cáo hoặc tài liệu được phép lưu; đặt tên theo nội dung/ngày, rồi liên kết từ review. Không sao chép toàn văn tài liệu bên ngoài vào repo.
