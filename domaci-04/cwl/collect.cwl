#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: CommandLineTool
baseCommand: ["python", "/app/collect.py"]
    
stdout: kfold_metrics.txt

hints:
  DockerRequirement:
    dockerPull: tsrdjan/cwl-collect

inputs:
  training_out:
    type: File[]
    inputBinding:
      position: 1

outputs:
  kfold_performance:
    type: stdout