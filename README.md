# Resume Enhancer AI

An intelligent resume enhancement system powered by CrewAI that automatically checks your resume for ATS (Applicant Tracking System) compatibility and enhances it to maximize your chances of landing interviews.

## 🚀 Features

- **ATS Compatibility Checker**: Analyzes your resume and provides a simulated ATS score
- **Intelligent Enhancement**: Two-stage resume enhancement process for optimal results
- **Iterative Improvement**: Automatically refines your resume until it meets ATS standards
- **Multi-LLM Support**: Uses different AI models for specialized tasks
- **PDF Processing**: Handles PDF resume uploads seamlessly

## 🎯 How It Works

The system uses a multi-agent approach with three specialized AI agents:

### 1. ATS Checker Agent
- **Role**: Evaluates resume for ATS compatibility
- **Goal**: Provides detailed ATS scoring and feedback
- **Output**: Comprehensive report with section-wise and overall ATS scores
- **Threshold**: Aims for 98+ ATS compatibility score

### 2. Initial Resume Enhancer Agent
- **Role**: Implements ATS feedback to improve the resume
- **Goal**: Transforms the resume based on actionable feedback
- **Focus**: Balances ATS optimization with human readability

### 3. Final Resume Enhancer Agent
- **Role**: Fine-tunes the enhanced resume for maximum impact
- **Goal**: Creates a compelling, recruiter-friendly document
- **Output**: Polished, professional resume ready for submission

## 🔄 Process Flow

```
1. Load Resume (PDF) → 2. ATS Check → 3. Score ≥ 85? 
                                          ↓ No
4. Initial Enhancement → 5. Final Enhancement → 6. Repeat (Max 3 iterations)
```

## 📋 Prerequisites

- Python 3.10+ <3.14
- OpenAI API key
- Groq API key
- Required Python packages (see requirements below)

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/resume-enhancer-ai.git
cd resume-enhancer-ai
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

4. **Create required directories**
```bash
mkdir -p input output config
```

## 📁 Project Structure

```
resume-enhancer-ai/
├── config/
│   ├── agents.yaml          # Agent configurations
│   ├── tasks_ats.yaml       # ATS checking tasks
│   └── tasks_enhancer.yaml  # Enhancement tasks
├── input/
│   └── resume.pdf          # Your resume (place here)
├── output/
│   ├── ats_score_report.md  # ATS analysis report
│   └── enhanced_resume_final.pdf  # Final enhanced resume
├── resume_enhancer_ai/
│   └── crew.py             # CrewAI crew definitions
├── main.py                 # Main execution script
├── .env                    # Environment variables
└── requirements.txt        # Python dependencies
```

## 🚀 Usage

1. **Place your resume**
   - Save your resume as `input/resume.pdf`

2. **Run the enhancer**
```bash
python main.py
```

3. **Check results**
   - View ATS report: `output/ats_score_report.md`
   - Get enhanced resume: `output/enhanced_resume_final.pdf`

## 📊 Configuration

### Customizing Agents

Edit `config/agents.yaml` to modify agent behaviors:

```yaml
ats_checker:
  role: >
    check the {resume} for ATS compatibility
  goal: >
    Ensure that the {resume} meets ATS standards
  backstory: >
    You are an expert in ATS systems...
  llm: openai/gpt-4o-mini
```

### Adjusting Tasks

Modify `config/tasks_ats.yaml` and `config/tasks_enhancer.yaml` for custom task configurations.

### Parameters

Adjust these constants in `main.py`:
- `MAX_ITERATIONS = 3`: Maximum enhancement iterations
- `ATS_THRESHOLD = 98`: Minimum required ATS score

## 🤖 AI Models Used

- **OpenAI GPT-4o-mini**: ATS checking and final enhancement
- **Groq Llama-3.3-70b**: Initial resume enhancement

## 📈 Output Examples

### ATS Score Report
```markdown
# ATS Compatibility Report

## Overall ATS Score: 85/100 (Simulated)

### Section Scores:
- Contact Information: 95/100
- Professional Summary: 80/100
- Work Experience: 85/100
- Skills: 75/100

### Recommendations:
- Add more industry-specific keywords
- Improve formatting consistency
- Optimize section headers
```

### Enhanced Resume Features
- Optimized keyword density
- ATS-friendly formatting
- Enhanced bullet points
- Improved section structure
- Quantified achievements

## 🔧 Troubleshooting

### Common Issues

1. **PDF Reading Errors**
   - Ensure PDF is not password-protected
   - Check if PDF contains extractable text
   - Try re-saving PDF from a different source

2. **API Rate Limits**
   - Add delays between API calls if needed
   - Check your API quotas

3. **ATS Score Not Found**
   - The system expects specific score format in output
   - Check agent prompts if scores aren't being generated

### Error Messages

- `Resume content seems empty`: PDF might be image-based or corrupted
- `ATS score not found`: Agent didn't output score in expected format
- `API key not found`: Check your `.env` file configuration

## 📝 Requirements.txt

```txt
crewai==0.70.1
python-dotenv==1.0.0
pypdf==4.0.1
gradio==4.44.0
openai>=1.0.0
groq>=0.4.0
```
---

**Made with ❤️ and AI**