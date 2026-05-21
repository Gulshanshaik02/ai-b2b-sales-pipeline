# AI-Powered B2B Sales Prospecting Pipeline

## The Business Problem
In B2B sales, executives are forced to choose between manually researching and writing hyper-personalized outreach (which takes hours) or using mass-templated emails (which get flagged as spam). 

## The Solution
This project is an automated Python pipeline that bridges the gap between data architecture and sales strategy. It ingests a structured dataset of target accounts and leverages Google's Gemini AI to dynamically generate highly personalized, solution-oriented cold emails at scale.

## Technical Architecture
* **Language:** Python
* **Data Handling:** Pandas (CSV ingestion and variable extraction)
* **AI Integration:** Google GenAI SDK (Gemini 2.5 Flash Model)
* **Prompt Engineering:** Configured with negative constraints to eliminate robotic tone and enforce a strict problem/solution narrative.

## How It Works
1. The script reads a structured dataset (`leads.csv`) containing Company Names, Industries, and specific Pain Points.
2. It iterates through the dataset, injecting these variables into a dynamic LLM prompt.
3. The API processes the prompt and outputs a customized, 3-sentence email tailored to solve that specific company's pain point.
4. The outputs are automatically logged and saved to an `outreach_emails.txt` file for immediate campaign deployment.
