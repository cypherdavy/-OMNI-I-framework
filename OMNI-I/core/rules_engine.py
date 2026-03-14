def evaluate_rules(data):
    alerts = []
   
    identity_targets = ['oktaverify', 'openid', 'ms-authenticator', 'duo', 'pingid']
    
    if "error" in data:
        return [{"level": "ERROR", "component": "System", "message": data["error"]}]

    for intent in data.get("intents", []):
        for scheme in intent['schemes']:
            
            if scheme in identity_targets and intent['priority'] >= 1:
                alerts.append({
                    "level": "INTERCEPT_VICTOR",
                    "component": intent['component'],
                    "message": f"CRITICAL: Identity scheme '{scheme}' vulnerable to Hijacking (Priority: {intent['priority']})."
                })
            elif scheme not in ['http', 'https']:
                alerts.append({
                    "level": "RISK_HIGH",
                    "component": intent['component'],
                    "message": f"Insecure Custom Scheme '{scheme}' detected."
                })
    return alerts