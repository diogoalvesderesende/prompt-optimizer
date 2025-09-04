# 🚀 AI Prompt Optimizer

A powerful Streamlit web application that helps you create better prompts for AI models like GPT-5, Claude, Gemini, and others. Get instant feedback and improved versions of your prompts!

## ✨ Features

- **AI Model Agnostic**: Works with GPT-5, Claude, Gemini, and other modern AI models
- **Instant Analysis**: Get detailed feedback on your prompts in seconds
- **Improved Versions**: Receive optimized prompts that work better with AI models
- **User-Friendly Interface**: Clean, intuitive web interface built with Streamlit
- **Local & Cloud Ready**: Run locally for testing or deploy to Streamlit Cloud
- **CLI Support**: Also works as a command-line tool

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/diogoalvesderesende/prompt-optimizer.git
   cd prompt-optimizer
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up your API key**
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your-openai-api-key-here
   ```

## 🚀 Usage

### Web Application (Recommended)
```bash
streamlit run app.py
```
The app will open at `http://localhost:8501`

### Command Line Interface
```bash
python app.py
```

## 📋 Requirements

- Python 3.8+
- OpenAI API key
- Internet connection

## 📦 Dependencies

- `openai==1.101.0`
- `streamlit==1.49.1`
- `python-dotenv==1.0.0`

## 🎯 How It Works

1. **Enter your prompt** in the text area
2. **Click "Analyze & Improve"** to get instant feedback
3. **Review the analysis** including:
   - What's good and what could be better
   - Specific problems to fix
   - An improved version of your prompt
   - What changes were made
   - Tips for next time

## 🌟 Tips for Better Prompts

- **Be Clear and Specific**: Tell the AI exactly what you want
- **Match Complexity to Task**: Simple tasks = brief prompts, complex tasks = detailed prompts
- **Control the Output**: Specify format, detail level, and explanation depth
- **Provide Context**: Give enough background information and examples
- **Set Boundaries**: Define what to include and exclude

## 🔧 Configuration

### Local Development
- API key is loaded from `.env` file
- App runs on `http://localhost:8501`

### Streamlit Cloud Deployment
- API key is stored in Streamlit secrets
- Automatically detects deployment environment

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Support

- **Feedback**: [Share your thoughts](https://6yoersztgja.typeform.com/to/Cgxtnpq1)
- **Support**: [Buy me a coffee](https://buymeacoffee.com/diogoalvesx)

## 📞 Contact

- **Author**: Diogo Resende
- **GitHub**: [@diogoalvesderesende](https://github.com/diogoalvesderesende)

---

Made with ❤️ by Diogo Resende
