# AI Application Engineer Learning Roadmap

Lộ trình học **Python → Web → phát triển phần mềm có AI → RAG/Agent → nghiên cứu dự án → sản phẩm → triển khai**, tổ chức theo mindmap và góp ý mentor. Mỗi chương trình có mục tiêu học tập, bài thực hành, mốc sản phẩm và cách kiểm chứng.

## Bắt đầu ở đâu

| Bạn cần | Mở tài liệu |
| --- | --- |
| Xem học gì, theo thứ tự nào | [Roadmap A–G](ROADMAP.md) |
| Hiểu cách chia program, course, unit, PLO/CLO | [Cấu trúc chương trình](docs/FORMAT.md) |
| Học và tra các concept thường gặp | [Danh mục concept](docs/CONCEPTS.md) |
| Xem bài tập và nguồn cho từng course | [Learning path](learning-path/ai-application-engineer/README.md) |
| Biết mỗi giai đoạn làm ra gì | [Running project](projects/RUNNING_PROJECT.md) |
| Ghi tiến độ, bài nộp và phản hồi | [Progress tracker](PROGRESS.md) |
| Xem sơ đồ và outline của lộ trình | [Mindmap Markdown](docs/MINDMAP.md) |

**Bước đầu:** làm [đối chiếu đầu vào](docs/ENTRY_REVIEW.md), chọn một unit cần học, làm bài rồi lưu review. Nếu đã có artifact đáp ứng yêu cầu, dùng artifact đó để review thay vì học lại theo lịch máy móc.

## Các giai đoạn

| Phase | Trọng tâm | Output để review |
| --- | --- | --- |
| A | Python Programming và Libraries | CLI, bộ test, báo cáo dữ liệu |
| B | Database, FastAPI, React/Next.js | Web có luồng UI → API → DB |
| C | AI-assisted SDLC | Feature từ spec đến review, ghi rõ đóng góp AI |
| D | LLM, RAG và Agent Systems | Prototype có nguồn, quyền, eval và giới hạn tool |
| E | Nghiên cứu dự án | Problem brief, thử nghiệm và quyết định phạm vi |
| F | Xây dựng sản phẩm | MVP có luồng hoàn chỉnh, demo và regression tests |
| G | Deployment và LLMOps | Release, quan sát hệ thống, rollback/restore và runbook |

Nhánh **Machine Learning / Deep Learning** có chương trình riêng khi cần đi sâu mô hình. Các nền tảng vector, metric và đánh giá cần cho AI Application vẫn nằm trong nhánh chính.

## Cách tổ chức repo

```text
README.md / ROADMAP.md / PROGRESS.md
learning-path/ai-application-engineer/
  README.md
  programs/<program>/
    README.md                     # PLO, đầu vào, courses, gate
    courses/<course>/
      README.md                   # CLO, units, bài nộp
      units/01.md, 02.md, 03.md    # topics, bài tập, output, nguồn
      docs/                       # tạo khi có ghi chú/bài làm thực tế
    running-project/README.md     # milestone và nghiệm thu
concepts/                         # giải nghĩa, cách dùng, tự kiểm
projects/                         # dự án xuyên suốt và các mốc
progress/                         # ma trận CLO và nhật ký review
templates/                        # mẫu unit, course, review
resources/                        # dữ liệu mẫu/manifest do người học bổ sung
archive/dashboard-v1/             # bản W0–W12 nguyên trạng
```

**9 programs · 18 courses · 54 units.** Trong đó 7 programs/14 courses thuộc nhánh chính; 2 programs/4 courses ML/DL là mở rộng. Các file là kế hoạch và đề bài; bài làm, kết quả chạy và năng lực đã đạt được ghi riêng trong tracker.

## Cách học và review

1. Đọc đúng phần nguồn gắn với unit; giải thích concept bằng ví dụ nhỏ.
2. Làm bài và kiểm ca hợp lệ, biên, lỗi; lưu file/repo và commit.
3. Demo milestone, giải thích code kể cả phần AI viết, xử lý một biến thể mới.
4. Ghi phản hồi, giờ thực tế và việc tiếp theo theo [mẫu review](templates/REVIEW.md).

Chuẩn bị một buổi review mỗi tuần theo gợi ý mindmap; ngày/giờ cụ thể cần tự sắp xếp. Kết quả có thể là tiếp tục, bổ sung hoặc đổi phạm vi. Hoàn thành tài liệu hoặc tick checkbox không tự xác nhận cấp bậc nghề nghiệp.

[Đối chiếu mindmap](docs/SOURCE.md) · [Nguồn học chính thức](docs/RESOURCES.md) · [Bản cũ](archive/dashboard-v1/README.md)
