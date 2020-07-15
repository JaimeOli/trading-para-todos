import subprocess

def getdukadata():
    process = subprocess.Popen("./scripts/daily_data_collection.sh", shell=True, stdout=subprocess.PIPE)
    print("Getting data via duka")
    process.wait()
    print(process.returncode)