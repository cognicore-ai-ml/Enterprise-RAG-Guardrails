# src/guardrails.py

def check_input_safety(user_input):
    """
    Basic filtering logic. In a production app, you would integrate 
    NeMo Guardrails or a library like 'presidio' here.
    """
    forbidden_keywords = ["sql injection", "hack", "ignore instructions"]
    
    for word in forbidden_keywords:
        if word in user_input.lower():
            return False, "Security violation: Unauthorized input detected."
    
    return True, "Safe"

def check_output_safety(llm_response):
    """
    Check if the LLM leaked any PII or prohibited information.
    """
    # Logic to detect PII (e.g., regex for emails, phone numbers)
    if "private_key" in llm_response:
        return False, "Security violation: Potential PII leakage."
        
    return True, "Safe"
  
