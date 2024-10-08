import streamlit as st
import os
from crewai import Crew
from langchain_groq import ChatGroq
from agents import create_agents
from tasks import create_tasks


def initialize_api_keys():
    # Add API key input in sidebar
    st.sidebar.title("API Configuration")

    # Option to use environment variable or manual input
    api_key_option = st.sidebar.radio(
        "Choose API Key Source",
        ["Enter API Key", "Use Environment Variable"]
    )

    if api_key_option == "Enter API Key":
        groq_api_key = st.sidebar.text_input(
            "Enter your Groq API Key",
            type="password",
            help="Your API key will not be stored and is only used for this session"
        )
    else:
        groq_api_key = os.getenv("GROQ_API_KEY")

    if not groq_api_key:
        st.sidebar.error(
            "Groq API Key not found. Please enter a key or set it in your environment variables."
        )
        st.sidebar.markdown("""
        Don't have a Groq API key? 
        [Get one here](https://console.groq.com/keys) 
        
        Steps to get your key:
        1. Sign up for a Groq account
        2. Navigate to the API keys section
        3. Create a new key
        4. Copy and paste it here
        """)
        st.stop()

    return groq_api_key


def initialize_llm(groq_api_key):
    return ChatGroq(
        temperature=0.7,
        model_name="llama-3.2-90b-text-preview",
        groq_api_key=groq_api_key  # Pass the API key directly
    )


def main():
    st.set_page_config(
        page_title="My Marketing Crew",
        page_icon="🚀",
        layout="centered"
    )

    # logo
    st.image("logo.png", width=704)

    groq_api_key = initialize_api_keys()

    st.title("v0.0.2 by Ranveer Singh Ranawat☢")

    with st.form("brand_info_form"):
        brand_name = st.text_input("Brand Name")
        industry = st.text_input("Industry")
        website = st.text_input("Website (if applicable)")
        description = st.text_area("Brief description of the brand")

        # New campaign goal field
        campaign_goal = st.text_area("Campaign Goal",
                                     help="What do you want to achieve with this marketing campaign? (e.g., increase brand awareness, drive sales, launch a new product)")

        brand_document = st.file_uploader(
            "Upload brand document (optional)",
            type=["pdf", "docx", "txt"]
        )

        submitted = st.form_submit_button("Generate Marketing Strategy")

    if submitted:
        if not brand_name or not industry or not description or not campaign_goal:
            st.error(
                "Please fill in all required fields (Brand Name, Industry, Description, and Campaign Goal)."
            )
        else:
            document_path, temp_filename = handle_uploaded_file(brand_document)

            brand_info = {
                "brand_name": brand_name,
                "industry": industry,
                "website": website,
                "description": description,
                "campaign_goal": campaign_goal,
                "brand_document_path": document_path
            }

            try:
                with st.spinner("Generating marketing strategy. This may take a few minutes..."):
                    llm = initialize_llm(groq_api_key)
                    agents = create_agents(llm)
                    tasks = create_tasks(agents, brand_info)

                    marketing_crew = Crew(
                        agents=list(agents.values()),
                        tasks=tasks,
                        verbose=True
                    )

                    result = marketing_crew.kickoff()

                st.success("Marketing strategy generation complete!")
                display_results()

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
            finally:
                if temp_filename and os.path.exists(temp_filename):
                    os.remove(temp_filename)


def display_results():
    report_names = ["Brand Analysis", "Marketing Strategy", "Content Plan"]
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


if __name__ == "__main__":
    main()
