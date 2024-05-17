import streamlit as st
import openai 

# API key của bạn
api_key = "sk-proj-DPu19QT1ZLHMcCzGc3fNT3BlbkFJeb6YFU7HbK8s0nFuprEu"

# Cấu hình API key cho OpenAI
openai.api_key = api_key

st.title("🔗Hệ thống tạo ngân hàng câu hỏi các môn học Học viện Ngân Hàng")

# Lựa chọn môn học
subjects = [
    "Tài chính doanh nghiệp I",
    "Thiết kế Web",
    "Lịch sử Đảng",
    "Trí tuệ nhân tạo",
    "Mạng và truyền thông"
]
selected_subject = st.selectbox("Chọn môn học:", subjects)

# Chọn mức độ khó
difficulty_levels = ["Dễ", "Trung bình", "Khó"]
selected_difficulty = st.radio("Chọn mức độ khó:", difficulty_levels)

# Chọn số lượng câu hỏi
number_of_questions = st.number_input("Nhập số lượng câu hỏi:", min_value=1, max_value=100, step=1, value=10)

# Chọn loại câu hỏi
question_types = ["Trắc nghiệm", "Bài tập", "Đúng/Sai"]
selected_question_type = st.radio("Chọn loại câu hỏi:", question_types)

# Nhập PROMPT tạo câu hỏi
text_input = st.text_area(label="Nhập nội dung tạo câu hỏi")

# Nút Submit
button = st.button("Submit", key="button")

if button:
    # Ghép nối các thông tin từ các lựa chọn để tạo prompt hoàn chỉnh
    prompt = (
        f"Môn học: {selected_subject}\n"
        f"Độ khó: {selected_difficulty}\n"
        f"Số lượng câu hỏi: {number_of_questions}\n"
        f"Loại câu hỏi: {selected_question_type}\n"
        f"Nội dung: {text_input}"
    )
    
    # Gửi prompt tới OpenAI API
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=prompt,
            temperature=0.7,
            max_tokens=150
        )

        result = response.choices[0].text.strip()
        st.subheader("Nội dung:")
        st.markdown(prompt)
        st.subheader("Kết quả:")
        st.write(result)
    except openai.OpenAIError as e:
        st.error(f"Lỗi khi gọi API OpenAI: {e}")
