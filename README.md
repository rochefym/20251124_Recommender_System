# API Documentation

## Food Intake Backend - Base URL  
- https://h3vkhzth-8000.asse.devtunnels.ms/api/patients/1
    
1. GET patients/{int}/
2. GET patients/{int}/recommended_intake
3. GET meals/{int}/


  
## Recommender - Base URL
Port-forwarded Django server running on RTX 5070 hardware:  
- https://jqh2g82b-8000.asse.devtunnels.ms
1. POST /api/ollama/generate-ingredients-from-meal/
2. POST /api/rag/query
3. POST /api/ollama/chat/prompt/  
  
  
---

## 1. Generate Ingredients from Meal

### Endpoint
POST /api/ollama/generate-ingredients-from-meal/


### Description  
Generates a list of ingredients based on a natural language meal description.

### Sample Request
```
{
  "meal_text": "Stir-fried chicken with broccoli and garlic sauce"
}
```   
### Sample Response
```
json

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

## Sample Response
```
```
  

  
## 2. Ollama Prompt API  
**Endpoint**  
POST /api/ollama/prompt/  

**Description**  
Sends a prompt directly to the Ollama LLM and returns the generated response.
    
### Sample Request

```
{
  "prompt": "Hi Ollama"
}
```

### Sample Response
  
```{
json
  "response": "Hello! How can I help you today?"
}
```
      
## 3. RAG (Retrieval-Augmented Generation) Recommender  
**Endpoint**  
POST /api/rag/query  

**Description**  
Generates personalized dietary or nutrition-related recommendations using user profile and meal data.
    
### Sample Request

```
json
{
"patient_id": 1
}
```

### Sample Response  

```
json
{
    "recommendation": ""
}
```
