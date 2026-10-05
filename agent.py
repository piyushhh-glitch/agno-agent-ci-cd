from agno.agent import Agent
from agno.team import Team
from agno.models.google import GeminiInteractions
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

def create_team():

    researcher=Agent(
        name="Researcher",
        role="Research the given topic and provide useful information",
        model=GeminiInteractions(id="gemini-2.5-flash-lite")
    )


    analyst=Agent(
        name="Analyst",
        role="Analyze the research and identify important insights",
        model=GeminiInteractions(id="gemini-2.5-flash-lite")
    )

    writer=Agent(
        name="Writer",
        role="Create a clear and well structured Answer",
        model=GeminiInteractions(id="gemini-2.5-flash-lite")
    )

    team=Team(
        name="AI Research Team",
        model=Groq(id="openai/gpt-oss-120b"),
        members=[researcher,analyst,writer],
        instructions=[
            "First ask the Researcher to research the topic.",
            "Then ask the Analyst to analyze the research.",
            "Finally ask the Writer to create the final answer."
        ]
    )

    return team


if __name__=="__main__":
    team=create_team()

    team.print_response(
        "Explain the current applications of Generative AI in healthcare.",
        stream=True
    )