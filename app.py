import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_ai_product_recommendation(user_preferences):
    """
    Generates a personalized product recommendation based on user interests
    using the OpenAI GPT model.
    """
    prompt = f"The user is looking for a product with these preferences: {user_preferences}. Suggest 3 ideal products with brief reasons why."
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful e-commerce shopping assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    sample_preference = "Comfortable running shoes under $100 for marathon training"
    print("Fetching AI Recommendations...")
    print(get_ai_product_recommendation(sample_preference))
