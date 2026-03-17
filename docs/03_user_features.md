## 03 – Tính năng người dùng & luồng sử dụng (User Features & Flows)

### 1. Nhóm tính năng chính

#### 1.1. Quét phòng & đo không gian (Room Scanning & Measurement)

- Mở camera AR và quét xung quanh phòng.
- Nhận diện mặt phẳng sàn (floor plane) bằng ARCore.
- Cho phép người dùng:
  - Chạm để đánh dấu các điểm trên sàn.
  - Tự động tính toán khoảng cách giữa các điểm (chiều dài, chiều rộng).
- Hiển thị kích thước vùng trống ước lượng (ví dụ: 1.6m × 2.1m).

#### 1.2. Nhập ngữ cảnh & sở thích (Context & Preference Input)

- Chọn loại phòng:
  - Phòng ngủ, phòng khách, phòng trọ, phòng học, v.v.
- Chọn phong cách nội thất:
  - Minimalist (tối giản), Modern (hiện đại), Classic (cổ điển), v.v.
- (Mở rộng) Nhập thêm yêu cầu:
  - Mô tả bằng text (VD: “mình muốn góc học tập gọn gàng, có kệ sách nhỏ”).

#### 1.3. Nhận gợi ý nội thất (Furniture Recommendations)

- Gửi thông tin phòng + ngữ cảnh lên Backend.
- Nhận về:
  - Danh sách các món đồ nội thất phù hợp (tên, hình ảnh, kích thước).
  - Lý do gợi ý (đặc biệt với chế độ AI/LLM).
- Hiển thị kết quả dạng:
  - List hoặc carousel có thể scroll ngang.
  - Mỗi item có nút “Xem chi tiết” và “Đặt vào AR”.

#### 1.4. Mô phỏng nội thất 3D trong AR (AR Visualization)

- Khi người dùng chọn một món đồ:
  - Tải mô hình 3D tương ứng (từ local hoặc từ URL).
  - Đặt nội thất lên mặt phẳng sàn đã nhận diện.
- Tương tác AR:
  - Chạm để chọn item.
  - Kéo để di chuyển quanh phòng.
  - Gesture xoay để thay đổi hướng.
- Đảm bảo scale 1:1:
  - Nếu bàn cao 75cm, hiển thị trong AR cũng 75cm so với mặt phẳng.

#### 1.5. Trải nghiệm hướng dẫn & hỗ trợ (Onboarding & Help)

- Màn hình hướng dẫn lần đầu sử dụng:
  - Cách quét phòng hiệu quả.
  - Cách đánh dấu điểm đo kích thước.
  - Cách đặt và chỉnh sửa mô hình 3D.
- Tooltip ngắn xuất hiện trong app ở các bước quan trọng.

---

### 2. User Flow chi tiết

#### 2.1. Flow 1 – Lần đầu mở ứng dụng

1. User mở app DecoAR / RoomFit.
2. App hiển thị màn hình giới thiệu ngắn:
   - Vấn đề → Giải pháp → Lợi ích.
3. App yêu cầu quyền truy cập camera.
4. App hiển thị hướng dẫn scan phòng đơn giản.

#### 2.2. Flow 2 – Scan phòng & đo kích thước

1. User bật chế độ AR camera.
2. App yêu cầu user:
   - Di chuyển điện thoại quanh phòng để ARCore nhận diện mặt phẳng.
3. Khi mặt phẳng sàn được nhận diện:
   - App hiển thị các “plane” bán trong suốt.
4. User chạm lên sàn để đánh dấu các điểm:
   - Điểm A, B (hoặc A–B–C nếu đo khu vực phức tạp hơn).
5. App tính toán và hiển thị:
   - Khoảng cách AB (hoặc kích thước vùng), lưu lại làm thông tin phòng.

#### 2.3. Flow 3 – Nhập ngữ cảnh & gọi gợi ý

1. Sau khi đã có kích thước cơ bản:
   - App chuyển sang màn hình “Thiết lập ngữ cảnh”.
2. User:
   - Chọn loại phòng (dropdown hoặc button).
   - Chọn phong cách (chip button).
   - (Tuỳ chọn) nhập ghi chú text.
3. User nhấn nút “Nhận gợi ý”.
4. App gửi request đến Backend:
   - `{ width_m, length_m, room_type, style, notes }`.

#### 2.4. Flow 4 – Nhận và xem danh sách gợi ý

1. Backend xử lý và trả về danh sách gợi ý.
2. App hiển thị:
   - Card cho từng món: tên, ảnh, kích thước, loại, style.
   - Lý do gợi ý (nếu có từ AI).
3. User có thể:
   - Scroll qua các gợi ý.
   - Chọn một item để xem chi tiết.

#### 2.5. Flow 5 – Đặt đồ nội thất vào AR

1. Trong màn chi tiết item, user nhấn “Đặt vào AR”.
2. App quay lại chế độ camera AR:
   - Nếu mặt phẳng đã nhận diện, hiển thị ghost preview (preview mờ).
3. User chạm để “thả” mô hình 3D xuống sàn.
4. User có thể:
   - Kéo để di chuyển vị trí.
   - Xoay bằng 2 ngón tay.
   - Chọn lại một món khác từ danh sách gợi ý để thay thế.

---

### 3. Các kịch bản sử dụng (Use Cases) chính

- **UC1 – Ướm thử giường trong phòng ngủ nhỏ**
  - Người dùng scan phòng ngủ, đo khoảng trống 2m × 2.5m.
  - Chọn loại phòng “Bedroom”, phong cách “Minimalist”.
  - Nhận gợi ý giường đơn/giường queen + tủ đầu giường nhỏ.
  - Ướm thử từng loại giường để xem còn đủ lối đi hay không.

- **UC2 – Setup góc làm việc trong phòng trọ**
  - Người dùng muốn có bàn làm việc + ghế + kệ sách nhỏ.
  - Scan góc phòng gần cửa sổ, đo kích thước.
  - Nhập yêu cầu text: “Muốn bàn làm việc nhỏ gọn, có chỗ để laptop và sách”.
  - Hệ thống gợi ý combo bàn 1m2 + ghế xoay + kệ sách treo tường.
  - User đặt thử bàn + ghế trong AR để xem có chắn lối đi hay không.

- **UC3 – Ướm thử sofa trong phòng khách**
  - Người dùng scan khu vực phòng khách trống dọc theo tường.
  - Chọn phòng khách, phong cách hiện đại.
  - Nhận gợi ý sofa 2 chỗ hoặc 3 chỗ + bàn trà nhỏ.
  - Đặt mẫu sofa khác nhau để so sánh kích thước và bố cục.

---

### 4. Ưu tiên tính năng (Feature Prioritization)

- **Must-have (giai đoạn đầu)**:
  - Scan phòng, nhận diện mặt phẳng, đo kích thước cơ bản.
  - Gợi ý dựa trên kích thước (không cần AI).
  - Đặt mô hình 3D nội thất cơ bản trong AR.

- **Should-have (khi có thời gian)**:
  - Gợi ý thông minh bằng AI/LLM (lý do chi tiết).
  - Lọc theo phong cách, loại phòng.

- **Nice-to-have (giai đoạn sau)**:
  - Lưu layout nhiều phiên bản cho cùng một phòng.
  - Chia sẻ layout cho bạn bè hoặc gửi link.
  - Tích hợp link mua hàng trực tiếp đến các shop nội thất.

