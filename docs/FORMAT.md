# Cấu trúc và quy ước chương trình

## Learning path, program, course, unit, topic

| Cấp | Ý nghĩa trong repo | Ví dụ |
| --- | --- | --- |
| Learning path | Một hướng năng lực, gồm các chương trình và điều kiện đầu vào | AI Application Engineer |
| Phase | Một khối kiến thức và năng lực trong thứ tự học A–G | Phase B · Web Development |
| Phần kiến thức | Phạm vi nhỏ bên trong phase, có topics và bài thực hành | B.2 · Database, SQL, ORM và NoSQL |
| Program | Nhóm course cùng tạo ra một năng lực/sản phẩm có thể review | Data và Full-stack Web |
| Course | Một phạm vi học có CLO, units, đầu ra và đánh giá | Database và Data Modeling |
| Unit | Một cụm bài học/thực hành đủ nhỏ để hoàn thành và nhận phản hồi | Transaction và ORM |
| Topic | Concept hoặc kỹ thuật trong unit | Isolation, optimistic locking |
| Running project | Bài tập tích hợp tiến hóa qua các course/program | Web dữ liệu → API/UI → AI → release |
| Milestone | Phiên bản đầu ra cụ thể để kiểm tra | API lưu dữ liệu sau restart |

Phase là cách đọc lộ trình theo khối kiến thức; program/course/unit tổ chức outcomes và bài học. Trong nhánh chính, mỗi phase tương ứng một program. Có 29 phần kiến thức bên trong 7 phase, liên kết tới các course hiện có; một course có thể phục vụ nhiều phần. `A.1` là phần kiến thức, còn `A1` là mã course. Hai hệ này không được cộng số giờ hai lần.

[ROADMAP](../ROADMAP.md) xác định nội dung và độ sâu; [PHASES](../progress/PHASES.md) ghi trạng thái/bằng chứng từng phần; [OUTCOMES](../progress/OUTCOMES.md) ghi kết luận CLO. Checkbox trong roadmap là phạm vi để đối chiếu, không dùng tính tiến độ riêng cạnh tracker.

## PLO và CLO

**PLO (Program Learning Outcome):** năng lực thể hiện được khi hoàn thành program. **CLO (Course Learning Outcome):** năng lực thể hiện được khi hoàn thành course và đóng góp vào PLO.

Ví dụ: PLO về xây hệ thống dữ liệu được hỗ trợ bởi CLO về schema, transaction và API persistence. Một PLO có thể cần nhiều CLO; một CLO cũng có thể hỗ trợ nhiều PLO. Trong bản này mỗi course chọn bốn CLO và ghi PLO đóng góp chính để review dễ hơn; không có công thức “6 CLO = 1 PLO” hoặc bắt buộc mọi chương trình phải cùng số outcome.

Outcome cần nêu hành động quan sát được, điều kiện và cách kiểm. Ví dụ: “Xử lý request lặp sao cho effect trong DB chỉ ghi một lần trong bộ test tuần tự và đồng thời”, thay vì chỉ “hiểu idempotency”. Mục tiêu, hoạt động học và đánh giá phải khớp nhau. [CMU Eberly Center](https://www.cmu.edu/teaching/designteach/design/learningobjectives.html)

## Mẫu thống nhất

| Thành phần | Nội dung bắt buộc |
| --- | --- |
| Phase / phần kiến thức | Topics cụ thể, độ sâu, thực hành, course tương ứng, output và điều kiện hoàn thành |
| Program | Mục tiêu/PLO, đầu vào, course, running project, gate |
| Course | Đầu vào, CLO và PLO liên quan, units, output và cách đánh giá |
| Unit | Topics/concepts, bài tập, output, tiêu chí kiểm tra, nguồn đúng phần |
| Review | Commit/file, input, lệnh, expected/actual, mức hỗ trợ, người review, quyết định |

Nguồn tài liệu hỗ trợ kiến thức; bài tập, giờ dự kiến và ngưỡng đánh giá là thiết kế riêng của roadmap. Một link chính thức không xác nhận toàn bộ giáo trình đã được chứng nhận hoặc người học đã làm được.

## Quy tắc hoàn thành

- Làm được và giải thích được, bao gồm phần code AI tạo.
- Kiểm cả ca đúng, ca lỗi quan trọng và một biến thể mới phù hợp phạm vi.
- Bài làm cần tái lập được: có commit, môi trường, dữ liệu và lệnh.
- Ghi rõ tự làm, tra tài liệu, được hướng dẫn hoặc AI viết; không suy ra ownership từ repo có code.
- Chưa đạt thì ghi phần thiếu và việc sửa, không chuyển `VERIFIED` chỉ vì đủ giờ.
- Phase chỉ hoàn thành khi mọi phần bắt buộc được review ở độ sâu đã ghi và đạt gate tích hợp; mục mở rộng chưa chọn không chặn hoàn thành.

## Cách thay đổi kế hoạch

Khi đổi phạm vi kiến thức, cập nhật ROADMAP rồi đồng bộ outcome/gate, unit và tracker liên quan. Khi chỉ sửa bài tập, giữ mapping tới phần kiến thức. Ghi lý do đổi phạm vi trong review. Tài liệu cũ nằm trong archive để đối chiếu, không dùng hai lịch làm nguồn tiến độ song song.
