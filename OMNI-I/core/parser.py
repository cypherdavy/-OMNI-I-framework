import xml.etree.ElementTree as ET

def parse_manifest(file_path):
   
    ns = {'android': 'http://schemas.android.com/apk/res/android'}
    ET.register_namespace('android', ns['android'])
    
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except Exception as e:
        return {"error": f"Failed to parse XML: {e}"}

    ns_prefix = f"{{{ns['android']}}}"
    data = {"intents": [], "components": []}

    for tag in root.findall(".//activity") + root.findall(".//service"):
        component_name = tag.attrib.get(f"{ns_prefix}name", "Unknown")
        
        for intent_filter in tag.findall("intent-filter"):
            priority = int(intent_filter.attrib.get(f"{ns_prefix}priority", 0))
            schemes = [d.attrib.get(f"{ns_prefix}scheme") for d in intent_filter.findall("data") if d.attrib.get(f"{ns_prefix}scheme")]
            
            if schemes:
                data["intents"].append({
                    "component": component_name,
                    "priority": priority,
                    "schemes": schemes
                })
    return data