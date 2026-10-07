# Running project qua các giai đoạn

## Chủ đề và phạm vi mẫu

Mindmap có nhánh **Travel with AI**. Bản này dùng chủ đề đó làm bài tập tích hợp: web quản lý dữ liệu địa điểm và lịch trình nháp, rồi bổ sung hỏi đáp có nguồn và đề xuất có kiểm soát. Đây là **đề bài mẫu**, chưa xác nhận nhu cầu người dùng hoặc có sản phẩm triển khai.

Giữ phạm vi ban đầu ở một điểm đến với dữ liệu tổng hợp/công khai được phép sử dụng. Các thông tin giá, giờ mở cửa và thời gian di chuyển trong fixture là dữ liệu thử, không phải thông tin du lịch hiện hành. Có thể đổi domain dự án sau review mà giữ learning outcomes và tiêu chí kỹ thuật tương đương.

## Năm kết quả sản phẩm cần thể hiện

1. Nhập, kiểm tra và truy nguyên dữ liệu; không mất dấu bản ghi lỗi hay phiên bản nguồn.
2. Thực hiện luồng UI → API → DB với contract, quyền và transaction rõ ràng.
3. Hỏi đáp dựa trên nguồn, đo retrieval/answer quality và xử lý thiếu bằng chứng.
4. Công cụ/agent có giới hạn, kiểm quyền và kiểm chứng tác động; mọi ràng buộc số học và lịch được code kiểm tra.
5. Release có hướng dẫn, số đo, rollback/restore và nhật ký quyết định để người khác tiếp tục được.

Đây là outcome của bài tập tích hợp, không thay thế PLO riêng của từng program.

## Roadmap sản phẩm

| Mốc | Học trong | Input | Làm gì | Output | Điều kiện review |
| --- | --- | --- | --- | --- | --- |
| M0 · Dữ liệu | A | CSV/JSON fixture địa điểm | Validate, clean, tổng hợp, vẽ biểu đồ | CLI + report + tests | Đối chiếu số dòng/tổng; không sửa nguồn; giải thích code |
| M1 · Web | B | Dữ liệu M0 và schema user/trip | API persistence, UI form/list/detail, kiểm quyền | Web chạy local | Luồng đầy đủ; restart không mất dữ liệu; chặn truy cập chéo |
| M2 · Quy trình | C | Một yêu cầu đổi nhỏ của M1 | Spec, kế hoạch, AI-assisted implementation, review/test | Feature có trace thay đổi | Người học giải thích code AI, sửa lỗi và retest |
| M3 · AI prototype | D | Corpus có provenance và query/task set | RAG, model adapter, agent/tool có giới hạn | Demo có citation + evaluation | Baseline công bằng; thiếu nguồn không kết luận; tool không vượt quyền |
| M4 · Chọn sản phẩm | E | Prototype, dữ liệu đo, vấn đề/người dùng giả định | Kiểm giả thuyết và lựa chọn phạm vi | Project brief + decision note | Tách facts/hypotheses; đủ dữ liệu quyết định hoặc ghi phần thiếu |
| M5 · MVP | F | Phạm vi M4 và acceptance criteria | Hoàn thiện một luồng, test lỗi và phản hồi | Release candidate + demo | Thực hiện được task; lỗi và giới hạn được ghi rõ |
| M6 · Delivery | G | Release candidate | Deploy, monitor, rollback/restore lab | Release + runbook + evidence | Có kết quả thật; chưa deploy thì NOT_TESTED |

## Ranh giới của AI trong bài tập

AI có thể trích thông tin, giải thích nguồn và đề xuất phương án. Validation deterministic quyết định schema, tổng chi phí, xung đột giờ và quyền dữ liệu. Mốc thời gian được khóa chỉ thay đổi khi người dùng quyết định. Không gọi dữ liệu fixture là availability hoặc lịch/giá thực tế.

Bắt đầu bằng tool chỉ đọc. Thao tác ghi chỉ thêm khi contract, approval, idempotency và audit đã rõ. Không mở rộng sang đặt vé, thanh toán hoặc hành động ngoài phạm vi bài tập.

## Một sản phẩm xuyên suốt, nhiều mốc review

Các course đóng góp vào cùng bài tập, không cần tạo nhiều repo giống nhau. Nhánh ML/DL có thể dùng một dataset riêng phù hợp bài toán mô hình; chỉ tích hợp model vào sản phẩm khi đã chứng minh ích lợi so với baseline.

Code có thể ở repo bài tập riêng. Trong repo roadmap lưu commit/link, dữ liệu mẫu được phép, báo cáo và review. Không tự tạo trạng thái “đã chạy” khi mới viết thiết kế.
