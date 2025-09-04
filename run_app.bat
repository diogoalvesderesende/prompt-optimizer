@echo off
echo 🚀 Starting GPT-5 Prompt Helper...
echo.

REM Activate virtual environment
echo 📦 Activating virtual environment...
call venv\Scripts\activate.bat

REM Run Streamlit app
echo 🌐 Starting Streamlit app...
echo.
echo 📍 The app will open at: http://localhost:8503
echo.
echo ⚠️  Make sure you have your OPENAI_API_KEY in the .env file!
echo.

streamlit run app.py --server.port 8503 --server.address 127.0.0.1

pause
