# API Documentation

## Food Intake Backend - Base URL  
- https://h3vkhzth-8000.asse.devtunnels.ms/api/patients/1
    
1. patients/{int}/
2. patients/{int}/recommended_intake
3. patients/{int}/meals


  
## Recommender - Base URL
Port-forwarded Django server running on RTX 5070 hardware:  
- https://jqh2g82b-8000.asse.devtunnels.ms
  
  
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
      
3. RAG (Retrieval-Augmented Generation)  
**Endpoint**  
POST /api/rag/  

**Description**  
Generates personalized dietary or nutrition-related recommendations using user profile and meal data.
    
### Sample Request
```
json

{
"query": "# Patient Record  - Patient Name: Granny  - Age:72  - Gender: Female - Height:173 cm  - Weight:98 kg  - BMI:32.74 - Heart Rate:93 bpm - Blood Pressure:140/90 mmHg  - Activity Level:active  # Recommended Daily Intake - Calories:2547 kcal - Protein:78.1 g - Carbohydrates:350.2 g  - Fat:78 g - Total Fiber:35.8 g - Alpha Linolenic Acid:1.1 g - Linoleic Acid:10.998 g  - Total Water:2.7 L # Meal Intakes  ## Meal 1  Meal Name: Braised pork chop  Meal Intake (grams): 690 g    ## Meal 2  Meal Name: Dried fish in soy sauce  Meal Intake (grams):  240 g"
}
```
```
{
     "patient": {},
     "recommended_intake":{},
     "meals": []
}
```
```
{
"patient": {
     "name": ,
      "age": ,
     "sex": ",
     "height_cm": ,
     "weight_kg": ,
     "heart": active,
     "systolic_bp":
     "diastolic_bp": 
     "activity_level": active,
     "bmi": 
},
"recommended_intake":{
     "daily_caloric_needs",
     "carbohydrate",
     "total_fiber",
     "protein",
     "fat",
     "alpha_linolenic_acid",
     "linoleic_acid",
     "total_water",
},
"meals": [
     {
     "meal_name",
     "meal_time",
     "day_cycle",
     "meal_description",
     },
      {
     "meal_name",
     "meal_time",
     "day_cycle",
     "meal_description",
     },
      {
     "meal_name",
     "meal_time",
     "day_cycle",
     "meal_description",
     },
]
}
```   
## Sample Response
```
json
{
    "recommendation": "Based on Granny's record, here’s an analysis and recommendations:\n\n### 1. **Analysis**\n- **BMI and Health Risks**: At 32.7 kg/m², Granny is obese, increasing risks for hypertension (BP 140/90), heart disease, and metabolic issues. Her active lifestyle is a positive factor but may not compensate for dietary excesses.\n- **Dietary Adequacy**:\n  - **Protein**: High intake from pork and dried fish (likely exceeding needs if not balanced with other foods). Pork is high in saturated fat, which may worsen cardiovascular health.\n  - **Fiber**: Likely low due to meat-heavy meals. Recommended fiber (35.8g/day) requires significant plant-based foods, which aren’t evident.\n  - **Sodium**: High risk from dried fish (traditional Cantonese-style salted fish may contain excessive salt, linked to hypertension and stomach cancer in studies).\n  - **Calories**: The two large meals (pork chop + dried fish) may contribute excess calories, hindering weight management despite activity.\n  - **Hydration**: Adequate water intake (2.7L) is good, but monitoring is advised.\n\n### 2. **Suggestions**\n- **Improve Balance**: Add fiber-rich foods (whole grains, legumes, vegetables) and fruits to meet recommendations. Include lean protein sources (e.g., poultry, fish, tofu) instead of relying solely on fatty meats.\n- **Reduce Sodium**: Limit salted fish and processed meats. Opt for fresh alternatives and use herbs/spices for flavor.\n- **Manage Weight**: Reduce portion sizes of high-calorie, high-fat foods and increase calorie-burning activities.\n- **Monitor BP**: Track blood pressure regularly and consult a healthcare provider for potential medication or lifestyle changes.\n\n### 3. **Recommendations**\n- **Dietary Adjustments**: Work with a dietitian to create a meal plan balancing protein, fiber, and low-sodium foods. Include traditional Cantonese dishes adapted for health (e.g., steamed fish with vegetables).\n- **Health Monitoring**: Schedule check-ups for hypertension and obesity. Educate Granny on the risks of high sodium and saturated fats.\n- **Hydration Support**: Encourage water intake and limit sugary drinks to support weight management.\n\nGranny’s active lifestyle is a strength, but dietary changes are crucial. A tailored plan can help her manage weight and BP while maintaining vitality."
}
```
