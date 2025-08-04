import os
import json

def translate_workflow(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if "description" not in data:
        data["description"] = ""  # Add an empty description if it doesn't exist

    if "translations" not in data:
        data["translations"] = {
            "fa": {
                "name": data["name"],
                "description": data["description"]
            }
        }

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    workflows_dir = 'workflows'
    for filename in os.listdir(workflows_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(workflows_dir, filename)
            try:
                translate_workflow(file_path)
                print(f"Processed {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == '__main__':
    main()
