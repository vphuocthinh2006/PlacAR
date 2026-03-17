## 10 – Định hướng mở rộng (Expansion Direction)

Tài liệu này mô tả các hướng phát triển tiếp theo nếu dự án DecoAR / RoomFit được đầu tư dài hạn.

---

### 1. Mở rộng tính năng cho người dùng cuối

#### 1.1. Lưu & quản lý layout phòng

- Cho phép người dùng:
  - Lưu nhiều cấu hình bố trí nội thất (layout) cho cùng một phòng.
  - Đặt tên layout (VD: “Phòng ngủ mùa hè”, “Setup góc làm việc mùa thi”).
  - So sánh nhanh các layout khác nhau.

#### 1.2. Hỗ trợ nhiều phòng & nhiều địa điểm

- Quản lý danh sách phòng:
  - Phòng ngủ 1, phòng ngủ 2, phòng khách, phòng làm việc, studio, v.v.
- Mỗi phòng có:
  - Kích thước, ảnh, layout hiện tại, layout dự kiến.

#### 1.3. Chia sẻ & cộng tác

- Chia sẻ layout:
  - Gửi link/QR để bạn bè hoặc người thân xem layout phòng.
  - Tải ảnh chụp màn hình hoặc video ngắn của bố trí AR.
- Cộng tác:
  - Nhiều người cùng chỉnh sửa layout cho một phòng (phiên bản nâng cao).

---

### 2. Tích hợp e-commerce & đối tác nội thất

#### 2.1. Tích hợp với nhà bán lẻ

- Liên kết từng món đồ nội thất trong app với:
  - Trang sản phẩm thực trên website của hãng.
  - Thông tin giá, tình trạng còn hàng, màu sắc.

#### 2.2. Gợi ý theo ngân sách (budget)

- Cho phép người dùng nhập:
  - Ngân sách tổng.
  - Ngân sách cho từng khu vực (VD: “budget cho phòng ngủ là 15 triệu”).
- Hệ thống gợi ý combo nội thất phù hợp ngân sách + gu thẩm mỹ.

---

### 3. Cải thiện AI/LLM & đề xuất thông minh

#### 3.1. Học từ hành vi người dùng

- Lưu:
  - Những món đồ thường được chọn hoặc bỏ qua.
  - Các layout được lưu lại nhiều.
- Sử dụng dữ liệu này để:
  - Tinh chỉnh prompt.
  - Điều chỉnh logic filter và xếp hạng.

#### 3.2. Phân tích phong cách sâu hơn

- Phân tích:
  - Màu tường, màu sàn từ camera.
  - Vật dụng hiện có trong phòng.
- Gợi ý:
  - Đồ nội thất phù hợp với bảng màu (color palette) hiện tại.
  - Gợi ý thêm đồ trang trí nhỏ (đèn, tranh, cây cảnh).

---

### 4. Kiến trúc & hạ tầng

#### 4.1. Scale backend & database

- Đưa backend lên cloud:
  - GCP, AWS hoặc Azure.
- Sử dụng:
  - Managed DB (Cloud SQL, RDS, v.v.).
  - Caching (Redis) cho dữ liệu catalog ít thay đổi.

#### 4.2. Microservices & tách chức năng

- Tách hệ thống thành các service:
  - Catalog Service (quản lý dữ liệu nội thất).
  - Recommendation Service (gợi ý logic).
  - AI Service (tương tác với LLM).
  - Layout Service (quản lý bố trí phòng).

---

### 5. Đa nền tảng

#### 5.1. Hỗ trợ iOS (ARKit)

- Xây dựng phiên bản iOS:
  - Dùng ARKit để thay thế ARCore.
  - Giữ chung backend và API.

#### 5.2. Web & WebAR (giới hạn)

- Phiên bản web:
  - Cho phép người dùng xem layout 3D (không AR) trong trình duyệt.
  - Thao tác kéo/thả đồ nội thất trên sơ đồ 2D/3D.
- WebAR (nếu hạ tầng & thiết bị cho phép):
  - Dùng WebXR để hiển thị một số trải nghiệm AR cơ bản trên mobile browser.

---

### 6. Hướng nghiên cứu nâng cao

- **Tự động nhận diện cấu trúc phòng**:
  - Phát hiện cửa, cửa sổ, cầu thang.
  - Đề xuất bố trí nội thất không che khuất lối đi/nguồn sáng.

- **Sinh layout tự động**:
  - Dùng AI/ML để sinh layout tối ưu về:
    - Lối đi.
    - Ánh sáng tự nhiên.
    - Khoảng cách giữa các đồ nội thất.

- **Tối ưu cá nhân hóa**:
  - Mỗi user có “profile” phong cách riêng.
  - Hệ thống học dần để gợi ý ngày càng “đúng gu”.

