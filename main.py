import pandas as pd
from src.extractor import extract_controls
from src.mapper import map_controls
from src.validator import validate_mapping

def read_file(path):
    with open(path, "r") as f:
        return f.read()

iso_text = read_file("data/sample_iso.txt")
hipaa_text = read_file("data/sample_hipaa.txt")

print("Extracting controls...")

iso_controls = extract_controls(iso_text)
hipaa_controls = extract_controls(hipaa_text)

print("Mapping controls...")

mapped = map_controls(iso_controls, hipaa_controls)

for m in mapped:
    m["validation"] = validate_mapping(m["similarity_score"])

df = pd.DataFrame(mapped)
df.to_csv("output/output.csv", index=False)

print("Done! Check output/output.csv")