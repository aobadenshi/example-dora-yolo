import subprocess
import sys
import time
import os

class DoraController:
    def __init__(self, dataflow_yaml):
        self.yaml_path = dataflow_yaml
        self.process = None

    def start(self):
        if self.process is None:
            subprocess.run(["dora", "up"], check=True)
            self.process = subprocess.Popen(["dora", "start", self.yaml_path])
            print(f"Dataflow {self.yaml_path} started (PID: {self.process.pid})")

    def stop(self):
        if self.process:
            self.process.terminate()
            self.process.wait()
            print("Dataflow stopped.")
            self.process = None
        else:
            subprocess.run(["dora", "stop"], check=False)
        subprocess.run(["dora", "destroy"], check=False)

def main():
    try:
        dc = DoraController('dataflow.yaml')
        dc.start()
        while True:
            pass
    except KeyboardInterrupt:
        dc.stop()
    finally:
        sys.exit(0)

if __name__ == "__main__":
    main()
