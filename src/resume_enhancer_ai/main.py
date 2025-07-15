#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
from resume_enhancer_ai.crew import ATSCheckCrew, ResumeEnhancerCrew
from pypdf import PdfReader
import gradio as gr
import re

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators

MAX_ITERATIONS = 3  # to prevent infinite loop
ATS_THRESHOLD = 85  # minimum ATS score for compatibility
def load_resume():
    """
    Load the resume from a PDF file.
    """
    try:
        reader = PdfReader("input/linkedin.pdf")
        return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    except Exception as e:
        raise Exception(f"An error occurred while loading the resume: {e}")

def extract_score(text:str) -> float:
    match = re.search(r"(?i)ats score[:\s]*([0-9]{1,3})", text)
    if match:
        return float(match.group(1))
    raise ValueError("ATS score not foung in the output")


def run():
    """
    Run the crew.
    """
    resume_text = load_resume()
    inputs = {
        'resume': resume_text
    }
    
    # first run ATS check crew. if it fails, only then run the resume enhancer crew
    print(f"Running ATS Checker...")
    for i in range(MAX_ITERATIONS):
        try:
            ats_result = ATSCheckCrew().crew().kickoff(inputs=inputs)
            print(f"ATS Check Result: {ats_result}")

            ats_score = extract_score(str(ats_result))
            print(f"ATS Score: {ats_score}")
            
            if ats_score is not None and ats_score >= ATS_THRESHOLD:
                print(f"Resume is ATS compatible with a score of {ats_score}.")
                return{
                    "final_iteration": i + 1,
                    "final_ats_score": ats_score,
                    "final_ats_result": ats_result,
                    "enhancement_performed": i > 0
                }
        except Exception as e:
            ats_score = None
            ats_result = None
            raise Exception(f"An error occurred while running the ATS Check crew: {e}")
        
        # ATS score is less that threshold. run the resume enhancer crew
        print(f"Running Resume Enhancer Crew...")
        try:
            resume_enhancer_result = ResumeEnhancerCrew().crew().kickoff(inputs=inputs)
            inputs['resume'] = resume_enhancer_result  # update the resume with the enhanced version
            
            print(f"Max iterations reached. ATS score is still below threshold.")
            
            return {
                "final_iteration": MAX_ITERATIONS,
                "final_ats_score": ats_score,
                "final_ats_result": ats_result,
                "enhancement_performed": True,
                "enhanced_resume": inputs['resume']
            }
        except Exception as e:
            raise Exception(f"An error occurred while running the Resume Enhancer crew: {e}")

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