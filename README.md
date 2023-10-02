# Reseach-Agent-using-Metaphor

Mini research agent using OpenAI Function Call and Metaphor APIs (https://metaphor.systems/)

Frontend is built with Chainlit. Demo is available [here](https://www.youtube.com/watch?v=1V1AStPO_5Y). 

## Funcitonalities

1. Chitchat: The agent can have normal conversation.
2. Search Papers: The agent can search research papers related to the requested topic.
3. Get Detailed Content: The agent can give you more detailed content of a paper you
requested.
4. Find Similar Papers: The agent can find some similar papers to the requested paper.
5. Propose Ideas: The agent can propose promising research directions based on the
information in the conversation.

## 🚀 Getting Started

To run a demo, follow these steps:

1. Clone this repository:
   ```
   git clone https://github.com/JungDongwon/Research-Agent-using-Metaphor.git
   ```
2. Navigate to the desired demo folder:
   ```
   cd Research-Agent-using-Metaphor
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create a `.env` file based on the provided `.env.example` file:
   ```
   cp .env.example .env
   ```
   Modify the `.env` file as needed to include any necessary API keys or configuration settings.
5. Run the Chainlit app in watch mode:
   ```
   chainlit run app.py -w
   ```

Your demo chatbot UI should now be up and running in your browser!
