def resume_app():
    import streamlit as st
    import base64
    
    def displayPDF(file):
        # Opening file from file path
        with open(file, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        # Embedding PDF in HTML
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="925" type="application/pdf"></iframe>'
        # Displaying File
        st.markdown(pdf_display, unsafe_allow_html=True)

    st.subheader('I am a Python programmer and I am excited to share my portfolio with you.👨‍💻')

    st.markdown('<style>body{background-color: #DCDCDC;}</style>', unsafe_allow_html=True)
    
    st.markdown('<style>body{background-color: white;}</style>', unsafe_allow_html=True)

    displayPDF("assets/resume_app/William Aponte Resume.pdf")