# Nguồn và kiểm chứng bộ bài ôn

Ngày kiểm: **07/10/2026**. Nội dung là tài liệu ôn và ví dụ minh họa, chưa phải kết quả học của người dùng.

## Nội dung và nguồn

- 14 bài: 8 Python/OOP và 6 AI; mỗi bài có mục tiêu, giải thích, ví dụ/tình huống, ba câu tự kiểm có đáp án và bài tập.
- Python đối chiếu tài liệu chính thức về kiểu dữ liệu, hàm, module, exception, class, dataclass, ABC/typing, context manager, asyncio và unittest.
- AI đối chiếu Google ML Crash Course, scikit-learn, Hugging Face; RAG/agent tham khảo Microsoft và Anthropic, MCP theo tài liệu giao thức. Skill/hook dùng tài liệu Claude Code làm ví dụ triển khai.
- URL và phần đọc đặt cuối từng bài. Cách chia bài, thời lượng, dữ liệu, câu hỏi và ví dụ code là thiết kế riêng của repo; không sao chép toàn bộ tutorial hoặc dùng nguồn làm chứng nhận năng lực.

## Ví dụ thực thi

**Đã chạy 11/11 file thành công trên Python 3.14.7**, bằng thư viện chuẩn, không cài package hoặc gọi mạng/API. Code trong file `.py` khớp khối Python của bài tương ứng; khi sửa cần đồng bộ cả hai. Ví dụ hướng tới Python 3.11+ vì P07 dùng TaskGroup; chưa chạy mọi phiên bản Python.

| Ví dụ | Hành vi đã kiểm trong demo |
| --- | --- |
| p01 | Aliasing, copy nông/sâu, comprehension và giữ giá trị 0 |
| p02 | Không sửa history, default tách biệt và từ chối bool |
| p03 | Đọc JSON, trim title, từ chối sai kiểu và dọn file tạm |
| p04 | List tags riêng từng instance, classmethod và equality/identity |
| p05 | Hai implementation retriever dùng chung service |
| p06 | Generator cạn, decorator giữ metadata và stream đóng sau dùng |
| p07 | Giới hạn concurrency, timeout và cleanup khi hủy |
| p08 | Ba test method về trim, chuỗi rỗng và sai kiểu |
| ai02 | Accuracy 0.9 nhưng recall 0 trên fixture lệch nhãn |
| ai05 | Ranking cosine, đối chiếu phép tính và từ chối vector 0 |
| ai06 | Tool đọc, từ chối tool ngoài allowlist và dừng theo budget |

Các demo có phạm vi nhỏ, không đại diện bộ test production. AI02 chỉ tính metric; AI05 dùng vector đặt tay; AI06 dùng đề xuất tool cố định. **Chưa gọi LLM, chưa training model, chưa xây RAG/agent hoàn chỉnh.** Bài tổng hợp là đề để người học tự làm, không có trạng thái hoàn thành được tự gán.

Đã thử bản sao P08 bỏ `.strip()` và thấy test fail; bản gốc vẫn giữ nguyên. Kiểm cú pháp theo Python 3.11, đường dẫn/anchor Markdown, số cột bảng và đối chiếu code bài với file ví dụ đều đạt. Trạng thái course/phase/CLO và 21 file trong archive được giữ nguyên.

[Mục lục](README.md) · [Phiếu tự ôn](REVIEW.md)
