# AI05 · Embedding, retrieval, RAG và fine-tuning

[Mục lục](../README.md) · [Bài trước](04-prompt-context-memory.md) · [Bài sau](06-tools-agents.md)

**Mục tiêu:** hiểu cách đưa tài liệu vào câu trả lời và kiểm nguồn. **Thời lượng đọc:** khoảng 20 phút.

## Từ tài liệu tới câu trả lời

```text
Tài liệu → parse/OCR → record có nguồn → chunk → embedding/index
Câu hỏi → retrieval → tập ứng viên → có thể rerank → context
Context + câu hỏi → model → câu trả lời + nguồn → kiểm chứng
```

RAG ghép truy xuất với sinh câu trả lời. Corpus cần được xử lý, cập nhật và kiểm quyền; model chỉ dùng được phần dữ liệu thực sự đưa vào context, không tự đọc toàn bộ database.

| Concept | Vai trò |
| --- | --- |
| Chunk | Đơn vị nội dung dùng khi truy xuất; chia phải giữ đủ nghĩa và metadata |
| Embedding | Vector biểu diễn input do model phù hợp tạo ra |
| Index | Cấu trúc hỗ trợ tìm kiếm; không đồng nghĩa cứ có index là tìm đúng |
| Lexical / dense retrieval | Tìm theo tín hiệu từ vựng / biểu diễn vector; đều cần đánh giá trên bài toán |
| Top-k / reranker | Lấy tập ứng viên / sắp lại các ứng viên bằng cách chấm phù hợp |
| Grounding / citation | Neo nội dung vào nguồn / chỉ tới nguồn; citation cần được kiểm có hỗ trợ claim |

## Ví dụ cosine trên vector tự đặt

Cosine đo độ cùng hướng: tích vô hướng chia cho tích độ dài. Nó không phải xác suất câu trả lời đúng. Trong ví dụ sau, vector do người viết đặt để học phép tính, **không phải embedding sinh từ văn bản**.

```python
from math import isclose, sqrt

def cosine(left, right):
    if len(left) != len(right):
        raise ValueError("dimensions must match")
    norm_left = sqrt(sum(x * x for x in left))
    norm_right = sqrt(sum(x * x for x in right))
    if norm_left == 0 or norm_right == 0:
        raise ValueError("zero vectors have no cosine direction")
    return sum(x * y for x, y in zip(left, right)) / (norm_left * norm_right)

vectors = {"note-python": [1, 0], "note-sql": [0, 1]}
query = [1, 0]
ranked = sorted(vectors, key=lambda key: cosine(query, vectors[key]), reverse=True)
assert ranked == ["note-python", "note-sql"]
assert isclose(cosine([1, 1], [1, 0]), 1 / sqrt(2))
try:
    cosine([0, 0], [1, 0])
except ValueError:
    print("AI05 OK: ranking demonstrated; zero vector rejected")
else:
    raise AssertionError("zero vector must be rejected")
```

[File chạy được](../examples/ai05.py). Code chỉ minh họa similarity/ranking; chưa có ingestion, embedding model hay generation để gọi là RAG hoàn chỉnh.

## Prompt, RAG hay fine-tuning?

| Cách | Thay đổi chủ yếu | Câu hỏi cần đặt |
| --- | --- | --- |
| Prompt/context | Input của lần xử lý | Đã có đủ thông tin liên quan và output contract chưa? |
| RAG | Cách tìm/cấp nguồn lúc dùng | Tài liệu có được tìm đúng, còn hiệu lực và được phép xem không? |
| Fine-tuning | Parameters hoặc adapter qua training bổ sung | Dữ liệu và mục tiêu học có sửa đúng loại lỗi, tốt hơn baseline không? |

Các cách có thể kết hợp. Fine-tuning không tự bảo đảm nhớ đúng mọi facts hoặc thay thế kho nguồn cập nhật. Trước khi tăng độ phức tạp, xác định lỗi nằm ở truy xuất, thiếu context hay hành vi sinh.

## Tự kiểm

1. Có citation nhưng đoạn trích không nói điều model kết luận thì đạt chưa?
2. Retrieval bỏ mất đoạn cần thiết có sửa chắc chắn bằng prompt tốt hơn không?
3. Vector gần nhau có chứng minh hai câu đồng nghĩa trong mọi ngữ cảnh không?

<details>
<summary>Đáp án ngắn</summary>

1. Chưa, nguồn phải hỗ trợ claim. 2. Không; phải sửa/đánh giá tầng truy xuất. 3. Không, phụ thuộc model, dữ liệu và mục tiêu đo.

</details>

**Bài tập 15 phút:** tạo năm ghi chú và ba câu hỏi: đủ nguồn, thiếu nguồn, nguồn mâu thuẫn. Chọn đoạn hỗ trợ bằng tay trước; không cần gọi model để kiểm logic evidence.

**Nguồn:** [Microsoft RAG Overview](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview), [Hugging Face Fine-tuning](https://huggingface.co/docs/transformers/training). Đi sâu theo [D.3](../../../ROADMAP.md#d-3).
