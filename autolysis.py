# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pandas",
#   "numpy",
#   "matplotlib",
#   "seaborn",
#   "requests",
#   "tenacity",
#   "tabulate"
# ]
# ///

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from tenacity import retry, stop_after_attempt, wait_exponential

def load_data(filename):
    """Load CSV data into a Pandas DataFrame."""
    try:
        df = pd.read_csv(filename, encoding='ISO-8859-1')
        print(f"Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        sys.exit(1)

def analyze_data(df):
    """Perform general data analysis."""
    summary = df.describe(include='all')
    missing_values = df.isnull().sum()
    correlation_matrix = df.corr(numeric_only=True)
    return summary, missing_values, correlation_matrix

def generate_visualizations(df):
    """Generate enhanced visualizations."""
    # Correlation Heatmap
    try:
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
        plt.title("Feature Correlation Heatmap")
        plt.savefig("correlation_heatmap.png", dpi=300)
        plt.close()
        visualizations = ["correlation_heatmap.png"]
    except Exception as e:
        print(f"Warning: Could not generate correlation heatmap: {e}")
        visualizations = []
    
    # Top Rated Books Distribution
    if 'average_rating' in df.columns:
        try:
            plt.figure(figsize=(8, 5))
            sns.histplot(df['average_rating'].dropna(), bins=20, kde=True, color='green')
            plt.title("Distribution of Average Ratings")
            plt.xlabel("Average Rating")
            plt.ylabel("Frequency")
            plt.grid(True, linestyle="--", alpha=0.6)
            plt.savefig("rating_distribution.png", dpi=300)
            plt.close()
            visualizations.append("rating_distribution.png")
        except Exception as e:
            print(f"Warning: Could not generate rating distribution: {e}")
    
    return visualizations

def get_openai_response(prompt, use_api=True):
    """Send a prompt to OpenAI for AI-driven insights."""
    if not use_api:
        return """**AI insights unavailable.** 
OpenAI API rate limit reached or API access disabled. Using offline mode.

You can analyze the data using the summary statistics and visualizations provided in this report."""
    
    ai_proxy_token = os.getenv("AIPROXY_TOKEN")
    if not ai_proxy_token:
        return "AI analysis could not be generated due to missing API token. Set the AIPROXY_TOKEN environment variable."
    
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {ai_proxy_token}", "Content-Type": "application/json"}
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a data analyst."},
            {"role": "user", "content": prompt}
        ]
    }
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, max=30))
    def chat():
        try:
            response = requests.post(url, headers=headers, json=data, timeout=30)
            response.raise_for_status()  # Raise exception for 4XX/5XX status codes
            result = response.json()
            if "choices" in result and len(result["choices"]) > 0:
                return result["choices"][0].get("message", {}).get("content", "")
            else:
                raise ValueError("Invalid response format from API")
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            raise
    
    try:
        result = chat()
        if result:
            print("AI insights successfully generated")
            return result
        return "AI analysis returned empty response."
    except Exception as e:
        print(f"Failed to get AI response after 3 attempts: {e}")
        return f"""**AI insights unavailable due to API error.**

Error details: {str(e)}

This could be due to:
- Rate limits (429 errors)
- Invalid API token
- Network connectivity issues
- Server-side errors

Check your API configuration and try again later."""

def generate_report(filename, summary, missing_values, correlation_matrix, insights, visualizations):
    """Create README.md with analysis results."""
    try:
        with open("README.md", "w") as f:
            f.write(f"# Automated Data Analysis Report\n\n")
            f.write(f"## Dataset: {filename}\n\n")
            f.write("### Summary Statistics\n\n")
            f.write(summary.to_markdown() + "\n\n")
            f.write("### Missing Values\n\n")
            f.write(missing_values.to_markdown() + "\n\n")
            f.write("### Correlation Matrix\n\n")
            f.write(correlation_matrix.to_markdown() + "\n\n")
            f.write("### AI-Generated Insights\n\n")
            f.write(insights + "\n\n")
            f.write("### Visualizations\n\n")
            
            for viz in visualizations:
                f.write(f"![{viz.replace('.png', '')}]({viz})\n\n")
                
        print(f"Report generated successfully: README.md")
    except Exception as e:
        print(f"Error generating report: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: uv run autolysis.py <media.csv>")
        sys.exit(1)
    
    filename = sys.argv[1]
    print(f"Starting analysis of {filename}...")
    
    # Step 1: Load data
    df = load_data(filename)
    
    # Step 2: Analyze data
    print("Analyzing data...")
    summary, missing_values, correlation_matrix = analyze_data(df)
    
    # Step 3: Generate visualizations
    print("Generating visualizations...")
    visualizations = generate_visualizations(df)
    
    # Step 4: Decide whether to use API or skip
    # Change USE_API to False if you want to bypass OpenAI API calls
    USE_API = True  # Set to False to disable API calls
    
    # Step 5: Get AI insights (with graceful fallback)
    if USE_API:
        print("Requesting AI insights...")
        prompt = f"""Analyze the dataset with the following information:
- Summary statistics: {summary.to_string()}
- Missing values: {missing_values.to_string()}
- Correlation matrix: {correlation_matrix.to_string()}

Provide insights into patterns, trends, and notable characteristics of this dataset. 
Interpret the data and suggest possible implications. Format your response as a concise data story."""

        insights = get_openai_response(prompt, use_api=USE_API)
    else:
        print("Skipping AI insights (API disabled)...")
        insights = """**AI insights unavailable - API calls disabled.**

To enable AI-driven insights:
1. Set the AIPROXY_TOKEN environment variable
2. Change USE_API to True in the script
3. Ensure you have internet connectivity and API quota available"""
    
    # Step 6: Generate final report
    print("Generating final report...")
    generate_report(filename, summary, missing_values, correlation_matrix, insights, visualizations)
    print("Analysis complete. Results are available in README.md and visualization files.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAnalysis interrupted by user.")
        sys.exit(130)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)