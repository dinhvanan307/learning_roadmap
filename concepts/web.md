# Web, API và frontend

[Danh mục concept](../docs/CONCEPTS.md) · [Roadmap](../ROADMAP.md)

**Học trong:** [B2](../learning-path/ai-application-engineer/programs/b-fullstack/courses/fastapi/README.md), [B3](../learning-path/ai-application-engineer/programs/b-fullstack/courses/frontend/README.md).

Các mức ưu tiên là lựa chọn của roadmap cho phạm vi ứng dụng này; không phải bảng xếp hạng độ phổ biến trên thị trường.

| Concept | Hiểu ngắn gọn | Khi dùng | Câu hỏi tự kiểm | Mức |
| --- | --- | --- | --- | --- |
| DNS, IP, port, TCP/TLS | Các tầng định vị, kết nối và bảo vệ giao tiếp; HTTP chạy phía trên transport phù hợp. | Chẩn đoán không gọi được API. | Lỗi DNS khác lỗi HTTP 500 ở đâu? | CORE |
| HTTP method, status, header | Contract trao đổi request/response, gồm ý nghĩa hành động và kết quả. | REST API và client. | Phân biệt input sai, chưa đăng nhập, bị cấm và không tồn tại. | CORE |
| REST và GraphQL | REST tổ chức tài nguyên qua giao diện nhất quán; GraphQL dùng schema và query lựa chọn dữ liệu. | Chọn API phù hợp nhu cầu client. | Không cần triển khai cả hai để đạt cùng một bài tập. | AWARENESS |
| Validation và serialization | Kiểm input theo quy tắc; chuyển dữ liệu thành biểu diễn truyền/lưu. | API boundary và model output. | Field bị bỏ, null và chuỗi rỗng có cùng nghĩa không? | PRACTICE |
| Idempotency | Thực hiện lặp một thao tác theo contract vẫn giữ effect mong muốn. | Retry tạo tài nguyên hoặc xử lý job. | Cùng key khác body và hai request đồng thời được xử lý ra sao? | PRACTICE |
| Pagination và ordering | Chia kết quả theo thứ tự ổn định; offset/cursor có trade-off. | List API lớn hoặc thay đổi liên tục. | Thêm một hàng giữa hai trang có lặp hoặc mất mục? | PRACTICE |
| Authentication và authorization | Xác thực danh tính khác với cho phép hành động trên tài nguyên. | User/tenant và object-level access. | Đăng nhập đúng nhưng đọc trip người khác có bị chặn? | CORE |
| Session, JWT, OAuth và OIDC | Session quản lý trạng thái; JWT là dạng token; OAuth ủy quyền, OIDC bổ sung lớp danh tính. | Tích hợp đăng nhập và API scopes. | JWT ký không đồng nghĩa payload được mã hóa hay mọi claim đáng tin. | AWARENESS |
| CORS và CSRF | CORS kiểm việc browser cho đọc cross-origin; CSRF liên quan request dùng credentials của nạn nhân. | Web gọi API và cookie session. | CORS có thay thế authorization server không? | CORE |
| SSE và WebSocket | SSE truyền event server→client; WebSocket hỗ trợ giao tiếp hai chiều. | Streaming câu trả lời hoặc tương tác realtime. | Client đóng kết nối thì server cleanup thế nào? | PRACTICE |
| Props, state và render | Props là input component; state thay đổi dẫn đến render lại theo mô hình UI. | Form, list và màn hình tương tác. | Dữ liệu nào là state thật, dữ liệu nào suy ra được? | CORE |
| React Hooks và effects | Hooks kết nối state/lifecycle; effect đồng bộ với hệ thống bên ngoài. | Subscription, network hoặc DOM integration. | Effect có cleanup và dependency đúng không? | PRACTICE |
| Server/Client Components | Ranh giới nơi component và logic thực thi trong kiến trúc Next.js. | Data fetching và tương tác UI. | Secret hoặc code DB có lọt vào client bundle? | PRACTICE |
| SSR, CSR và hydration | Render phía server/client; hydration gắn tương tác client lên HTML đã có. | Hiệu năng tải và tính nhất quán UI. | Render mismatch xuất hiện do trạng thái nào? | AWARENESS |
| Accessibility và UI states | Semantic HTML, nhãn, keyboard/focus cùng loading/empty/error. | Luồng người dùng hoàn chỉnh. | Không dùng chuột vẫn hoàn thành form được không? | PRACTICE |

## Nguồn đối chiếu

[MDN HTTP Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview), [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/), [GraphQL Learn](https://graphql.org/learn/), [React Learn](https://react.dev/learn), [Next.js App Router](https://nextjs.org/docs/app/getting-started), [Tailwind Utility Classes](https://tailwindcss.com/docs/styling-with-utility-classes), [RFC 7519 JSON Web Token](https://www.rfc-editor.org/info/rfc7519/).

Bảng là diễn giải phục vụ học tập; bài thực hành và câu hỏi tự kiểm là thiết kế của repo. Đọc đúng phần được chỉ trong unit, sau đó giải thích bằng code hoặc ví dụ thay vì học thuộc bảng.
