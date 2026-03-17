## TASKS – Kế hoạch công việc cho dự án DecoAR / RoomFit

### 1. Tổng quan giai đoạn

- **Giai đoạn 0 – Phân tích & thiết kế**  
  Làm rõ bài toán, phạm vi, yêu cầu chức năng/phi chức năng, kiến trúc tổng thể.

- **Giai đoạn 1 – Prototype AR & đo không gian**  
  Tạo demo quét phòng và đặt mô hình 3D đơn giản (không cần AI).

- **Giai đoạn 2 – Backend & catalog nội thất**  
  Thiết kế dữ liệu, xây dựng API cơ bản, chưa cần LLM.

- **Giai đoạn 3 – Gợi ý thông minh (AI/LLM)**  
  Tích hợp LLM vào backend để gợi ý thông minh hơn.

- **Giai đoạn 4 – Hoàn thiện UX/UI & tích hợp end-to-end**  
  Tối ưu trải nghiệm người dùng, kết nối mượt mà giữa mobile – backend – AI.

- **Giai đoạn 5 – Báo cáo, demo & chuẩn bị bảo vệ**  
  Hoàn thiện tài liệu, slide, video demo và kịch bản thuyết trình.

---

### 2. Chi tiết nhiệm vụ theo giai đoạn

#### 2.1. Giai đoạn 0 – Phân tích & thiết kế

- **0.1. Làm rõ bài toán & phạm vi**
  - Viết problem statement và solution statement ngắn gọn (1–2 trang).
  - Xác định rõ phạm vi demo: loại phòng chủ đạo (ví dụ: phòng ngủ/phòng khách), số lượng món đồ nội thất mẫu.

- **0.2. Phân tích nghiệp vụ & luồng người dùng**
  - Vẽ user flow:
    - Mở app → scan phòng → nhập/chọn phong cách → nhận gợi ý → đặt đồ AR → tinh chỉnh.
  - Liệt kê các trường hợp sử dụng (Use Cases) chính.

- **0.3. Thiết kế kiến trúc tổng thể**
  - Vẽ sơ đồ kiến trúc: Mobile App (AR) ↔ Backend API ↔ LLM Provider ↔ Database.
  - Xác định các module chính ở backend (auth – nếu cần, catalog, recommendation, integration AI).

- **0.4. Thiết kế UI/UX ở mức wireframe**
  - Vẽ mockup các màn: màn intro, màn quét phòng AR, màn danh sách gợi ý, màn chi tiết item.
  - Chọn phong cách thiết kế (minimal, hiện đại).

---

#### 2.2. Giai đoạn 1 – Prototype AR & đo không gian

- **1.1. Chuẩn bị môi trường mobile (chưa cần code chi tiết)**
  - Cài đặt Android Studio.
  - Kiểm tra thiết bị Android có hỗ trợ ARCore.
  - Tạo project Android trống, cấu hình minSdk phù hợp.

- **1.2. Prototype AR cơ bản**
  - Tích hợp ARCore (hoặc Unity + AR Foundation nếu đổi hướng).
  - Hiển thị camera feed và phát hiện mặt phẳng sàn.
  - Đặt một mô hình 3D đơn giản (ví dụ khối hộp) lên mặt phẳng.

- **1.3. Đo kích thước không gian**
  - Thiết kế flow cho người dùng chọn 2–3 điểm trên sàn.
  - Tính toán khoảng cách giữa các điểm để ước lượng chiều dài, chiều rộng khu vực.
  - Hiển thị kết quả đo cho người dùng (ví dụ: 1.6m × 2.1m).

---

#### 2.3. Giai đoạn 2 – Backend & catalog nội thất

- **2.1. Thiết kế dữ liệu nội thất**
  - Xác định các thuộc tính cho một món đồ: kích thước, loại, phong cách, mô tả, URL model 3D, ảnh thumbnail, v.v.
  - Vẽ sơ đồ ERD đơn giản (nếu dùng SQL).

- **2.2. Thiết kế API**
  - Định nghĩa các endpoint chính:
    - Lấy danh sách đồ nội thất.
    - Lọc đồ nội thất theo kích thước/phòng/phong cách.
    - Gợi ý cơ bản (không dùng AI).
  - Xác định model request/response (JSON schema).

- **2.3. Thiết lập backend**
  - Khởi tạo project Python + FastAPI.
  - Thêm thư viện quản lý DB (SQLAlchemy hoặc ORM khác).
  - Cấu hình database (local: SQLite hoặc PostgreSQL).

- **2.4. Seed dữ liệu mẫu**
  - Tạo một bộ dữ liệu nhỏ (10–30 món đồ) đủ cho demo.
  - Viết script seed vào DB.

---

#### 2.4. Giai đoạn 3 – Gợi ý thông minh (AI/LLM)

- **3.1. Phân tích logic gợi ý**
  - Xác định đầu vào cho gợi ý:
    - Thông tin không gian (kích thước, loại phòng).
    - Phong cách mong muốn.
    - Yêu cầu thêm: budget, sở thích (mở rộng).
  - Xác định tiêu chí lựa chọn đồ: vừa kích thước, đúng chức năng, đúng phong cách.

- **3.2. Thiết kế prompt & pipeline LLM**
  - Viết prompt mẫu cho LLM: mô tả bối cảnh, dữ liệu đồ nội thất, yêu cầu output.
  - Thiết kế pipeline:
    - Backend lọc trước đồ phù hợp kích thước.
    - Gửi danh sách rút gọn + ngữ cảnh cho LLM.
    - Nhận lại danh sách ưu tiên + lý do gợi ý.

- **3.3. Tích hợp LLM vào backend**
  - Chọn provider (OpenAI, Gemini, v.v.) và phương thức gọi API.
  - Xây dựng service gọi LLM (module riêng).
  - Thử nghiệm và điều chỉnh prompt cho kết quả ổn định.

- **3.4. Nâng cấp API gợi ý**
  - Thêm endpoint gợi ý “thông minh”.
  - Chuẩn hóa response để mobile dễ hiển thị (thông tin đồ + lý do + dữ liệu model 3D).

---

#### 2.5. Giai đoạn 4 – Hoàn thiện UX/UI & tích hợp end-to-end

- **4.1. Tích hợp mobile ↔ backend**
  - Backend trả dữ liệu gợi ý.
  - Mobile hiển thị danh sách đồ gợi ý.
  - Khi chọn item, mobile tải model 3D tương ứng để đặt trong AR.

- **4.2. Tối ưu trải nghiệm AR**
  - Chỉnh lại scale mô hình cho đúng kích thước thực tế (1:1).
  - Cải thiện điều khiển: chạm để chọn, kéo để di chuyển, gesture để xoay.
  - Hiển thị bóng đổ/ánh sáng cơ bản (nếu framework hỗ trợ).

- **4.3. Cải thiện UI/UX tổng thể**
  - Thêm màn onboarding/hướng dẫn scan phòng.
  - Xử lý các trạng thái lỗi (mất mạng, lỗi backend, lỗi AR).
  - Tinh chỉnh layout, màu sắc, icon cho nhất quán.

---

#### 2.6. Giai đoạn 5 – Báo cáo, demo & bảo vệ

- **5.1. Tài liệu kỹ thuật**
  - Viết chi tiết kiến trúc hệ thống.
  - Viết mô tả thiết kế dữ liệu, API, và integration AI.
  - Tóm tắt các quyết định kỹ thuật và lý do lựa chọn.

- **5.2. Demo & slide thuyết trình**
  - Quay video demo: từ lúc scan phòng đến lúc đặt đồ AR.
  - Thiết kế slide theo flow: Problem → Solution → Demo → Tech → Architecture → Future Work.
  - Chuẩn bị script trình bày, chia người nói (nếu làm nhóm).

- **5.3. Ôn tập & chuẩn bị câu hỏi phản biện**
  - Dự đoán câu hỏi giảng viên có thể hỏi (tech stack, hạn chế, hướng phát triển).
  - Chuẩn bị câu trả lời ngắn gọn, có số liệu/luận điểm rõ ràng.

---

### 3. Gợi ý phân bổ thời gian (mang tính tham khảo)

- **Tuần 1–2**: Giai đoạn 0 – Phân tích & thiết kế.
- **Tuần 3–4**: Giai đoạn 1 – Prototype AR.
- **Tuần 5–6**: Giai đoạn 2 – Backend & catalog.
- **Tuần 7–8**: Giai đoạn 3 – Gợi ý AI.
- **Tuần 9–10**: Giai đoạn 4 – UX/UI & tích hợp end-to-end.
- **Tuần 11–12**: Giai đoạn 5 – Tài liệu, demo, luyện bảo vệ.

