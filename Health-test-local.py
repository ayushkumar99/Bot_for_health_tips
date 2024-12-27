from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

client = MiraClient(config={"API_KEY": api_key})  

# Load flow configuration
flow = Flow(source="Bot_for_health_tips\flow.yaml")

# Prepare test input
test_input = {
    "mood": "stressed",
    "energy_level": "low",
    "hydration_status": "no"
}

# Test flow
response = client.flow.test(flow, test_input)

# Output response
print("Test Response:", response)
