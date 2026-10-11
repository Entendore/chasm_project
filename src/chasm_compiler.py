#!/usr/bin/env python3
import sys
import re

class ChASMCompiler:
    def __init__(self):
        self.registers = {}
        self.flags = {}
        self.labels = {}
        self.state_commits = {}
        self.output = []

    def compile(self, filepath):
        try:
            with open(filepath, 'r') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"Error: File {filepath} not found.")
            return

        # First pass: map labels
        line_num = 0
        for line in lines:
            line = line.strip()
            if not line or line.startswith(';'): continue
            if line.endswith(':'):
                self.labels[line[:-1]] = line_num
            line_num += 1

        # Second pass: execute/compile
        print(f"\n[ChASM-OS] Initializing Reactor Vessel...")
        print("-" * 50)
        line_num = 0
        for line in lines:
            line = line.split(';')[0].strip() # Strip comments
            if not line or line.endswith(':'): continue
            
            # Simulate execution
            if line.startswith("LOAD_MOL"):
                parts = re.findall(r'(\w+)\s*,\s*(\w+)', line)[0]
                self.registers[parts[0]] = parts[1]
                print(f"[LOAD] \t{parts[0]} <- {parts[1]}")
            
            elif line.startswith("HEAT"):
                print(f"[THERM] \tVessel heated to {line.split(' ')[1]}")
            
            elif line.startswith("STATE_COMMIT"):
                label = line.split(' ')[1]
                self.state_commits[label] = dict(self.registers)
                print(f"[OS] \tState committed to snapshot: {label}")
                
            elif line.startswith("OUT"):
                target = line.split(' ')[1]
                print(f"[OUT] \tDispensing {target} to target destination.")
                
            elif line.startswith("HALT"):
                print("[HALT] \tExecution terminated safely. Reactor standby.")
                break
                
            # Add more instruction parsing here for a full simulator
            line_num += 1

        print("-" * 50)
        print("[ChASM-OS] Run complete.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: chasmc <file.chasm>")
        sys.exit(1)
    
    compiler = ChASMCompiler()
    compiler.compile(sys.argv[1])
