#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: CommandLineTool
baseCommand: ["python", "/app/split.py"]
    

requirements:
  InlineJavascriptRequirement: {}

hints:
  DockerRequirement:
    dockerPull: tsrdjan/cwl-split

inputs:
  data_file:
    type: File
    inputBinding:
      position: 1
  index: 
    type: int
    inputBinding:
      position: 2
  k: 
    type: int
    inputBinding:
      position: 3

outputs:
  slice_file:
    type: File
    outputBinding:
      glob: "part_$(parseInt(inputs.index)+1).csv"