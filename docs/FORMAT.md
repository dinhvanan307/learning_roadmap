# Cấu trúc và quy ước chương trình

## Learning path, program, course, unit, topic

| Cấp | Ý nghĩa trong repo | Ví dụ |
| --- | --- | --- |
| Learning path | Một hướng năng lực, gồm các chương trình và điều kiện đầu vào | AI Application Engineer |
| Phase | Thứ tự hoặc mốc phát triển của lộ trình | Phase B |
| Program | Nhóm course cùng tạo ra một năng lực/sản phẩm có thể review | Data và Full-stack Web |
| Course | Một phạm vi học có CLO, units, đầu ra và đánh giá | Database và Data Modeling |
| Unit | Một cụm bài học/thực hành đủ nhỏ để hoàn thành và nhận phản hồi | Transaction và ORM |
| Topic | Concept hoặc kỹ thuật trong unit | Isolation, optimistic locking |
| Running project | Bài tập tích hợp tiến hóa qua các course/program | Web dữ liệu → API/UI → AI → release |
| Milestone | Phiên bản đầu ra cụ thể để kiểm tra | API lưu dữ liệu sau restart |

Phase mô tả tiến trình; program mô tả chương trình học. Trong nhánh chính repo ánh xạ mỗi phase sang một program để dễ đọc, nhưng đây không phải quy tắc phổ quát.

## PLO và CLO

**PLO (Program Learning Outcome):** năng lực thể hiện được khi hoàn thành program. **CLO (Course Learning Outcome):** năng lực thể hiện được khi hoàn thành course và đóng góp vào PLO.

Ví dụ: PLO về xây hệ thống dữ liệu được hỗ trợ bởi CLO về schema, transaction và API persistence. Một PLO có thể cần nhiều CLO; một CLO cũng có thể hỗ trợ nhiều PLO. Trong bản này mỗi course chọn bốn CLO và ghi PLO đóng góp chính để review dễ hơn; không có công thức “6 CLO = 1 PLO” hoặc bắt buộc mọi chương trình phải cùng số outcome.

Outcome cần nêu hành động quan sát được, điều kiện và cách kiểm. Ví dụ: “Xử lý request lặp sao cho effect trong DB chỉ ghi một lần trong bộ test tuần tự và đồng thời”, thay vì chỉ “hiểu idempotency”. Mục tiêu, hoạt động học và đánh giá phải khớp nhau. [CMU Eberly Center](https://www.cmu.edu/teaching/designteach/design/learningobjectives.html)

## Mẫu thống nhất

| Thành phần | Nội dung bắt buộc |
| --- | --- |
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

## Cách thay đổi kế hoạch

Sửa outcome hoặc gate trong program/course trước, rồi đồng bộ unit và tracker. Ghi lý do đổi phạm vi trong review. Tài liệu cũ nằm trong archive để đối chiếu, không dùng hai lịch làm nguồn tiến độ song song.
