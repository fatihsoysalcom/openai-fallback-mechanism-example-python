import os
import time

# Simulate an API key, though not strictly used for this dummy call
# PRIMARY_API_KEY = os.getenv("OPENAI_API_KEY", "sk-YOUR_OPENAI_KEY")

def call_openai_api(prompt: str, simulate_failure: bool = False) -> str:
    """
    Simulates a call to the OpenAI API.
    Can be configured to simulate a failure, mimicking issues like billing problems.
    """
    print(f"\nAttempting to call primary OpenAI API for prompt: '{prompt}'...")
    time.sleep(1) # Simulate network latency

    if simulate_failure:
        # Simulate a common API error, e.g., network issue, billing problem, rate limit
        print("--- Primary API call FAILED! Simulating an error (e.g., billing issue, network). ---")
        raise ConnectionError("Failed to connect to OpenAI API or billing issue.")
    
    # Simulate a successful response
    response = f"Primary API response for '{prompt}': This is a detailed AI-generated text from OpenAI."
    print("Primary API call SUCCESSFUL.")
    return response

def fallback_mechanism(prompt: str) -> str:
    """
    Provides a fallback response when the primary API fails.
    This could be a simpler model, a cached response, or a default message.
    """
    print(f"\n--- Activating fallback mechanism for prompt: '{prompt}' ---")
    time.sleep(0.5) # Simulate quicker local processing

    # Example fallback: a simpler, rule-based response or a cached answer
    if "hello" in prompt.lower():
        return "Fallback: Hello there! How can I assist you in a basic way?"
    elif "weather" in prompt.lower():
        return "Fallback: I cannot fetch live weather, but it's generally good to check a local weather app."
    else:
        return f"Fallback: I received your request for '{prompt}'. Due to an issue with the primary service, I can only provide a general or predefined response."

def main():
    user_prompt = "Tell me about the importance of fallback mechanisms."

    # --- Scenario 1: Simulate Primary API Failure ---
    print("\n" + "="*60)
    print("--- Running Scenario 1: Primary API Failure (demonstrates fallback) ---")
    print("="*60)
    final_response_scenario1 = ""
    try:
        # Attempt to call the primary service
        # This flag is set to True to force a failure and demonstrate the fallback
        final_response_scenario1 = call_openai_api(user_prompt, simulate_failure=True) # ILLUSTRATES ARTICLE'S CONCEPT: SIMULATED FAILURE
    except Exception as e:
        print(f"Error caught: {e}. Initiating fallback mechanism.")
        # If primary service fails, activate the fallback
        final_response_scenario1 = fallback_mechanism(user_prompt) # ILLUSTRATES ARTICLE'S CONCEPT: FALLBACK ACTIVATION
    
    print(f"\n[Scenario 1] Final Response: {final_response_scenario1}")
    print("\n" + "="*60)

    # --- Scenario 2: Simulate Primary API Success ---
    print("\n" + "="*60)
    print("--- Running Scenario 2: Primary API Success (no fallback needed) ---")
    print("="*60)
    user_prompt_success = "What is the capital of France?"
    final_response_scenario2 = ""
    try:
        # Attempt to call the primary service
        # This flag is set to False to allow a successful primary call
        final_response_scenario2 = call_openai_api(user_prompt_success, simulate_failure=False)
    except Exception as e:
        print(f"Error caught: {e}. Initiating fallback mechanism.")
        final_response_scenario2 = fallback_mechanism(user_prompt_success)
    
    print(f"\n[Scenario 2] Final Response: {final_response_scenario2}")
    print("\n" + "="*60)

if __name__ == "__main__":
    main()
