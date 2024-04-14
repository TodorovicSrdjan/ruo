#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: CommandLineTool
baseCommand: ["python", "/app/train.py"]

hints:
  DockerRequirement:
    dockerPull: tsrdjan/cwl-step-2:wocmd

inputs:
  data:
    type: File
    inputBinding:
      position: 1
  training_ratio:
    type: float
    inputBinding:
      position: 2
  target_col:
    type: string
    inputBinding:
      position: 3

outputs:
  test_performance:
    type: stdout

stdout: std-output.txt