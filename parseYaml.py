import yaml
with open('customer.yaml', 'r') as f:
    doc = yaml.load(f)
txt = doc["firstName"]
print txt
