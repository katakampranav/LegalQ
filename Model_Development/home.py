import streamlit as st

# Function to render the Home page
def render_page():
    # Custom Styles for UI
    st.markdown(
        """
        <style>
        body {
            background-color: #F9F9F9;
            color: #2E3A59;
            font-family: 'Arial', sans-serif;
        }
        .header {
            text-align: center;
            font-size: 50px; /* Increased font size for the title */
            margin-bottom: 20px; /* Added more space below the title */
            color: #3B5998;
        }
        .header2 {
            text-align: center;
            font-size: 20px; /* Increased font size for the title */
            margin-bottom: 20px; /* Added more space below the title */
            color: #555;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Create two columns with balanced widths
    col1, col2, col3 = st.columns([0.1, 1, 2])  # Adjust the ratios for better balance

    with col1:
        st.markdown("")  # Empty column for spacing

    # Add the image to the first column with padding
    with col2:
        st.image("assets/emblem_of_india.png", use_container_width=False, width=350)  # Adjust width as necessary

    # Add the title and description to the third column
    with col3:
        st.markdown("<h1 class='header'>LegalQ</h1>", unsafe_allow_html=True)
        st.markdown("<h3 class='header'>A Legal Offense Query System</h3>", unsafe_allow_html=True)
        st.markdown(
            """
            <h5 class='header2'>
            <br><br>
            Welcome to the <strong>LegalQ A Legal Offense Query System</strong>, your go-to platform for exploring legal offenses, 
            understanding their relevant sections, and receiving personalized legal insights. Our platform is designed 
            to simplify the complex legal landscape, providing you with accurate, concise, and easy-to-understand information.
            <br><br>
            Whether you are a legal professional, a student, or simply a curious individual, this system empowers you to
            navigate the intricacies of the legal framework with confidence and clarity. Gain insights into legal terminology, 
            discover detailed explanations of offenses, and access resources tailored to your queries.
            </h5> 
            """,
            unsafe_allow_html=True,
        )