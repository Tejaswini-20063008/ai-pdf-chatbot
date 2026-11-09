import streamlit as st
import google.genai as genai
from pypdf import PdfReader

# Page layout configuration
st.set_page_config(page_title="AI PDF Chatbot", page_icon="📚", layout="centered")

st.title("📚 AI Document Study Assistant")
st.write("Upload a PDF textbook, research paper, or notes, and ask questions directly to the document!")

# Sidebar for configuration
st.sidebar.header("Settings")
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password", help="Get a free key from Google AI Studio")

# Session state to store document context and chat history
if "context" not in st.session_state:
    st.session_state.context = ""
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# File uploader widget
uploaded_file = st.file_uploader("Upload your Study Material (PDF)", type=["pdf"])

# Extract text when a new file is uploaded
if uploaded_file:
    with st.spinner("Processing PDF and extracting text..."):
        try:
            reader = PdfReader(uploaded_file)
            extracted_text = ""
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    extracted_text += text
            
            st.session_state.context = extracted_text
            st.sidebar.success(f"Successfully loaded {len(reader.pages)} pages!")
        except Exception as e:
            st.sidebar.error(f"Error reading PDF: {e}")

# Chat interface
st.divider()
st.subheader("Chat Window")

# Display previous messages in the chat
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User question input box
if user_query := st.chat_input("Ask something about the uploaded document..."):
    # Append user question to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.write(user_query)

    # Validate inputs before calling AI
    if not api_key:
        with st.chat_message("assistant"):
            st.error("Please enter your Gemini API Key in the sidebar to proceed.")
    elif not st.session_state.context:
        with st.chat_message("assistant"):
            st.error("Please upload a valid PDF document first.")
    else:
        # Generate response using Gemini
        with st.chat_message("assistant"):
            with st.spinner("Searching document..."):
                try:
                    # Construct strict prompt
                    prompt = f"""
                    You are an expert academic tutor. Answer the user's question based strictly on the provided context extracted from a document.
                    If the answer cannot be found in the context, politely state: "I couldn't find the answer in the provided document."

                    Context:
                    {st.session_state.context}

                    Question:
                    {user_query}
                    """

                    # Call API
                    client = genai.Client(api_key=api_key)
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt,
                    )
                    
                    # Display and save response
                    assistant_response = response.text
                    st.write(assistant_response)
                    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
                    
                except Exception as e:
                    st.error(f"API Error: {e}")