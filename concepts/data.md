# Dữ liệu, SQL và NoSQL

[Danh mục concept](../docs/CONCEPTS.md) · [Roadmap](../ROADMAP.md)

**Học trong:** [A2](../learning-path/ai-application-engineer/programs/a-python/courses/python-libraries/README.md), [B1](../learning-path/ai-application-engineer/programs/b-fullstack/courses/database/README.md).

Các mức ưu tiên là lựa chọn của roadmap cho phạm vi ứng dụng này; không phải bảng xếp hạng độ phổ biến trên thị trường.

| Concept | Hiểu ngắn gọn | Khi dùng | Câu hỏi tự kiểm | Mức |
| --- | --- | --- | --- | --- |
| Schema và data contract | Quy tắc về field, kiểu, khóa và ý nghĩa dữ liệu. | Ingestion và giao tiếp giữa các tầng. | Schema hợp lệ nhưng giá trị sai nghiệp vụ có qua được không? | CORE |
| PK, FK và constraint | Định danh, tham chiếu và điều kiện DB cưỡng chế. | Ngăn trùng ID, tham chiếu thiếu và dữ liệu sai. | Client bỏ validation thì DB chặn được gì? | PRACTICE |
| NULL và three-valued logic | NULL biểu diễn thiếu/không biết; so sánh SQL có thể cho UNKNOWN. | Filter, aggregate và LEFT JOIN. | COUNT(*) khác COUNT(column) thế nào? | CORE |
| JOIN và cardinality | Ghép hàng theo điều kiện; số dòng phụ thuộc quan hệ và tính duy nhất của khóa. | Báo cáo dữ liệu nhiều bảng. | Vì sao merge làm tổng tiền tăng gấp đôi? | PRACTICE |
| Normalization | Tổ chức quan hệ để giảm dư thừa và bất nhất cập nhật. | Schema nghiệp vụ. | Một tên địa điểm đổi phải sửa bao nhiêu nơi? | CORE |
| Transaction và ACID | Gom thao tác thành đơn vị với các bảo đảm của DB/cấu hình. | Ghi job cùng dữ liệu liên quan. | Exception giữa hai câu lệnh có để trạng thái nửa vời? | PRACTICE |
| Isolation và lost update | Mức cô lập quyết định quan sát tương tác đồng thời; read-modify-write có thể mất cập nhật. | Nhiều request sửa cùng bản ghi. | Hai session cùng tăng counter thì invariant còn đúng? | PRACTICE |
| Optimistic locking | So version trước khi ghi để phát hiện dữ liệu đã đổi. | Form sửa lịch từ bản đọc cũ. | Conflict được báo và xử lý thế nào? | PRACTICE |
| Index và query plan | Index hỗ trợ access path; optimizer chọn kế hoạch dựa trên điều kiện/thống kê. | Truy vấn chậm trên dữ liệu đủ lớn. | Có index mà vẫn scan có luôn là lỗi? | PRACTICE |
| ORM, session và N+1 | Ánh xạ object–DB; cách tải quan hệ có thể tạo quá nhiều query. | FastAPI persistence. | Một màn danh sách thực sự phát bao nhiêu SQL? | PRACTICE |
| Migration | Biến đổi schema/dữ liệu có phiên bản và kế hoạch tương thích. | Thêm field hoặc thay contract lưu trữ. | Dữ liệu cũ và app cũ còn đọc được không? | PRACTICE |
| NoSQL document và key-value | Hai kiểu mô hình lưu trữ phục vụ access pattern khác nhau. | Dữ liệu tài liệu, cache, trạng thái. | Lý do chọn dựa trên query hay chỉ vì tên công nghệ? | AWARENESS |
| Cache, TTL và invalidation | Giữ bản sao để truy cập nhanh; cần quy tắc hết hạn/cập nhật. | Giảm đọc lặp hoặc gọi dịch vụ tốn phí. | Cache hỏng hoặc stale thì nguồn chuẩn ở đâu? | PRACTICE |
| Shape, broadcasting, view/copy | Quy tắc kích thước và chia sẻ bộ nhớ trong thao tác mảng. | NumPy và dữ liệu vector. | Phép tính đúng shape có đúng ý nghĩa axis không? | CORE |
| Missing, outlier và aggregation | Quyết định cách xử lý dữ liệu thiếu/lệch trước khi tổng hợp. | Pandas và báo cáo. | Mẫu nào bị loại và có làm sai kết luận nhóm? | PRACTICE |
| ETL/ELT và lineage | Biến đổi/đưa dữ liệu vào hệ thống; lineage ghi nguồn và chuỗi xử lý. | Ingestion có thể tái lập. | Truy được một giá trị về file/phiên bản gốc không? | CORE |

## Nguồn đối chiếu

[PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html), [PostgreSQL Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html), [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/), [NumPy Basics](https://numpy.org/doc/stable/user/absolute_beginners.html), [pandas Intro Tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html), [Redis Quick Starts](https://redis.io/docs/latest/develop/get-started/).

Bảng là diễn giải phục vụ học tập; bài thực hành và câu hỏi tự kiểm là thiết kế của repo. Đọc đúng phần được chỉ trong unit, sau đó giải thích bằng code hoặc ví dụ thay vì học thuộc bảng.
