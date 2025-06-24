# 🥗 Thattu.ai Smart Tamil Meal Planner – End-to-End Data Pipeline

A modern, ML-powered data pipeline that recommends healthy, Tamil-style meals based on user preferences, built using:

> **S3 + AWS Glue + Snowflake + dbt + Airflow + Databricks + Slack + Tableau**

---

## 🚀 Project Objective

This project simulates a **production-grade data pipeline** that:
- Ingests Tamil recipe data and user dietary preferences
- Cleans and transforms data using ELT workflows
- Stores structured data in **Snowflake**
- Uses **Databricks + ML** to recommend personalized meals
- Visualizes macro breakdown in **Tableau**
- Sends alerts via **Slack** with meal plan suggestions

> 🔁 Built to showcase modern **DataOps** and orchestration using **Apache Airflow**

---

## 💡 Use Case: Smart Tamil Meal Planner

### 🎯 Goal
Help users plan **healthy Tamil meals** that align with:
- Their **calorie goals** (e.g., 1200–1500 kcal/day)
- **Meal types** (breakfast, lunch, dinner, snack)
- **Dietary preferences** (veg, high-protein, diabetic-friendly)
- Ingredient availability, allergies, or dislikes

The system processes recipes and user profiles to generate **daily/weekly meal plans**, delivered via Slack and visualized in Tableau.

---

### 🧾 Input Data

| Source | Description |
|--------|-------------|
| **Tamil Recipes Dataset** |  
Recipe name, ingredients, instructions, calories, macros, cuisine tags, meal type |
| **User Profile** |  
Name, daily calorie goal, preferences (veg/non-veg), allergies, dislikes, available ingredients |

---

### 🔍 Data Transformation & Modeling (dbt)

- Normalize ingredients and classify meals
- Calculate missing calories/macros per serving
- Build `dim_user`, `dim_meal_type`, `dim_ingredient`
- Generate `fact_user_meal_plan` table with suggestions

---

### 🤖 Machine Learning (Databricks)

- **Option 1**: Rule-based filtering  
- **Option 2**: Collaborative filtering (LightFM)  
- Optional: Calorie optimizer to stay within target range
- Future: TensorFlow classification for health-specific diets

---

### ⚙️ Pipeline Workflow (Airflow DAG)

1. Ingest recipe + user profile data into S3
2. Run AWS Glue job to clean & enrich data
3. Load curated data into Snowflake
4. Transform with dbt models
5. Run ML model in Databricks
6. Save recommendations to Snowflake
7. Send Slack notification to user with their plan
8. Refresh Tableau dashboard

---

### 📥 Example User Scenario

**User**: Abinaya  
**Target**: 1200 kcal/day  
**Preferences**: Vegetarian, high-protein  
**Dislikes**: Raw onion  
**Ingredients on hand**: Carrot, beans, oats, toor dal

| Meal | Suggestion | Calories |
|------|------------|----------|
| Breakfast | Oats Pongal | 320 kcal |
| Snack | Sundal | 150 kcal |
| Lunch | Beans Poriyal + Sambar + Red Rice | 480 kcal |
| Dinner | Tofu Kurma + Phulka | 250 kcal |

✅ Slack Alert  
✅ Tracked in Snowflake  
✅ Dashboard in Tableau

---

### 🧰 Tech Stack

| Component | Tool |
|----------|------|
| **Data Sources** | Tamil Recipes CSV, User Preferences |
| **Storage** | Amazon S3 |
| **ETL** | AWS Glue |
| **Data Warehouse** | Snowflake |
| **Transformation** | dbt |
| **Orchestration** | Apache Airflow |
| **ML Modeling** | Databricks |
| **Alerting** | Slack |
| **Dashboard** | Tableau |

---

## 📂 Folder Structure

meal-planner-pipeline/
│
├── airflow_dags/ # Airflow DAGs
├── dbt/ # dbt project
├── data/ # Sample recipe & user data
├── glue_jobs/ # PySpark scripts for AWS Glue
├── notebooks/ # ML notebooks for Databricks
├── tableau/ # Tableau workbook or screenshots
├── utils/ # Slack alerts, config, helpers
└── README.md

---

## 📊 Tableau Dashboard

> [Insert link or screenshot here]

---

## 🧪 Future Enhancements

- [ ] Voice-based assistant (LangChain or Whisper)
- [ ] Live integration with grocery APIs (e.g., Walmart or Amazon Fresh)
- [ ] Export meal plans to mobile calendar/reminders
- [ ] Add meal logging + calorie tracking feedback loop

---

## ✍️ Author

**Abinaya Sankaralingam**  
Senior Data Engineer | Aspiring TPM | YouTube Creator  
📍 Canada | 💼 10+ years in Data & ETL | 🌐 [LinkedIn](https://linkedin.com/in/your-link)

---

## 📌 License

MIT License. Free to fork, learn, and build on!
