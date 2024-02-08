import PyPDF2
import re
import streamlit as st

def pdf_to_txt(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text() if page.extract_text() else ''
    # テキストの前処理（改行と空白の削除）
    text = re.sub(r'\n+', '\n', text)  # 連続する改行を1つに置換
    text = re.sub(r'\s+', ' ', text)  # 連続する空白を1つに置換
    return text

# Streamlit UI
st.title('PDF to Text Converter')
uploaded_file = st.file_uploader('PDFファイルを選択してください', type='pdf')
if uploaded_file is not None:
    text_data = pdf_to_txt(uploaded_file)
    st.text_area('変換されたテキスト', text_data, height=300)
    st.download_button(label='テキストをダウンロード', data=text_data, file_name='converted_text.txt', mime='text/plain')
