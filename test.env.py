from dotenv import load_dotenv
import os

load_dotenv()

print("Raw environment variables:")
print(f"BASE_URL: '{os.getenv('ATLASSIAN_BASE_URL')}'")
print(f"EMAIL: '{os.getenv('ATLASSIAN_EMAIL')}'") 
print(f"API_TOKEN: '{os.getenv('ATLASSIAN_API_TOKEN')}'")