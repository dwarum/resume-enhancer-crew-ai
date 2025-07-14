#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
from resume_enhancer_ai.crew import ResumeEnhancerAi
from pypdf import PdfReader
import gradio as gr

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators

def load_resume():
    """
    Load the resume from a PDF file.
    """
    try:
        reader = PdfReader("input/linkedin.pdf")
        return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    except Exception as e:
        raise Exception(f"An error occurred while loading the resume: {e}")


def run():
    """
    Run the crew.
    """
    resume = load_resume()
    inputs = {
        'resume': resume
    }
    
    try:
        result = ResumeEnhancerAi().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "topic": "AI LLMs",
#         'current_year': str(datetime.now().year)
#     }
#     try:
#         ResumeEnhancerAi().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")

# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         ResumeEnhancerAi().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "AI LLMs",
#         "current_year": str(datetime.now().year)
#     }
    
#     try:
#         ResumeEnhancerAi().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")

# iface = gr.Interface(
#     fn=run,
#     inputs=[],
#     outputs="text",
#     title="Resume Enhancer AI",
#     description="Enhance your resume with AI tools and techniques.",
#     theme="default")

# if __name__ == "__main__":
#     iface.launch()