import streamlit as st
import os
from crewai import Crew
from langchain_groq import ChatGroq
from agents import create_agents
from tasks import create_tasks


def initialize_api_keys():
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    if not GROQ_API_KEY:
        st.sidebar.error(
            "GROQ API Key not found. Please set it in your environment variables.")
        st.stop()
    return GROQ_API_KEY


def initialize_llm(groq_api_key):
    return ChatGroq(temperature=0.7, model_name="llama-3.2-90b-text-preview")


def handle_uploaded_file(uploaded_file):
    if uploaded_file is None:
        return None, None

    file_extension = os.path.splitext(uploaded_file.name)[1]
    temp_filename = f"temp_brand_document{file_extension}"

    content = uploaded_file.read()

    with open(temp_filename, "wb") as f:
        f.write(content)

    abs_path = os.path.abspath(temp_filename)

    return abs_path, temp_filename


def run_marketing_crew(brand_info):
    groq_api_key = initialize_api_keys()
    llm = initialize_llm(groq_api_key)

    agents = create_agents(llm)
    tasks = create_tasks(agents, brand_info)

    marketing_crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        verbose=True
    )

    result = marketing_crew.kickoff()
    return result


def main():
    st.set_page_config(page_title="My Marketing Crew",
                       page_icon="🚀", layout="centered")
    st.image("logo.png", width=704)
    st.title("v0.0.1🚀")

    with st.form("brand_info_form"):
        brand_name = st.text_input("Brand Name")
        industry = st.text_input("Industry")
        website = st.text_input("Website (if applicable)")
        description = st.text_area("Brief description of the brand")
        brand_document = st.file_uploader(
            "Upload brand document (optional)", type=["pdf", "docx", "txt"])

        submitted = st.form_submit_button("Generate Marketing Strategy")

    if submitted:
        if not brand_name or not industry or not description:
            st.error(
                "Please fill in all required fields (Brand Name, Industry, and Description).")
        else:
            document_path, temp_filename = handle_uploaded_file(brand_document)

            brand_info = {
                "brand_name": brand_name,
                "industry": industry,
                "website": website,
                "description": description,
                "brand_document_path": document_path
            }

            try:
                with st.spinner("Generating marketing strategy. This may take a few minutes..."):
                    result = run_marketing_crew(brand_info)
                st.success("Marketing strategy generation complete!")

                report_names = ["Brand Analysis",
                                "Marketing Strategy", "Content Plan"]

                tabs = st.tabs(report_names)

                report_files = {
                    "Brand Analysis": "brand_and_customer_analysis.md",
                    "Marketing Strategy": "marketing_strategy.md",
                    "Content Plan": "content_and_campaign_plan.md"
                }

                for tab, (tab_name, file_name) in zip(tabs, report_files.items()):
                    with tab:
                        if os.path.exists(file_name):
                            with open(file_name, "r") as file:
                                content = file.read()
                            st.download_button(
                                label=f"Download {tab_name}",
                                data=content,
                                file_name=file_name,
                                mime="text/markdown"
                            )
                            st.markdown(content)
                        else:
                            st.warning(f"{tab_name} report was not generated.")

                st.balloons()

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
            finally:
                if temp_filename and os.path.exists(temp_filename):
                    os.remove(temp_filename)


if __name__ == "__main__":
    main()
