import streamlit as st
import pandas as pd
from utils.clean_data import clean_dataset
from utils.analysis import get_dataset_summary
from utils.charts import plot_chart
from utils.ai_agent import ask_ai
from utils.pdf_report import generate_pdf
# Store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


st.set_page_config(page_title="AI Data Analyst Agent", page_icon="📊")

st.title("📊 AI Data Analyst Agent")

uploaded_file = st.file_uploader(
    "Upload a CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    # Read File
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("✅ File Uploaded Successfully!")

    # Show Dataset
    st.subheader("Dataset Preview")
    st.dataframe(df)
    
    df = clean_dataset(df)

    st.subheader("🧹 Cleaned Dataset")
    st.dataframe(df)

    summary = get_dataset_summary(df)

    st.subheader("📊 Dataset Summary")
 
    col1, col2 = st.columns(2)

    with col1:
     st.metric("Total Rows", summary["Total Rows"])
     st.metric("Missing Values", summary["Missing Values"])

    with col2:
     st.metric("Total Columns", summary["Total Columns"])
     st.metric("Duplicate Rows", summary["Duplicate Rows"])
    # Number of Rows and Columns
     st.subheader("Dataset Information")

    rows, columns = df.shape

    st.write(f"**Number of Rows:** {rows}")
    st.write(f"**Number of Columns:** {columns}")

    # Column Names
    st.subheader("Column Names")

    st.write(df.columns.tolist())

    # Data Types
    st.subheader("Data Types")

    st.write(df.dtypes)

    # Missing Values
    st.subheader("Missing Values")

    st.write(df.isnull().sum())

    # Duplicate Rows
    st.subheader("Duplicate Rows")

    st.write(df.duplicated().sum())

    st.subheader("📊 Data Visualization")

    plot_chart(df)

    st.subheader("🤖 AI Data Analyst")

question = st.text_input("Ask a question about your data")

if st.button("Ask AI"):

    if question:
      answer = ask_ai(question, df)

    if answer is None:
       st.error("No response received from the AI.")
    elif "Answer:" in answer:
       answer = answer.split("Answer:")[-1].strip()

    if answer:
      st.success(answer)
    st.session_state.chat_history.append({
        "question": question,
        "answer": answer
    })
       
else:
    st.warning("Please enter a question.")

st.subheader("📜 Question History")

selected_questions = []

for i, chat in enumerate(st.session_state.chat_history):

    selected = st.checkbox(
        chat["question"],
        key=f"question_{i}"
    )

    if selected:
        selected_questions.append(chat)

    st.write("**Answer:**")
    st.write(chat["answer"])

    st.divider()
   
    if selected:
            selected_questions.append(chat)
     
if selected_questions:     
    
    pdf_file = generate_pdf(summary, selected_questions)

    with open(pdf_file, "rb") as file:
      st.download_button(
        label="📄 Download PDF Report",
        data=file,
        file_name="AI_Report.pdf",
        mime="application/pdf"
    )
    