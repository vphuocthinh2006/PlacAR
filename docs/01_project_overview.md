## 01 – Tổng quan dự án (Project Overview)

### 1. Tên dự án

- **Tên**: DecoAR / RoomFit  
- **Mô tả ngắn**: Ứng dụng hỗ trợ người dùng thiết kế và mô phỏng nội thất bằng công nghệ AR và AI/LLM, giúp “ướm thử” đồ nội thất 3D tỷ lệ 1:1 ngay trong phòng thật trước khi mua.

---

### 2. Vấn đề & Động lực (Problem Statement & Motivation)

**Vấn đề chính**:
- Người dùng khó hình dung kích thước thật của đồ nội thất khi mua online hoặc tại showroom.
- Không dễ đánh giá mức độ phù hợp của một món đồ với không gian thực tế (diện tích, lối đi, ánh sáng, màu sắc).
- Quá trình đo đạc thủ công bằng thước dây, giấy bút vừa tốn thời gian vừa dễ sai số.

**Hệ quả**:
- Mua đồ về mới phát hiện quá to, quá nhỏ, hoặc lệch phong cách.
- Tốn chi phí đổi trả, lãng phí thời gian và gây khó chịu cho người dùng.

**Động lực**:
- Tận dụng công nghệ **AR (Augmented Reality)** và **AI/LLM** để:
  - Giảm rủi ro trong việc chọn mua nội thất.
  - Giúp người dùng ra quyết định trực quan, tự tin hơn.
  - Tạo trải nghiệm “thiết kế nội thất mini” ngay trên điện thoại cá nhân.

---

### 3. Mục tiêu & Phạm vi (Goals & Scope)

**Mục tiêu chính**:
- Xây dựng một hệ thống có khả năng:
  1. **Hiểu không gian phòng** thông qua camera và AR.
  2. **Gợi ý đồ nội thất** phù hợp với kích thước phòng và ngữ cảnh sử dụng.
  3. **Mô phỏng đồ nội thất 3D** trong phòng thật với tỷ lệ chính xác.

**Phạm vi đồ án**:
- Tập trung vào:
  - Nền tảng **Android** sử dụng **ARCore**.
  - Một số loại phòng phổ biến: phòng ngủ, phòng khách (có thể thêm phòng trọ).
  - Bộ catalog nội thất mẫu (10–30 món) được mô tả kỹ (kích thước, phong cách, model 3D).
  - Gợi ý nội thất ở 2 cấp độ:
    - Gợi ý **logic cơ bản** dựa trên kích thước phòng.
    - Gợi ý **thông minh** kết hợp AI/LLM và phong cách.
- Không tập trung vào:
  - Xây dựng sàn thương mại điện tử hoàn chỉnh.
  - Triển khai đa nền tảng (iOS, Web) trong giai đoạn đầu.
  - Tối ưu hóa hiệu năng cho dữ liệu rất lớn.

---

### 4. Đối tượng người dùng (Target Users)

- **Người dùng phổ thông**:
  - Sinh viên, người đi làm muốn tự sắp xếp lại phòng trọ/phòng ngủ.
  - Gia đình muốn thử bố trí lại phòng khách/phòng ngủ trước khi mua nội thất mới.

- **Nhà bán lẻ nội thất (trong tương lai)**:
  - Tích hợp hệ thống vào app/web của họ để khách hàng “ướm thử” sản phẩm trước.

---

### 5. Giá trị mang lại (Value Proposition)

- **Cho người dùng cuối**:
  - Nhìn thấy trước cách đồ nội thất “thật” xuất hiện trong phòng của họ.
  - Hạn chế mua nhầm kích thước, tiết kiệm thời gian và chi phí.
  - Trải nghiệm thiết kế nội thất một cách trực quan, thú vị.

- **Cho đồ án / nghiên cứu**:
  - Trình diễn khả năng kết hợp AR + AI/LLM trong một bài toán thực tế.
  - Minh họa kiến trúc hệ thống đa tầng: Mobile AR, Backend API, AI/LLM, Database.
  - Làm nền tảng cho việc mở rộng thành sản phẩm hoàn chỉnh trong tương lai.

---

### 6. Mục tiêu kỹ thuật (Technical Objectives)

- Thiết kế được **kiến trúc hệ thống rõ ràng**, phân tách Mobile – Backend – AI/LLM – DB.
- Triển khai:
  - Prototype AR: quét phòng, nhận diện mặt phẳng, đặt mô hình 3D.
  - Backend Python (FastAPI): cung cấp API gợi ý nội thất.
  - Tích hợp thử nghiệm AI/LLM: cải thiện chất lượng gợi ý.
- Đảm bảo:
  - Tài liệu đầy đủ (tech stack, kiến trúc, roadmap, API, rủi ro, hướng phát triển).
  - Demo mượt, thể hiện được trải nghiệm người dùng cuối.

