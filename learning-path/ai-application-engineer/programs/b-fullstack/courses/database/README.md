# B1 · Database và Data Modeling

[Program](../../README.md) · [Tiến độ](../../../../../../PROGRESS.md)

**Đầu vào:** A1; biết đọc bảng và viết hàm.

**Khối lượng:** 30–45 giờ dự kiến, gồm thực hành và review. Học theo năng lực đầu vào; người đã có artifact tương đương có thể xin review để rút phần ôn.

## Course Learning Outcomes

| CLO | Kết quả thể hiện | Đóng góp vào program |
| --- | --- | --- |
| CLO1 | Giải thích key, constraint, NULL, JOIN cardinality, transaction và index. | PLO1 |
| CLO2 | Thiết kế schema relational và truy vấn báo cáo giữ cả nhóm rỗng. | PLO2 |
| CLO3 | Tái hiện rollback, duplicate insert và lost update bằng hai session. | PLO3 |
| CLO4 | So sánh SQL với document/key-value, chọn nơi dùng cache và nêu nguồn dữ liệu chuẩn. | PLO4 |

## Units và topics

| Unit | Topics chính | Đầu ra |
| --- | --- | --- |
| [1. SQL và mô hình dữ liệu](units/01.md) | PK/FK; UNIQUE/CHECK/NOT NULL; normalization; JOIN; aggregate; NULL | schema.sql, seed.sql, query và expected. |
| [2. Transaction và ORM](units/02.md) | ACID; isolation; race condition; optimistic locking; migration; ORM session; N+1 | Timeline, migration và integration report. |
| [3. Index và NoSQL](units/03.md) | EXPLAIN; composite index; document/key-value; TTL; invalidation; cache-aside | Query plan và ADR SQL/NoSQL/cache. |

## Bài nộp và đánh giá

Gộp output của các unit thành một milestone của [running project](../../running-project/README.md). Trước review, gửi file/repo+commit, lệnh chạy, fixture và kết quả thật.

- CLO1: giải thích concept qua ví dụ, không chỉ đọc định nghĩa.
- CLO2: demo artifact đúng contract.
- CLO3: chạy ca lỗi/biên; ghi expected và actual.
- CLO4: sửa một biến thể hoặc giải thích trade-off, ghi mức trợ giúp.

Các tiêu chí cụ thể của unit và outcome của course được dùng để kết luận; bốn dòng trên là cách thu bằng chứng, không thay thế nội dung CLO.

## Tài liệu và ghi chú

Nguồn gắn trực tiếp trong mỗi unit; xem thêm [danh mục nguồn](../../../../../../docs/RESOURCES.md). Tạo `docs/` trong course khi có ghi chú, báo cáo hoặc tài liệu được phép lưu; đặt tên theo nội dung/ngày, rồi liên kết từ review. Không sao chép toàn văn tài liệu bên ngoài vào repo.
