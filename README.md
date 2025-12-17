# API Documentation

## Food Intake Backend - Base URL  
- https://h3vkhzth-8000.asse.devtunnels.ms
    
1. GET /patients/{int}
2. GET /patients/{int}/recommended_intake
3. GET /meals/{int}


  
## Recommender - Base URL
Port-forwarded Django server running on RTX 5070 hardware:  
- https://jqh2g82b-8000.asse.devtunnels.ms
1. POST /api/ollama/generate-ingredients-from-meal
2. POST /api/rag/query
3. GET and POST /api/rag/recommendations/patient/{int}
4. POST /api/rag/query/tr-cn/
5. GET and POST /api/rag/recommendations/patient/{int}/tr-cn/
6. POST /api/ollama/chat/prompt  
  
  
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
        {
            "name": "chicken",
            "food_group": "豆魚蛋肉類",
            "nutrients": [
                "Protein",
                "Fats"
            ]
        },
        {
            "name": "broccoli",
            "food_group": "蔬菜類",
            "nutrients": [
                "Carbohydrate",
                "Water",
                "Total Fiber"
            ]
        },
        {
            "name": "garlic",
            "food_group": "蔬菜類",
            "nutrients": [
                "Water",
                "Total Fiber"
            ]
        },
        {
            "name": "soy sauce",
            "food_group": "調味品類",
            "nutrients": []
        },
        {
            "name": "oil",
            "food_group": "調味品類",
            "nutrients": [
                "Fats"
            ]
        },
        {
            "name": "vinegar",
            "food_group": "調味品類",
            "nutrients": [
                "Water"
            ]
        },
        {
            "name": "ginger",
            "food_group": "蔬菜類",
            "nutrients": [
                "Water",
                "Total Fiber"
            ]
        }
    ]
}
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
 json 
```{
  "response": "Hello! How can I help you today?"
}
```
      
## 3. RAG (Retrieval-Augmented Generation) Recommender  
**Endpoint**  
POST /api/rag/query  

**Description**  
Generates personalized dietary or nutrition-related recommendations using user profile and meal data.
    
### Sample Request  
json
```
{
"query": "# Patient Record  - Patient Name: Granny  - Age:72  - Gender: Female - Height:173 cm  - Weight:98 kg  - BMI:32.74 - Heart Rate:93 bpm - Blood Pressure:140/90 mmHg  - Activity Level:active  # Recommended Daily Intake - Calories:2547 kcal - Protein:78.1 g - Carbohydrates:350.2 g  - Fat:78 g - Total Fiber:35.8 g - Alpha Linolenic Acid:1.1 g - Linoleic Acid:10.998 g  - Total Water:2.7 L # Meal Intakes  ## Meal 1  Meal Name: Braised pork chop  Meal Intake (grams): 690 g    ## Meal 2  Meal Name: Dried fish in soy sauce  Meal Intake (grams):  240 g"
}
```

### Sample Response    
json
```
{
    "recommendation": ""
}
```
     
## 4. RAG (Retrieval-Augmented Generation) Recommender By Patient Id
**Endpoint**  
GET and POST /api/rag/recommendations/patient/{int}

**Description**  
Generates personalized dietary or nutrition-related recommendations using user profile and meal data by patient id
    
### Sample Request     
json
```
# post only
```

### Sample Response    
json
```
{
    "recommendation": ""
}
```
