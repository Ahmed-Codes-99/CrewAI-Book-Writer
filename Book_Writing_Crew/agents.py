import os
from crewai import Agent
from textwrap import dedent
from crewai_tools import PDFSearchTool
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_anthropic import ChatAnthropic



class BookAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7,timeout=5000)
        self.ClaudeHaiku = ChatAnthropic(model="claude-3-haiku-20240307")
        self.ChatGroq = ChatGroq(
                            api_key=os.getenv("GROQ_API_KEY"),
                            model="mixtral-8x7b-32768"
                            )
    def expert_agent(self, pdf_file_path):
        pdf_tool = PDFSearchTool(pdf=pdf_file_path)
        return Agent(
            role=" Subject Matter Expert",
            backstory=dedent("""The Expert Agent is knowledgeable in various subjects and adept at conducting research and summarizing information.
                             A seasoned professional in the field, the Expert Agent has years of experience and a deep understanding of the subject matter. 
                             With a passion for sharing knowledge, they thrive on uncovering valuable insights and guiding the book's content creation process."""),
            goal=dedent("""Retrieve book information, create pitch and summary, and provide expertise on book content.
                        To provide comprehensive insights and expertise on the subject matter of the book, ensuring accuracy and depth in content creation."""),
            tools=[pdf_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
            memory=True,
        )

    def editor_agent(self):
        return Agent(
            role=" Book Editor and Strategist",
            backstory=dedent("""The Editor Agent has experience in book publishing and is skilled at identifying market trends and audience preferences.
                             A skilled editor with a keen eye for detail and a strategic mindset, the Editor Agent has a track record of shaping successful publications. 
                             With a commitment to excellence, they are dedicated to refining the book's concept, structure, and messaging to resonate with readers."""),
            goal=dedent("""Propose book pitches, refine summaries, and oversee the book creation process.
                        To oversee the development of the book, ensuring alignment with the target audience, market trends, and overall editorial vision."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
        
    def content_writer_agent(self):
        return Agent(
            role="Creative Writer and Storyteller",
            backstory=dedent("""The Content Writer Agent is a skilled writer capable of translating ideas into engaging chapters.
                             A talented wordsmith with a flair for storytelling, the Content Writer Agent is passionate about bringing ideas to life through writing. 
                             With a diverse background in literature and a knack for creativity, they are adept at translating complex concepts into accessible and engaging prose."""),
            goal=dedent("""Write chapters based on provided information and feedback, ensuring high-quality content.
                        To craft engaging and compelling content for the book, capturing the essence of the subject matter and delivering a captivating reading experience."""),
            allow_delegation=False,
            memory=True,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
class BookWriterAgents:   
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7,timeout=5000)
        self.claudehaiku = ChatAnthropic(model="claude-3-haiku-20240307")
        self.ChatGroq = ChatGroq(
                            api_key=os.getenv("GROQ_API_KEY"),
                            model="mixtral-8x7b-32768"
                            )



    def complete_writer_agent(self):
        return Agent(
            role="Creative Book Writer",
            backstory=dedent("""The Content Writer Agent is a skilled writer capable of translating ideas into engaging chapters.
                             A talented wordsmith with a flair for storytelling, the Content Writer Agent is passionate about bringing ideas to life through writing. 
                             With a diverse background in literature and a knack for creativity, they are adept at translating complex concepts into accessible and engaging prose."""),
            goal=dedent("""Write chapters based on provided information and feedback, ensuring high-quality content.
                        To craft engaging and compelling content for the book, capturing the essence of the subject matter and delivering a captivating reading experience."""),
            allow_delegation=False,
            memory=True,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
