import streamlit as st
from langchain.llms import OpenAI
from langchain_community.callbacks import get_openai_callback

st.title("🔗Hệ thống tạo ngân hàng câu hỏi các môn học Học viện Ngân Hàng")

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(input_text):
    llm = OpenAI(model="gpt-3.5-turbo-instruct",max_tokens=2000, temperature=0.7, openai_api_key=openai_api_key)
    result = llm(input_text)

    with st.expander("Kết quả chi tiết:", expanded=True):
        st.text_area("Kết quả", result, height=400)  # Điều chỉnh chiều cao theo nhu cầu
        print(result)
        with get_openai_callback() as cb:
            result = llm.invoke(input_text)
            st.info(cb)

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
question_types = ["Trắc nghiệm (4 đáp án)", "Bài tập", "Đúng/Sai"]
selected_question_type = st.radio("Chọn loại câu hỏi:", question_types)

# Nhập PROMPT tạo câu hỏi
text_input = st.text_area(label="Nhập nội dung tạo câu hỏi")

# Nút Submit
button = st.button("Submit", key="button")
if button:
    # Ghép nối các thông tin từ các lựa chọn để tạo prompt hoàn chỉnh
    prompt = (
        f"Là một giảng viên Học viện Ngân hàng, hãy soạn một số câu hỏi với yêu cầu chi tiết như sau: \n"
        f"Môn học: {selected_subject},\n"
        f"Độ khó: {selected_difficulty},\n"
        f"Số lượng câu hỏi: {number_of_questions},\n"
        f"Loại câu hỏi: {selected_question_type},\n"
        f"Nội dung: {text_input}"
    )
    st.markdown(prompt)
    st.subheader("Kết quả:")
    if not openai_api_key.startswith('sk-'):
        st.warning('Vui lòng nhập OpenAI API key!', icon='⚠')
    if openai_api_key.startswith('sk-'):
        generate_response(prompt)
