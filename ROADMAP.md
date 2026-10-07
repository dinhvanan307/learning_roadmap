# Roadmap AI Application Engineer

Mục tiêu là phát triển khả năng thiết kế, triển khai, đánh giá và vận hành ứng dụng AI thông qua bài làm có thể kiểm tra. Lộ trình khởi tạo từ [dashboard hiện có](AI-Application-Roadmap-Dashboard.html); xem [ghi chú nguồn](docs/SOURCE.md) để phân biệt nội dung gốc với quy ước theo dõi của repo.

## Phạm vi và lịch học

**Full-track:** W0 và W1–W12, tổng 116 hạng mục, **288 giờ dự kiến**. W0 chiếm 20 giờ; 12 tuần chính chiếm 268 giờ. Mỗi tuần là một đơn vị nội dung, có thể kéo dài hơn một tuần lịch khi cần học bù hoặc sửa bài.

Bắt đầu bằng đối chiếu W0 với bài làm đã có. Chỉ bỏ qua phần đầu vào khi có bằng chứng đáp ứng yêu cầu; không mặc định đã có nền backend chỉ vì chọn lịch nhanh. Ngày bắt đầu và giờ thực tế được ghi trong [PROGRESS.md](PROGRESS.md).

## Các giai đoạn

| Giai đoạn | Tuần | Giờ dự kiến | Đầu ra chính |
| --- | --- | ---: | --- |
| P0 · Prerequisites | W0 | 20 | Bài Python, API/SSE, SQL, Git/Docker/CI và toán tối thiểu để kiểm tra đầu vào. |
| P1 · Nền tảng | W1–W3 | 66 | Ma trận chọn model có số đo, prompt-kit và dịch vụ AI Chat P1. |
| P2 · Data & Knowledge | W4–W6 | 66 | Retrieval benchmark và hệ thống hỏi đáp tài liệu P2 có nguồn và quyền truy cập. |
| P3 · Agent Systems | W7–W9 | 63 | Agent đa bước, checkpoint/resume và hệ thống tích hợp MCP P3. |
| P4 · Production | W10–W12 | 73 | Evaluation/observability, thử nghiệm bảo mật/chi phí và capstone có demo, runbook. |

## Kế hoạch từng tuần

| Tuần | Trọng tâm | Hạng mục | Giờ dự kiến | Tiêu chí hoàn thành từ bản gốc |
| --- | --- | ---: | ---: | --- |
| [W0](weeks/W00.md) | Prerequisites (chỉ Full-track) | 5 | 20 | Giải thích được sync/async, stateless/stateful; debug được API bằng curl |
| [W1](weeks/W01.md) | LLM Foundations & Model Selection | 9 | 22 | Trình bày ma trận chọn model kèm số liệu TỰ ĐO (quality/latency/cost), không copy blog |
| [W2](weeks/W02.md) | Prompt & Context Engineering | 9 | 22 | Chứng minh prompt v2 tốt hơn v1 bao nhiêu %, trên tiêu chí gì |
| [W3](weeks/W03.md) | AI App Architecture → P1 | 9 | 22 | 100 req đồng thời không sập; đổi model qua env; xem được cost/conversation; cancel không rò token |
| [W4](weeks/W04.md) | Embedding & Vector Retrieval | 8 | 22 | Nêu chiến lược chunking tốt nhất cho corpus của mình KÈM BẰNG CHỨNG |
| [W5](weeks/W05.md) | Advanced RAG & Failure Modes | 9 | 22 | Bảng số liệu naive→hybrid→rerank→rewrite; chẩn đoán được cả 7 failure mode |
| [W6](weeks/W06.md) | KMS / RAG System → P2 | 10 | 22 | recall@5 ≥ 0.85; mọi câu trả lời có citation; user A không bao giờ thấy tài liệu user B |
| [W7](weeks/W07.md) | Tool Calling & Agent from Scratch | 6 | 20 | Agent tự viết (không framework) hoàn thành 1 nhiệm vụ đa bước thật |
| [W8](weeks/W08.md) | Orchestration: Graph, State, Multi-Agent | 7 | 20 | Agent resume đúng chỗ sau khi kill; kết luận trung thực multi-agent có tốt hơn không |
| [W9](weeks/W09.md) | MCP & Tool Ecosystem → P3 | 10 | 23 | ≥80% trên 20 kịch bản; mọi hành động ghi/xóa qua approval; trace giải thích được quyết định |
| [W10](weeks/W10.md) | Evaluation & Observability | 9 | 22 | Đổi 1 prompt → biết chính xác tốt/xấu bao nhiêu %, trên tiêu chí nào, trong 10 phút |
| [W11](weeks/W11.md) | Security, Cost, Scale + Fine-tuning | 12 | 24 | Bypass rate <10% sau phòng thủ; trình bày cây quyết định fine-tune kèm số liệu thí nghiệm |
| [W12](weeks/W12.md) | CAPSTONE & Deploy | 13 | 27 | Pass đủ 12 hạng mục rubric nghiệm thu + defense 15 phút |

Các ngưỡng như recall@5 ≥ 0,85 hay success ≥ 80% là mục tiêu thực hành trong kế hoạch gốc. Khi nộp bài, cần chỉ rõ tập dữ liệu, số mẫu và cách đo. Test quyền truy cập chứng minh hành vi trên các trường hợp đã kiểm tra; không biến một bộ test thành cam kết tuyệt đối về mọi dữ liệu hoặc người dùng.

So sánh hai phương án có thể cho thấy không cải thiện. Ghi nhận kết quả đó và phân tích nguyên nhân; không sửa số liệu để đạt mục tiêu trên giấy.

## Lịch rút gọn 8 khối

Bản gốc gom W1–W12 thành F1–F8 và bỏ W0. Nếu giữ nguyên toàn bộ hạng mục, khối lượng vẫn là **268 giờ**, tức **33,5 giờ/tuần** khi làm trong 8 tuần. Con số khoảng 22 giờ/tuần trên dashboard không khớp tổng hạng mục; cần đổi lịch hoặc quyết định rõ phần được miễn bằng bằng chứng.

| Khối | Nội dung tương ứng | Giờ nếu giữ đủ nội dung |
| --- | --- | ---: |
| F1 | [W1](weeks/W01.md), [W2](weeks/W02.md) | 44 |
| F2 | [W3](weeks/W03.md) | 22 |
| F3 | [W4](weeks/W04.md), [W5](weeks/W05.md) | 44 |
| F4 | [W6](weeks/W06.md) | 22 |
| F5 | [W7](weeks/W07.md), [W8](weeks/W08.md) | 40 |
| F6 | [W9](weeks/W09.md) | 23 |
| F7 | [W10](weeks/W10.md) | 22 |
| F8 | [W11](weeks/W11.md), [W12](weeks/W12.md) | 51 |

Dù học theo F1–F8, vẫn cập nhật từng W trong bảng tiến độ để không mất dấu tiêu chí. Ghi riêng quyết định miễn/giảm phạm vi và bằng chứng; bản rút gọn không tự xác nhận hoàn thành W0.

## Cách chuyển sang tuần tiếp theo

1. Hoàn thành bài thực hành và ghi kết quả vào [nhật ký](templates/WEEKLY_REVIEW.md).
2. Đối chiếu tiêu chí tuần bằng output, lệnh chạy và giải thích của người học.
3. Ghi rõ người review, phần còn thiếu và quyết định tiếp tục hoặc bổ sung trong [PROGRESS.md](PROGRESS.md).
4. Sau mỗi giai đoạn, cập nhật [bảng năng lực](COMPETENCIES.md) bằng link tới bằng chứng.

Hoàn thành lịch không tự chứng minh cấp bậc nghề nghiệp. Kế hoạch này là khung bài học và đầu ra; tài liệu đọc, hướng dẫn lab chi tiết và ước lượng phù hợp từng người có thể được bổ sung khi triển khai mỗi tuần.
