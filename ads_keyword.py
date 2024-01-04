import csv , subprocess
import sys , requests


api_url = "https://api.bobble.ai/v4/keyboardPrompts"
params = {
    "deviceType": "android",
    "languageCodes": "en",
    "appVersion": "999999992",
    "clientId": "7wZFJWA5chjgat68y826IAIKQ6s197RM",
    "timezone": "Asia/Kolkata",
    "sdkVersion": "12",
    "deviceId": "179a5471520f8a8a",
}

try:
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()

        prompts_list = data.get("prompts", [])

        csv_file_path = "shopping_keywords_data.csv"
        with open(csv_file_path, mode="w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Prompt ID", "Keyword"])

            for prompt in prompts_list:
                keywords_dict = prompt.get("settings", {}).get("keywords", {})
                
                if "Shopping" in prompt.get("settings", {}).get("packageSets", []):
                    english_keywords = keywords_dict.get("en", [])

                    for keyword in english_keywords:
                        csv_writer.writerow([prompt['id'], keyword])

        print(f"Data for Shopping keywords successfully written to {csv_file_path}")

    else:
        print(f"Error: {response.status_code} - {response.text}")

except Exception as e:
    print(f"An error occurred: {e}")
# file handling and assertion below

filename = "shopping_keywords_data.csv"

second_data=[]         
with open(filename, 'r') as rf:
    reader = csv.reader(rf, delimiter=',')
    for row in reader:
      second_data.append(row[1])

print(second_data)

# device = sys.argv[1]
device = "9646582087000GS"
        # Prepare environment variables for maestro command
for i, word in enumerate(second_data):
    env_vars = ['-e', f'WORD={word}']
    if i == 0:
        # run the original script for the first env variable
        subprocess.run(["maestro", "--device="+device,"test"] + env_vars + ["amazon_start.yaml"])
        print("Suggestion testing successful for first env variable")
    else:
        # run a different script for the remaining env variables
        subprocess.run(["maestro", "--device="+device,"test"] + env_vars + ["amazon_type.yaml"])
        print(f"Suggestion testing successful for env variable {i+1}")