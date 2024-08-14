import os
import sys
from crewai import Crew, Agent, Task
from textwrap import dedent
from dotenv import load_dotenv
from crewai_tools import PDFSearchTool
from langchain_openai import ChatOpenAI
from agents import BookAgents
from agents import BookWriterAgents
from tasks import BookTasks
from tasks import ChapterTasks
load_dotenv()

class BookCrew1:
    def __init__(self):
        self.agents = BookAgents()
        self.tasks = BookTasks()

    def run(self):
        pdf_file_path = input("Please enter the path to the PDF file: ")
        expert_agent = self.agents.expert_agent(pdf_file_path)  # Pass PDF file path to expert agent
        editor_agent = self.agents.editor_agent()
        content_writer_agent = self.agents.content_writer_agent()

        pitch_task = self.tasks.pitch_creation(expert_agent)
        pitch_selection_task = self.tasks.pitch_selection(editor_agent)
        summary_development_task = self.tasks.summary_development(editor_agent)
        detailed_summary_chapter_outline_task = self.tasks.detailed_summary_chapter_outline(editor_agent)
        chapter_writing_task = self.tasks.chapter_writing(content_writer_agent)

        crew = Crew(
            agents=[expert_agent, editor_agent, content_writer_agent],
            tasks=[pitch_task, pitch_selection_task, summary_development_task, detailed_summary_chapter_outline_task, chapter_writing_task],
            verbose=True
        )

        result = crew.kickoff()
        return result
class BookCrew2:
    def __init__(self,user_input,test_result):
       
        self.agents = BookWriterAgents()
        self.tasks = ChapterTasks()
        self.user_input = user_input 
        self.book_summary = test_result
    def run(self):
        complete_writer_agent = self.agents.complete_writer_agent()

        chapter_1_task = self.tasks.chapter_1(complete_writer_agent,self.user_input,self.book_summary)
        chapter_2_task = self.tasks.chapter_2(complete_writer_agent,self.user_input,self.book_summary)
        chapter_3_task = self.tasks.chapter_3(complete_writer_agent,self.user_input,self.book_summary)
        chapter_4_task = self.tasks.chapter_4(complete_writer_agent,self.user_input,self.book_summary)
        chapter_5_task = self.tasks.chapter_5(complete_writer_agent,self.user_input,self.book_summary)
        chapter_6_task = self.tasks.chapter_6(complete_writer_agent,self.user_input,self.book_summary)
        chapter_7_task = self.tasks.chapter_7(complete_writer_agent,self.user_input,self.book_summary)

        crew = Crew(
            agents=[complete_writer_agent],
            tasks=[chapter_1_task,chapter_2_task,chapter_3_task,chapter_4_task,chapter_5_task,chapter_6_task,chapter_7_task],
            verbose=True
        )

        result = crew.kickoff()
        return result    

def main():

    print("## Welcome to Book Creation Crew!")
    print("--------------------------------")

    book_crew = BookCrew1()
    crew1_result = book_crew.run()

    print("\n\n########################")
    print("## Here is your Book Summary from Crew1:")
    print("########################\n")
    print(crew1_result)
    
    with open("book_summary.txt", "a") as file:
            file.write("\n\n########################\n")
            file.write("## Crew1 Result:\n")
            file.write("########################\n")
            file.write(crew1_result)

  
    print("\n\n########################")
    print(" -------------------------")
    print("########################\n")
    
    user_input = input("Please provide your feedback for book writing agents:")

    with open('complete_book.txt', 'w') as f:
        sys.stdout = f
        chapter_writer_crew = BookCrew2()
        result = chapter_writer_crew.run()
        print("\n\n########################")
        print("## Here is your Book crew run result:")
        print("########################\n")
        print(result)
        sys.stdout = sys.__stdout__

if __name__ == "__main__":
    main()