from crewai import Task
from textwrap import dedent

class BookTasks:
    def pitch_creation(self, agent):
        return Task(
            description = "Generate a concise pitch and summary outlining the book's content, writing style, target audience, and structure.The book must only consist of 7 chapters.",
            expected_output = "Short pitch, summary, writing style description, target audience, book structure.The book must only consist of 7 chapters.",
            agent=agent,
            human_input=True,
        )

    def pitch_selection(self, agent):
        return Task(
            description = "Propose multiple book pitches based on the expert's summary, highlighting potential best-selling attributes.The book must only consist of 7 chapters.",
            expected_output = "Multiple pitches for consideration.The book must only consist of 7 chapters.",
            agent=agent,
            human_input=True,
        )
    
    def summary_development(self, agent):
        return Task(
            description = "Develop a unique and detailed summary of the book, incorporating feedback and refining it to accurately represent the content.The book must only consist of 7 chapters.",
            expected_output = "Detailed summary with feedback incorporated.The book must only consist of 7 chapters.",
            agent=agent,
            human_input=True,
        )

    def detailed_summary_chapter_outline(self, agent):
        return Task(
            description = "Provide a comprehensive summary with chapter outlines, ensuring coherence and alignment with the book's objectives.The book must only consist of 7 chapters.",
            expected_output = "Detailed summary with chapter outlines.The book must only consist of 7 chapters.",
            agent=agent,
            human_input=True,
        )

    def chapter_writing(self, agent):
        return Task(
            description = "Write chapters based on the outlined structure, conducting research and incorporating feedback to deliver polished content.Each chapter must contain 1000 to 2500 words.The book must only consist of 7 chapters.",
            expected_output = """ Title: <title>
                                  Chapter 1: <1000-2500 words>
                                  Chapter 2: <1000-2500 words>
                                  Chapter 3: <1000-2500 words>
                                  Chapter 4: <1000-2500 words>
                                  Chapter 5: <1000-2500 words>
                                  Chapter 6: <1000-2500 words>
                                  Chapter 7: <1000-2500 words>.""",
            agent=agent,
            human_input=True,
        )
class ChapterTasks:
    def chapter_1(self, agent,user_input,book_summary):
        return Task(
            description = f"Write the chapter 1 only of the book summary:{book_summary}, please consider this:{user_input}.",
            expected_output = """Write Chapter 1 only, it must contain more than 500 words.""",
            agent=agent,
            human_input=True,
        )
    def chapter_2(self, agent,user_input,book_summary):
        return Task(
            description = f"Write the chapter 2 only of the book summary:{book_summary}, please consider this:{user_input}.",
            expected_output = """Write Chapter 2 only, it must contain more than 500 words.""",
            agent=agent,
            human_input=True,
        )
    def chapter_3(self, agent,user_input,book_summary):
        return Task(
            description = f"Write the chapter 3 only of the book summary:{book_summary}, please consider this:{user_input}.",
            expected_output = """Write Chapter 3 only, it must contain more than 500 words.""",
            agent=agent,
            human_input=True,
        ) 
    def chapter_4(self, agent,user_input,book_summary):
        return Task(
            description = f"Write the chapter 4 only of the book summary:{book_summary}, please consider this:{user_input}.",
            expected_output = """Write Chapter 4 only, it must contain more than 500 words.""",
            agent=agent,
            human_input=True,
        )
    def chapter_5(self, agent,user_input,book_summary):
        return Task(
            description = f"Write the chapter 5 only of the book summary:{book_summary}, please consider this:{user_input}.",
            expected_output = """Write Chapter 5 only, it must contain more than 500 words.""",
            agent=agent,
            human_input=True,
        )
    def chapter_6(self, agent,user_input,book_summary):
        return Task(
            description = f"Write the chapter 6 only of the book summary:{book_summary}, please consider this:{user_input}.",
            expected_output = """Write Chapter 6 only, it must contain more than 500 words.""",
            agent=agent,
            human_input=True,
        )
    def chapter_7(self, agent,user_input,book_summary):
        return Task(
            description = f"Write the chapter 7 only of the book summary:{book_summary}, please consider this:{user_input}.",
            expected_output = """Write Chapter 7 only, it must contain more than 500 words.""",
            agent=agent,
            human_input=True,
        )