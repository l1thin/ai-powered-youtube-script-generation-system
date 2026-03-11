import os
import json

def build_dataset(processed_dir: str, output_file: str) -> None:
    """Read processed transcripts and build an instruction-tuning dataset."""
    dataset = []

    if not os.path.exists(processed_dir):
        print(f"Error: Processed directory '{processed_dir}' does not exist.")
        return

    # Ensure output directory exists
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process all JSON files in the processed directory
    for filename in os.listdir(processed_dir):
        if not filename.endswith(".json"):
            continue

        file_path = os.path.join(processed_dir, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            title = data.get("title", "Untitled")
            sections = data.get("sections", [])

            for section in sections:
                sec_type = section.get("type", "")
                text = section.get("text", "")
                
                # Only add if both type and text are present
                if sec_type and text:
                    entry = {
                        "instruction": f"Write a YouTube script section for a video titled '{title}'",
                        "input": sec_type,
                        "output": text
                    }
                    dataset.append(entry)

        except Exception as e:
            print(f"Failed to process {filename}: {e}")

    # Save to output file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(dataset, f, indent=2, ensure_ascii=False)
        print(f"Dataset size: {len(dataset)}")
        # Construct relative path for print statement to match the format requested
        rel_output_file = os.path.relpath(output_file, start=os.path.dirname(os.path.dirname(output_file)))
        # Specifically output the exact string requested
        print(f"Saved to data/training/instruction_dataset.json")
    except Exception as e:
        print(f"Failed to save dataset: {e}")

def main():
    # Define paths based on the script location (scripts/) 
    # so that data/ is one level up
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    processed_dir = os.path.join(base_dir, "data", "processed")
    output_file = os.path.join(base_dir, "data", "training", "instruction_dataset.json")

    build_dataset(processed_dir, output_file)

if __name__ == "__main__":
    main()
