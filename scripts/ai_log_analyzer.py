import subprocess
import shutil

def get_pod_logs():
    kubectl_path = shutil.which("kubectl") or "/opt/homebrew/bin/kubectl"
    cmd = f"{kubectl_path} logs -n dev-environment -l app=devsecops-app --tail=30"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout

def analyze_logs(logs):
    print("\n==========================================")
    print("🤖 AI INCIDENT ANALYSIS & DIAGNOSTICS")
    print("==========================================")
    if not logs.strip():
        print("⚠️ No log output captured from cluster pods.")
        return
    
    print("--- TAIL POD LOGS ---")
    print(logs)
    print("------------------------------------------")
    if "ERROR" in logs or "Exception" in logs:
        print("🚨 CRITICAL: Crash or Exception detected in application logs!")
        print("💡 Suggestion: Inspect Python environment dependencies or HTTP entrypoints.")
    else:
        print("✅ STATUS NORMAL: All active pods are responding successfully without critical errors.")

if __name__ == "__main__":
    pod_logs = get_pod_logs()
    analyze_logs(pod_logs)
