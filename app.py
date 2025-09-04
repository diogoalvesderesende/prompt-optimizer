import streamlit as st
import openai
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_api_key():
    """Get API key from environment or Streamlit secrets"""
    # First try environment variable (for local development)
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        return api_key
    
    # Then try Streamlit secrets (for deployment)
    try:
        if hasattr(st, 'secrets') and st.secrets.get("OPENAI_API_KEY"):
            return st.secrets.get("OPENAI_API_KEY")
    except:
        pass
    
    return None

def critique_and_improve_prompt(user_prompt, client):
    """Use OpenAI responses endpoint to critique and improve the prompt for any AI model"""
    
    system_prompt = """You are a helpful assistant that improves prompts for AI models like GPT-5, Claude, Gemini, and others. 
    
    Your job is to:
    1. Look at the user's prompt and see what could be better
    2. Point out any problems or unclear parts
    3. Give them a better version that works well with modern AI models
    
    **What makes modern AI models special:**
    - They're really good at following instructions exactly
    - They can handle complex tasks step by step
    - They're great at coding and problem-solving
    - They can be adjusted to be more or less detailed
    - They understand context better than older models
    
    **What to look for when improving prompts:**
    
    **Clear Instructions:**
    - Remove confusing or contradictory instructions
    - Make sure the prompt is specific and clear
    - Add backup plans for when things are unclear
    - Fix any conflicting instructions
    
    **Task Complexity:**
    - Match the detail level to how complex the task is
    - For simple tasks, keep it brief
    - For complex tasks, be more thorough
    - Set clear limits on how much work to do
    
    **Output Control:**
    - Specify how detailed the answer should be
    - Control how much the AI should explain its thinking
    - Make sure the format is what you want
    - Set the right level of detail for your needs
    
    **Context and Examples:**
    - Provide enough background information
    - Give examples when helpful
    - Set clear boundaries for what to include
    - Balance being thorough with being efficient
    
    Please give your response in this format:
    
    ## What I Found
    [Simple explanation of what's good and what could be better about their prompt]
    
    ## Problems to Fix
    - [Problem 1: explain in simple terms]
    - [Problem 2: explain in simple terms]
    - [Problem 3: explain in simple terms]
    
    ## Better Version
    [Your improved prompt written in clear, simple language]
    
    ## What I Changed
    - [Change 1: simple explanation]
    - [Change 2: simple explanation]
    - [Change 3: simple explanation]
    
    ## Tips for Next Time
    - [Simple tip 1]
    - [Simple tip 2]
    - [Simple tip 3]"""
    
    try:
        response = client.responses.create(
            model="gpt-5-nano",
            input=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Please analyze and improve this prompt:\n\n{user_prompt}"}
            ],
            text={
                "format": {
                    "type": "text"
                },
                "verbosity": "low"
            },
            reasoning={
                "effort": "low",
                "summary": None
            },
            store=False,
        )
        
        return response.output_text
        
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """Main function that works for both CLI and Streamlit"""
    
    # Get API key
    api_key = get_api_key()
    
    if not api_key:
        if 'streamlit' in sys.modules:
            st.error("❌ OpenAI API key not found! Please set it in your .env file or Streamlit secrets.")
            st.info("Create a .env file with: OPENAI_API_KEY=your-key-here")
            st.stop()
        else:
            print("❌ OpenAI API key not found! Please set it in your .env file.")
            print("Create a .env file with: OPENAI_API_KEY=your-key-here")
            sys.exit(1)
    
    # Initialize OpenAI client
    client = openai.OpenAI(api_key=api_key)
    
    # Check if running in Streamlit
    if 'streamlit' in sys.modules:
        is_streamlit = True
    else:
        is_streamlit = False
    
    if is_streamlit:
        # Streamlit UI
        st.set_page_config(
            page_title="AI Prompt Optimizer",
            page_icon="🚀",
            layout="wide"
        )
        
        st.title("🚀 AI Prompt Helper")
        st.markdown("Make your AI prompts clearer and more effective! Works with GPT-5, Claude, Gemini, and other AI models. Enter a prompt and click 'Analyze & Improve' to see results here!")
        
        # Collapsible tips section
        with st.expander("💡 Click to see tips for better prompts", expanded=False):
            st.markdown("""
            **Simple Tips for Better Prompts:**
            
            **🎯 Be Clear and Specific:**
            - Tell the AI exactly what you want
            - Avoid confusing or contradictory instructions
            - Give clear examples when possible
            - Set boundaries for what to include
            - Give enough background information
            
            **📝 Match Complexity to Task:**
            - Simple tasks = brief prompts
            - Complex tasks = more detailed prompts
            - Set clear limits on how much work to do
            - Don't overcomplicate simple requests
            
            **💡 Control the Output:**
            - Specify how detailed you want the answer
            - Ask for the format you prefer (list, paragraph, etc.)
            - Tell the AI how much to explain its thinking            
            
            """)
        
        # Sidebar for configuration
        with st.sidebar:

            st.header("📝 Feedback")
            st.markdown("Help me improve this tool with your suggestions.")
            st.markdown(f"""
            <a href="https://6yoersztgja.typeform.com/to/Cgxtnpq1" target="_blank" style="text-decoration: none;">
                <button style="width: 100%; background-color: #0074FF; color: white; border: none; border-radius: 8px; padding: 0.5rem 1rem; font-size: 14px; font-weight: 500; cursor: pointer; transition: all 0.3s ease; display: flex; align-items: center; justify-content: center; gap: 8px;">
                    📝 Share your thoughts
                </button>
            </a>
            """, unsafe_allow_html=True)

            st.markdown("---")
            
            st.header("☕ Support")
            st.markdown("If you find this tool helpful, consider supporting its maintenance.")
            st.markdown(f"""
            <a href="https://buymeacoffee.com/diogoalvesx" target="_blank" style="text-decoration: none;">
                <button style="width: 100%; background-color: #FF6B6B; color: white; border: none; border-radius: 8px; padding: 0.5rem 1rem; font-size: 14px; font-weight: 500; cursor: pointer; transition: all 0.3s ease; display: flex; align-items: center; justify-content: center; gap: 8px;">
                    ☕ Buy me a coffee
                </button>
            </a>
            """, unsafe_allow_html=True)
         

        
        # Main content
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.header("📝 Input Prompt")
            user_prompt = st.text_area(
                "Enter your prompt here:",
                height=300,
                placeholder="Paste your prompt here and I'll help make it better..."
            )
            
            if st.button("🚀 Analyze & Improve", type="primary", use_container_width=True):
                if user_prompt.strip():
                    with st.spinner("Analyzing your prompt..."):
                        result = critique_and_improve_prompt(user_prompt, client)
                        
                    with col2:
                        st.header("🎯 Analysis & Improvement")
                        st.markdown(result)
                else:
                    st.error("Please enter a prompt to analyze!")
        
        
        # Footer
        st.markdown("---")
        st.markdown("*Powered by Diogo Resende*")
        
    else:
        # CLI Interface
        print("🚀 AI Prompt Optimizer (Command Line Version)")
        print("=" * 50)
        
        while True:
            print("\n📝 Enter your prompt (or 'quit' to exit):")
            user_prompt = input("> ")
            
            if user_prompt.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
                
            if user_prompt.strip():
                print("\n🔄 Analyzing your prompt...")
                result = critique_and_improve_prompt(user_prompt, client)
                print("\n🎯 Analysis & Improvement:")
                print("=" * 50)
                print(result)
                print("=" * 50)
            else:
                print("❌ Please enter a prompt!")

if __name__ == "__main__":
    main()
