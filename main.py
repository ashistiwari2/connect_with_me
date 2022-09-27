import streamlit as st
from PIL import Image
im = Image.open("favicon1.ico")
PAGE_TITLE = "Connect with Ashis Tiwari"
st.set_page_config(page_title=PAGE_TITLE, page_icon=im)

st.header(":mailbox: Get In Touch With Me!")


contact_form = """
<form action="https://formsubmit.co/ashistiwari2@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
