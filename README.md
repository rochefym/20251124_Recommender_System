# API Endpoints
**BASE URL**
port forwarded Django server address on RTX 5070 hardware server:
- https://jqh2g82b-8000.asse.devtunnels.ms/

# Generate Ingredients from meal
## api/ollama/generate-ingredients-from-meal/
## api/ollama/generate-ingredients-from-meal/
    
**Sample JSON Request**  
```
{
"meal_text": "Stir-fried chicken with broccoli and garlic sauce"
}
```




# OLLAMA
## api/ollama/prompt/

**Sample JSON Request** 
```
{
"prompt": "HI ollama"
}
 </code>
</pre>

# RAG
**Sample JSON Request** 
<pre>
  <code>
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
```
