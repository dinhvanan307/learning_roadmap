# Bài tổng hợp tùy chọn · Tra cứu ghi chú học tập

[Mục lục](README.md) · [Phiếu tự ôn](REVIEW.md)

**Thời gian gợi ý:** 60–90 phút sau lượt đọc. Đây là đề bài để bạn tự làm; repo chưa có lời giải hoàn chỉnh hoặc kết quả làm bài của bạn. Dùng Python chuẩn, chưa cần API, database hay model thật.

## Mục tiêu

Nối Python, OOP và tư duy kiểm bằng chứng: nhập một tập ghi chú → kiểm dữ liệu → tìm theo từ khóa → trả nguyên văn kết quả và ID nguồn. Tìm từ khóa này là baseline đơn giản, chưa phải semantic retrieval hay RAG hoàn chỉnh.

## Dữ liệu mẫu

```json
[
  {"id": "n1", "title": "Python", "text": "List có thể thay đổi nội dung."},
  {"id": "n2", "title": "OOP", "text": "Composition ghép object theo trách nhiệm."},
  {"id": "n3", "title": "Lịch học", "text": "Buổi ôn bắt đầu lúc 19:00."}
]
```

## Contract

1. Input phải là list các object; mỗi object có id/title/text là chuỗi sau trim không rỗng. ID duy nhất; record sai hoặc trùng làm cả lần nhập bị từ chối với lỗi rõ ràng. Không sửa input và không giữ trạng thái nhập dở.
2. Model dữ liệu `Note` dùng dataclass hoặc class thường; giải thích lựa chọn. Tags không bắt buộc.
3. `KeywordRetriever.search(query)` tìm substring không phân biệt hoa/thường trong title + text. Query được trim, rỗng bị từ chối. Kết quả giữ thứ tự nguồn, không dùng điểm similarity giả.
4. `NoteService` nhận retriever qua constructor, không đọc file trực tiếp trong method tìm kiếm.
5. Kết quả có `status`, `matches`; mỗi match có `source_id`, `text` nguyên văn. Có match thì status = `found`, không có thì `not_found`. `found` chỉ nói có khớp từ khóa, không xác nhận đủ bằng chứng trả lời mọi câu hỏi.

## Expected để bắt đầu

| Input | Expected |
| --- | --- |
| Query `LIST` | found; chỉ source_id n1, giữ đúng text của n1 |
| Query `composition` | found; chỉ n2 |
| Query `deadline` | not_found; matches rỗng |
| Query chỉ dấu cách | Lỗi query rỗng |
| Dataset có hai record id n1 | Từ chối lần nhập, không mất dấu lỗi |
| title là số hoặc text rỗng | Từ chối với vị trí/ID record nếu xác định được |

## Bài nộp nhỏ

- Mã đọc/validate, `Note`, retriever và service; một file cũng được nếu các trách nhiệm rõ.
- README nêu lệnh chạy, input/output và giới hạn.
- Test các expected ở trên, thêm hai instance không chia sẻ state và input không bị sửa.
- Năm dòng giải thích: contract, composition, một bug đã sửa, nguồn expected và phần AI hỗ trợ nếu có.

## Thiết kế bước AI, chưa cần gọi model

Vẽ nơi bạn sẽ thêm `Answerer` nhận câu hỏi + matches. Với “Deadline nộp bài là khi nào?”, không được suy thời hạn từ giờ bắt đầu buổi học ở n3. Nêu cơ chế trả `insufficient_evidence`, schema output, ca cần test và cách giữ ID nguồn.

Giải thích thêm: điều gì cần đổi nếu thay baseline từ khóa bằng embedding, vì sao JSON hợp lệ chưa chứng minh câu trả lời đúng, và bước nào phải kiểm quyền khi có nhiều người dùng. Không cần cài agent để hoàn thành bài này.
