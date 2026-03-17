## 09 – Rủi ro & Giải pháp (Risks & Mitigations)

Tài liệu này liệt kê các rủi ro chính của dự án DecoAR / RoomFit và hướng xử lý.

---

### 1. Rủi ro kỹ thuật (Technical Risks)

#### 1.1. AR không ổn định trên một số thiết bị

- **Mô tả**: Không phải mọi thiết bị Android đều hỗ trợ ARCore tốt; có thể gặp lỗi nhận diện mặt phẳng kém, giật lag.
- **Giải pháp**:
  - Kiểm tra danh sách thiết bị hỗ trợ ARCore trước khi demo.
  - Lựa chọn 1–2 thiết bị ổn định để trình diễn.
  - Thiết kế fallback tối giản (ví dụ: chế độ chỉ hiển thị mô hình 3D không AR nếu buộc phải dùng).

#### 1.2. Sai số khi đo kích thước phòng

- **Mô tả**: ARCore chỉ ước lượng, có thể có sai số (vài cm đến chục cm).
- **Giải pháp**:
  - Ghi chú rõ trong tài liệu: đây là **ước lượng**, không phải đo kiến trúc chính xác.
  - Dùng sai số trong khoảng chấp nhận được (ví dụ: gợi ý đồ chiếm tối đa 70% vùng trống).
  - Cho phép người dùng nhập/tinh chỉnh kích thước thủ công nếu muốn.

#### 1.3. Gọi API AI/LLM chậm hoặc lỗi

- **Mô tả**: Độ trễ phụ thuộc nhà cung cấp; có thể timeout, trả lỗi mạng.
- **Giải pháp**:
  - Thiết lập timeout hợp lý và xử lý retry ở backend.
  - Thiết kế UI hiển thị trạng thái “Đang suy nghĩ…” cho user.
  - Nếu AI/LLM lỗi, fallback về gợi ý cơ bản (không AI).

---

### 2. Rủi ro về phạm vi & thời gian (Scope & Timeline Risks)

#### 2.1. Quá tham về tính năng

- **Mô tả**: Muốn làm quá nhiều (đa nền tảng, nhiều loại phòng, nhiều loại đồ nội thất) dẫn đến trễ tiến độ.
- **Giải pháp**:
  - Bám sát roadmap (Phase 0–5).
  - Xác định rõ:
    - **Must-have**: scan phòng, gợi ý cơ bản, đặt 3D trong AR.
    - **Should-have**: gợi ý AI/LLM, phong cách.
    - **Nice-to-have**: share layout, e-commerce, nhiều phòng, v.v.

#### 2.2. Thiếu thời gian tích hợp end-to-end

- **Mô tả**: Tập trung quá nhiều vào một phía (AR hoặc AI) dẫn đến cuối kỳ không kịp nối pipeline hoàn chỉnh.
- **Giải pháp**:
  - Ưu tiên sớm một pipeline đơn giản nhưng chạy từ đầu đến cuối (end-to-end) rồi mới tối ưu.
  - Chia rõ mốc:
    - AR prototype xong trước Phase 2.
    - Backend & API cơ bản xong trước Phase 3.

---

### 3. Rủi ro về phụ thuộc bên thứ ba (Third-Party Dependencies)

#### 3.1. Thay đổi chính sách hoặc hạn chế API LLM

- **Mô tả**: Provider LLM thay đổi quota/giá, hoặc khoá tài khoản.
- **Giải pháp**:
  - Thiết kế layer tích hợp AI tách biệt, dễ chuyển provider.
  - Chuẩn bị sẵn plan demo dùng “mock data” nếu LLM không truy cập được.

#### 3.2. Không có mạng trong lúc demo

- **Mô tả**: Kết nối internet không ổn định/bị chặn khi bảo vệ.
- **Giải pháp**:
  - Chuẩn bị:
    - Video demo offline.
    - Chế độ demo offline với dữ liệu gợi ý được cache sẵn (cơ bản, không AI).

---

### 4. Rủi ro về trải nghiệm người dùng (UX Risks)

#### 4.1. Người dùng không quen dùng AR

- **Mô tả**: Một số người dùng chưa từng dùng AR, không biết phải di chuyển máy thế nào để “nhận mặt phẳng”.
- **Giải pháp**:
  - Onboarding rõ ràng với hình minh họa.
  - Tooltip hoặc text hướng dẫn trong màn AR: “Hãy di chuyển điện thoại chậm xung quanh phòng để nhận diện mặt phẳng”.

#### 4.2. Gợi ý không trúng ý người dùng

- **Mô tả**: Gợi ý có thể chưa “thông minh” như mong đợi, hoặc không đúng gu.
- **Giải pháp**:
  - Cho phép người dùng filter thêm (ví dụ: chỉ xem giường, chỉ sofa nhỏ).
  - Cho phép user đánh dấu “không thích” một gợi ý (ở version nâng cao).
  - Ghi chú rõ đây là prototype/PoC, mục tiêu chính là minh hoạ ý tưởng.

---

### 5. Tổng kết

- Rủi ro là không thể tránh khỏi, đặc biệt với dự án kết hợp nhiều công nghệ (AR + AI/LLM).
- Mục tiêu của tài liệu này là:
  - Cho thấy nhóm đã **nhận diện trước** các rủi ro lớn.
  - Đưa ra **giải pháp hợp lý** trong phạm vi đồ án (thời gian, nguồn lực có hạn).

