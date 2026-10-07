# Running project · Data và Full-stack Web Development

[Chương trình](../README.md) · [Dự án xuyên suốt](../../../../../projects/RUNNING_PROJECT.md)

## Mục tiêu và output

Web quản lý địa điểm và lịch trình nháp với PostgreSQL, FastAPI, React/Next.js.

Đây là đầu ra cần thực hiện, chưa phải sản phẩm đã có mã hoặc đã chạy. Có thể giữ code ở repo bài tập riêng và ghi commit trong bằng chứng.

## Năng lực được đánh giá

| PLO | Bằng chứng cần nộp |
| --- | --- |
| PLO1 · Giải thích luồng browser → HTTP → API → database và ranh giới trách nhiệm. | Sơ đồ hoặc giải thích kèm ví dụ cụ thể, chỉ ra input/output và ranh giới. |
| PLO2 · Thiết kế schema và triển khai API/UI cho một luồng dữ liệu hoàn chỉnh. | Artifact chạy được, README và commit tương ứng. |
| PLO3 · Kiểm thử transaction, quyền dữ liệu và lỗi mạng bằng tình huống đối nghịch. | Test/report cho ca đúng, ca lỗi và giới hạn kết luận. |
| PLO4 · Chẩn đoán lỗi qua log/query/network và giải thích lựa chọn REST, ORM, rendering. | Demo, một biến thể mới, lý do thiết kế và ghi rõ mức trợ giúp. |

## Mốc theo course

- [ ] B1: Thiết kế schema relational và truy vấn báo cáo giữ cả nhóm rỗng. — [yêu cầu course](../courses/database/README.md).
- [ ] B2: Xây REST API có validation, pagination, persistence và dependency injection. — [yêu cầu course](../courses/fastapi/README.md).
- [ ] B3: Tạo UI danh sách/chi tiết/form nối API thật của bài tập. — [yêu cầu course](../courses/frontend/README.md).

## Nghiệm thu

Luồng tạo/sửa/xem chạy qua UI/API/DB; dữ liệu tồn tại sau restart; người dùng khác không đọc/sửa được dữ liệu riêng trong bộ test.

Ghi môi trường, input, lệnh chạy, expected/actual, commit, lỗi còn lại, người review và quyết định tiếp tục/bổ sung. Một artifact có thể chứng minh nhiều CLO/PLO, nhưng phải chỉ rõ phần nào hỗ trợ kết luận nào.
