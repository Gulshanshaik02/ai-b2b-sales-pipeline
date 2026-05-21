import pandas as pd
from google import genai

API_KEY = "YOUR_API_KEY_HERE"
client = genai.Client(api_key=API_KEY)

print("Loading data from spreadsheet...\n")
leads_df = pd.read_csv('leads.csv')

with open('outreach_emails.txt', 'w', encoding='utf-8') as output_file:
    output_file.write("============================================================\n")
    output_file.write("               GENERATED OUTREACH CAMPAIGN TEXT             \n")
    output_file.write("============================================================\n\n")

    for index, row in leads_df.iterrows():
        company_name = row['Company_Name']
        industry = row['Industry']
        pain_point = row['Pain_Point']
        
        print(f"[{index + 1}/{len(leads_df)}] Drafting email for: {company_name}...")
        
        prompt = f"""
        Write a highly professional, 3-sentence cold outreach email to {company_name}, 
        a company operating in the {industry} industry. 
        Focus strictly on how our software helps solve their main problem: {pain_point}.
        Do not use robotic, spammy, or mass-templated opening lines like "Dear Sir" or "To whom it may concern".
        """
        
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            )
            email_text = response.text.strip()

            output_file.write(f"--- Lead #{index + 1}: {company_name} ({industry}) ---\n")
            output_file.write(f"{email_text}\n")
            output_file.write("=" * 60 + "\n\n")
            
        except Exception as e:
            output_file.write(f"An error occurred for {company_name}: {e}\n\n")

print("\nPipeline execution complete! All emails saved to 'outreach_emails.txt'.")