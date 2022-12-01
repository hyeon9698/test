import streamlit as st

def main():
    st.sidebar.title("Electron")
    st.sidebar.info("The Electron Slide...")
    st.sidebar.slider('How "nativive"?', 0, 100, 50)
    st.title("Streamlit in `Electron`")
    st.write("github test")
    st.write("2022.12.01 12:11:30 version.")

if __name__ == "__main__":
    main()