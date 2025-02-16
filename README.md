# my-marketing-crew🤖

mymarketingcrew.ai is a multi-agent system designed to automate marketing campaign creation. Built as part of the Google Gen AI Exchange Hackathon, this app enables brands to generate targeted and effective marketing strategies with ease. Using advanced AI, this tool simplifies campaign planning, customer segmentation, and content strategy development. 🌟

## Crew Workflow
![Screenshot 2024-10-10 200615](https://github.com/user-attachments/assets/d5fbcf3b-c3d7-41f3-8df1-2d54d3a7ddfb)


## Features 🌟

- **Brand and Customer Analysis**: Analyze CRM data and brand documents to create personalized marketing plans.
- **Multi-Agent System**: Implements agents for different tasks such as brand analysis, strategy generation, and content creation.
- **Streamlined Workflow**: An intuitive interface built with Streamlit for easy interaction.
- **Integration with Groq**: Uses the `ChatGroq` API for enhanced natural language processing capabilities.


## Installation 🛠️

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/MyMarketingCrew.ai.git
   cd MyMarketingCrew.ai
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Run the application:
   ```bash
   poetry run streamlit run app.py
   ```

## Usage 🎯

1. **Set up your API key**:
   - Enter your Groq API key manually or use an environment variable.

2. **Provide Brand Details**:
   - Input brand name, industry, website (optional), description, and campaign goals.

3. **Upload Files**:
   - Add CRM data (CSV) for customer segmentation.
   - Upload a brand document (optional) to enhance analysis.

4. **Generate Strategy**:
   - Click **Generate Marketing Strategy** to let the multi-agent system create your campaign.

5. **Download Results**:
   - Download detailed reports, including:
     - Brand Analysis 🔍
     - Marketing Strategy 📈
     - Content Plan 📝

## Key Components 🔧

- **Agents**: Tasks are delegated to specialized agents created using the `crewai` framework.
- **Tasks**: Automates the workflow from analyzing brand data to developing a marketing strategy.
- **Streamlit Interface**: Simplifies interaction with a user-friendly design.

## Requirements 📋

- Python 3.11+
- Streamlit
- Poetry
- Groq API key (sign up at Groq)

## Contributing 🤝

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request. For major changes, please open an issue to discuss your proposal first.

## License 📜

This project is licensed under the MIT License.

## Acknowledgments 🙏

- **Google Gen AI Exchange Hackathon** for providing the opportunity.
- **crewai** for the multi-agent framework.
- **Groq** for the natural language processing API.
- Special thanks to the contributors and the open-source community!

## Contact 📬

Developed by **Ranveer Singh Ranawat**. For queries or collaborations, reach out at ranawatranveer0323@gmail.com
