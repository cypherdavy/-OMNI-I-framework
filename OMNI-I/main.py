import argparse
from colorama import init, Fore, Style
from pyfiglet import Figlet
from core.parser import parse_manifest
from core.rules_engine import evaluate_rules

# Initialize Colors for the OMNI-I Terminal UI
init(autoreset=True)

def main():
    # 1. Display the "Famous" ASCII Banner
    f = Figlet(font='slant')
    print(Fore.GREEN + f.renderText('OMNI-I'))
    print(Fore.CYAN + "[ IDENTITY INTERCEPTION FRAMEWORK v1.0 ]\n")
    
    
    parser = argparse.ArgumentParser(description="OMNI-I Manifest Security Scanner")
    parser.add_argument("-m", "--manifest", required=True, help="Path to AndroidManifest.xml")
    args = parser.parse_args()

    
    data = parse_manifest(args.manifest)
    
    
    alerts = evaluate_rules(data)

    
    print(Fore.WHITE + "="*60)
    if not alerts:
        print(Fore.GREEN + "[+] NO VULNERABILITIES DETECTED.")
    else:
        for alert in alerts:
            
            color = Fore.RED if "VICTOR" in alert['level'] else Fore.YELLOW
            print(f"{color}[{alert['level']}] {Style.BRIGHT}{alert['component']}")
            print(f"    -> {alert['message']}")
            
           
            if alert['level'] == "INTERCEPT_VICTOR":
               
                parts = alert['message'].split("'")
                if len(parts) > 1:
                    scheme = parts[1].replace("://", "")
                    
                   
                    print(Fore.GREEN + Style.BRIGHT + f"\n    [!] GENERATED OMNI-I REFLECTOR HOOK:")
                    print(Fore.GREEN + fr"    if($Data -like '*{scheme}*') {{ Start-Process chrome.exe $Data }}")
                    print(Fore.YELLOW + f"    (Paste this into your Dashboard for active session reflection)\n")
    
    print(Fore.WHITE + "="*60)

if __name__ == "__main__":
    main()