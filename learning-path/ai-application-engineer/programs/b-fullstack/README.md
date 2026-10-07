# B · Data và Full-stack Web Development

[Learning path](../../README.md) · [Tiến độ](../../../../PROGRESS.md)

**Vai trò:** giai đoạn chính theo mindmap. **Đầu vào:** A hoặc bài làm tương đương đã được review.

## Phạm vi kiến thức của Phase B

- [B.1 · Internet, Network và OS căn bản](../../../../ROADMAP.md#b-1)
- [B.2 · Database, SQL, ORM và NoSQL](../../../../ROADMAP.md#b-2)
- [B.3 · Backend và Web API với FastAPI](../../../../ROADMAP.md#b-3)
- [B.4 · Ngôn ngữ và nền tảng Web](../../../../ROADMAP.md#b-4)
- [B.5 · Frontend với React, Next.js và Tailwind CSS](../../../../ROADMAP.md#b-5)

Xem checklist topics, thực hành và độ sâu tại các liên kết trên. Hoàn thành toàn bộ phần bắt buộc và gate của phase; ghi bằng chứng trong [tracker từng phần](../../../../progress/PHASES.md).

## Program Learning Outcomes

Sau chương trình, người học có thể:

- **PLO1:** Giải thích luồng browser → HTTP → API → database và ranh giới trách nhiệm.
- **PLO2:** Thiết kế schema và triển khai API/UI cho một luồng dữ liệu hoàn chỉnh.
- **PLO3:** Kiểm thử transaction, quyền dữ liệu và lỗi mạng bằng tình huống đối nghịch.
- **PLO4:** Chẩn đoán lỗi qua log/query/network và giải thích lựa chọn REST, ORM, rendering.

## Courses và khối lượng

| Course | Giờ dự kiến | Milestone |
| --- | ---: | --- |
| [B1 · Database và Data Modeling](courses/database/README.md) | 30–45 | Thiết kế schema relational và truy vấn báo cáo giữ cả nhóm rỗng. |
| [B2 · Internet Basics và FastAPI](courses/fastapi/README.md) | 40–60 | Xây REST API có validation, pagination, persistence và dependency injection. |
| [B3 · React, Next.js và Tailwind CSS](courses/frontend/README.md) | 35–50 | Tạo UI danh sách/chi tiết/form nối API thật của bài tập. |

**Tổng tham chiếu:** 105–155 giờ, gồm đọc, thực hành, test và review. Đây là ước lượng thiết kế mới, cần điều chỉnh theo bài làm đầu vào; không phải số giờ do mindmap xác nhận.

## Running project

Web quản lý địa điểm và lịch trình nháp với PostgreSQL, FastAPI, React/Next.js.

Chi tiết: [mốc sản phẩm và tiêu chí nghiệm thu](running-project/README.md).

## Gate kết thúc

Luồng tạo/sửa/xem chạy qua UI/API/DB; dữ liệu tồn tại sau restart; người dùng khác không đọc/sửa được dữ liệu riêng trong bộ test.

Mỗi PLO cần liên kết tới bài làm, kết quả chạy và phần giải thích. Dùng [mẫu review](../../../../templates/REVIEW.md); chưa có bài làm thì không đánh dấu đạt.

## Học theo nhu cầu

Các mục `CORE`, `PRACTICE`, `AWARENESS`, `OPTIONAL` được giải thích trong [danh mục concept](../../../../docs/CONCEPTS.md). Hoàn thành số tuần không tự xác nhận cấp bậc nghề nghiệp.
