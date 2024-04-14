#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: CommandLineTool
baseCommand: ["python", "/app/fix.py"]
    
stdout: output.txt

hints:
  DockerRequirement:
    dockerPull: tsrdjan/cwl-step-1:wocmd

inputs:
  data:
    type: File
    inputBinding:
      position: 1

outputs:
  cleaned_data:
    type: File
    outputBinding:
      glob: cleaned.csv