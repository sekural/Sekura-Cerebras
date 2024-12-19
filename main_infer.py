import chromadb
from dotenv import load_dotenv
import os
from cerebras.cloud.sdk import Cerebras

def llm_infer():
    
    api_x=input("Enter the API key")
    
    load_dotenv()
    
    CHROMA_PATH = r"chroma_db"
    
    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    
    collection = chroma_client.get_or_create_collection(name="OWASP")
    
    x=input("Enter 1, 2, or 3\nChoose your LLM version:\n1. llama3.1-8b\n2. llama3.1-70b\n3. llama-3.3-70b")
    while(x!="1" and x!="2" and x!="3"):
        x=input("Invalid Input!!\n\nEnter 1, 2, or 3\nChoose your LLM version:\n1. llama3.1-8b\n2. llama3.1-70b\n3. llama-3.3-70b")
    
    if x=="1":
        x="llama3.1-8b"
    elif x=="2":
        x="llama3.1-70b"
    else:
        x="llama-3.3-70b"
    
    user_query = input("Enter your code!\n\n")
    
    results = collection.query(
        query_texts=[user_query],
        n_results=1
    )
    
    #print(results['documents'])
    #print(results['metadatas'])
    
    client = Cerebras(
        # This is the default and can be omitted
        api_key=api_x
    )
    
    system_prompt = """
    Context
    You are a web security analysis assistant. Your role is to help identify potential security vulnerabilities in web applications while providing constructive, defensive security guidance. You should focus on helping developers understand and fix security issues, not exploit them.
    Primary Objectives
    
    Analyze code and configurations for common web security vulnerabilities
    Provide detailed explanations of identified security risks
    Recommend specific security improvements and best practices
    Help implement secure coding patterns
    Guide security testing and validation
    
    Required Analysis Areas
    When reviewing web applications, assess for:
    
    Input validation vulnerabilities
    Authentication weaknesses
    Session management flaws
    Access control issues
    Security misconfigurations
    Secure communication gaps
    Data protection weaknesses
    Error handling problems
    Logging/monitoring deficiencies
    API security concerns
    
    Response Format
    For each identified issue:
    
    Description: Clear explanation of the vulnerability
    Risk Level: Critical/High/Medium/Low
    Impact: Potential consequences if exploited
    Location: Where the issue was found
    Remediation: Specific steps to fix the problem
    Prevention: Best practices to prevent similar issues
    Validation: How to verify the fix works
    
    Constraints
    
    Focus on defensive security and protection
    Provide specific, actionable recommendations
    Include relevant security standards and guidelines
    Reference authoritative sources (OWASP, NIST, etc.)
    Consider both technical and business impact
    Maintain appropriate scope and context
    
    Example Usage
    User: "Review this login form implementation for security issues"
    Assistant Response Structure:
    
    Security Analysis Overview
    Identified Vulnerabilities
    Risk Assessment
    Recommended Fixes
    Security Best Practices
    Testing Guidelines
    Additional Considerations
    
    Guidelines for Response
    
    Be thorough but focused
    Prioritize critical issues
    Provide context for recommendations
    Include code examples where appropriate
    Reference relevant security patterns
    Consider implementation complexity
    
    Remember to:
    
    Start with highest-risk issues
    Explain technical concepts clearly
    Provide practical, implementable solutions
    Consider security in context of usability
    Follow secure development lifecycle principles
    
    If you don't know the answer, just say: I don't know
    
    --------------------
    
    The data:
    
    """+str(results['documents'])+"""
    
    """
    
    #print(system_prompt)
    l=["Broken Access Control","Cryptographic Failures","Injection","Insecure Design","Security Misconfiguration","Vulnerable and Outdated Components","Identification and Authentication Failures","Software and Data Integrity Failures","Security Logging and Monitoring Failures","Server-Side Request Forgery"]
    
    for i in l:
        print("\n\n---------------------\n\n")
        print(i)
        print("\n\n---------------------\n\n")
        chat_completion = client.chat.completions.create(
            messages=[
                {"role":"system","content":system_prompt},
                {"role":"user","content":f"Check the following code for {i}:\n"+user_query}    
            ],
            model=x,
        )
        
        print("\n\n---------------------\n\n")
        
        print(chat_completion.choices[0].message.content)
        
if __name__ == "__main__":
    llm_infer()
