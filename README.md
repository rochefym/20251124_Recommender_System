# API Documentation

## Base URL
Port-forwarded Django server running on RTX 5070 hardware:

https://jqh2g82b-8000.asse.devtunnels.ms


---

## 1. Generate Ingredients from Meal

**Endpoint**
POST /api/ollama/generate-ingredients-from-meal/


**Description**  
Generates a list of ingredients based on a natural language meal description.

**Sample Request**
```
{
  "meal_text": "Stir-fried chicken with broccoli and garlic sauce"
}
Sample Response

json
複製程式碼
{
  "ingredients": [
    "chicken breast",
    "broccoli",
    "garlic",
    "soy sauce",
    "cooking oil"
  ]
}
```

  
2. Ollama Prompt API
Endpoint

POST /api/ollama/prompt/
Description
Sends a prompt directly to the Ollama LLM and returns the generated response.

Sample Request

```
{
  "prompt": "Hi Ollama"
}
```

Sample Response

json
複製程式碼
{
  "response": "Hello! How can I help you today?"
}
3. RAG (Retrieval-Augmented Generation)
Endpoint

bash
複製程式碼
POST /api/rag/
Description
Generates personalized dietary or nutrition-related recommendations using user profile and meal data.

Sample Request

json
複製程式碼
{
  "sex": "male",
  "age": 78,
  "height_cm": 180,
  "weight_kg": 73.5,
  "activity_level": 1.12,
  "meal": {
    "meal_name": "Stir-fried potatoes with minced meat",
    "consumed_weight_g": 500.0
  }
}
Sample Response

json
複製程式碼
{
  "recommendation": "Reduce portion size and increase protein intake for muscle maintenance."
}
