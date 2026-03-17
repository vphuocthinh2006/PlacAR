## 02 – Kiến trúc hệ thống (System Architecture)

### 1. Sơ đồ kiến trúc tổng quan (mô tả)

Ở mức logic, hệ thống DecoAR / RoomFit được chia thành 4 khối chính:

1. **Mobile AR Client (Android + ARCore)**
2. **Backend API (FastAPI – Python)**
3. **AI/LLM Service (External Provider)**
4. **Database (Catalog nội thất)**

Luồng tương tác (mô tả text):

1. Người dùng mở app, bật camera và quét phòng → Mobile dùng ARCore nhận diện mặt phẳng sàn và đo kích thước vùng trống.
2. Mobile thu thập:
   - Thông tin không gian (width/length, dạng m²).
   - Thông tin ngữ cảnh (loại phòng, phong cách, yêu cầu thêm).
   → Gửi request đến Backend qua HTTP/JSON.
3. Backend:
   - Đọc thông tin phòng.
   - Query Database để lấy danh sách đồ nội thất candidate.
   - Nếu dùng gợi ý thông minh:
     - Chuẩn bị prompt + dữ liệu → gọi AI/LLM Provider.
     - Nhận lại danh sách được xếp hạng + lý do gợi ý.
   → Trả danh sách gợi ý (list items) về Mobile.
4. Mobile hiển thị danh sách gợi ý, khi user chọn một item:
   - Mobile tải model 3D từ URL (hoặc bundle sẵn).
   - Đặt mô hình lên mặt phẳng sàn trong AR với scale 1:1.

---

### 2. Các thành phần chính

#### 2.1. Mobile AR Client

- **Module AR**:
  - Tích hợp ARCore.
  - Phát hiện/visualize mặt phẳng.
  - Đo kích thước vùng trống (đánh dấu điểm A, B, C…).

- **Module UI/UX**:
  - Màn hình onboarding/hướng dẫn.
  - Màn hình camera AR.
  - Màn hình danh sách gợi ý nội thất.
  - Màn hình chi tiết một món đồ (thông tin, kích thước, button “Đặt vào AR”).

- **Module Networking**:
  - Gửi request gợi ý đến Backend.
  - Xử lý response, hiển thị kết quả, quản lý lỗi kết nối.

#### 2.2. Backend API

- **Layer Routing (FastAPI)**:
  - Endpoint health check.
  - Endpoint catalog (list/detail).
  - Endpoint gợi ý cơ bản.
  - Endpoint gợi ý thông minh (AI/LLM).

- **Business Layer (Services)**:
  - Service quản lý catalog nội thất.
  - Service recommendation:
    - Logic filter theo kích thước/phòng/phong cách.
    - Kết hợp với AI/LLM nếu được bật.

- **Integration Layer (AI/LLM)**:
  - Module gọi API OpenAI/Gemini (hoặc provider khác).
  - Chuẩn hóa prompt và parse kết quả.

- **Data Layer**:
  - ORM (SQLAlchemy).
  - Model dữ liệu nội thất.
  - Migration script (nếu dùng Alembic).

#### 2.3. AI/LLM Provider

- Thành phần bên ngoài, giao tiếp qua HTTP.
- Chịu trách nhiệm:
  - Hiểu yêu cầu ngữ cảnh từ người dùng.
  - Xử lý text, tái xếp hạng danh sách candidate.
  - Sinh ra mô tả/lý do gợi ý.

#### 2.4. Database

- CSDL quan hệ (SQL):
  - Bảng `furniture_items` (core).
  - Có thể mở rộng:
    - `styles`, `room_types`, `users` (nếu cần).

---

### 3. Luồng dữ liệu chính (Data Flow)

#### 3.1. Luồng “Scan phòng → Gợi ý cơ bản”

1. User scan phòng, đánh dấu khu vực cần đặt đồ.
2. Mobile tính toán kích thước vùng trống (m²).
3. Mobile gửi request `POST /recommend/basic`:
   - Kèm thông tin: chiều dài, chiều rộng, loại phòng, phong cách (optional).
4. Backend:
   - Dùng logic thuần (không AI) để lọc đồ từ DB:
     - Loại đồ tương ứng với loại phòng.
     - Kích thước không vượt quá một ngưỡng tỉ lệ diện tích.
   - Trả list các món phù hợp.
5. Mobile hiển thị danh sách gợi ý và cho phép người dùng chọn item để đặt AR.

#### 3.2. Luồng “Scan phòng → Gợi ý thông minh (AI/LLM)”

1. Các bước 1–3 giống gợi ý cơ bản, nhưng request gửi đến `POST /recommend/ai`.
2. Backend:
   - Lọc sơ bộ danh sách đồ nội thất từ DB (candidate set).
   - Tạo prompt chứa:
     - Thông tin phòng + style + yêu cầu text.
     - Danh sách candidate (tên + kích thước + loại + style).
   - Gửi prompt cho LLM và nhận kết quả:
     - Top k món đồ + lý do chọn.
   - Chuẩn hóa kết quả, trả về Mobile.
3. Mobile hiển thị list gợi ý nâng cao, có lý do chi tiết hơn.

---

### 4. Các quyết định kiến trúc chính

- **Tách Mobile và Backend**:
  - Giúp backend có thể tái sử dụng cho nhiều client (mobile khác, web…).
  - Dễ bảo trì, nâng cấp logic gợi ý mà không phải update app.

- **Đặt AI/LLM phía Backend thay vì phía Mobile**:
  - Bảo mật API key.
  - Linh hoạt chuyển đổi provider hoặc prompt mà không cần đổi app.
  - Cho phép logging và theo dõi hiệu suất AI.

- **Dùng CSDL quan hệ (SQL)**:
  - Dữ liệu nội thất có cấu trúc rõ ràng, quan hệ đơn giản.
  - Dễ query theo kích thước, loại, phong cách.

---

### 5. Hướng mở rộng kiến trúc

- Thêm:
  - Module user account (login, lưu layout, lịch sử gợi ý).
  - Analytics: log hành vi người dùng để cải thiện gợi ý.
  - Tích hợp với hệ thống e-commerce (link đến trang mua đồ).

- Chuyển đổi hạ tầng:
  - Deploy backend trên cloud (GCP/AWS/Azure).
  - Dùng managed DB thay cho SQLite local.
  - Xây dựng pipeline CI/CD để tự động build & deploy.

