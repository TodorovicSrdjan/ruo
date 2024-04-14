cwlVersion: v1.2
class: CommandLineTool
baseCommand: echo

requirements:
  InlineJavascriptRequirement: {}

inputs:
  k:
    type: int

outputs:
  indexes:
    type: int[]
    outputBinding:
      outputEval: |-
          ${
            var indexes = []
            for(var i = 0; i < inputs.k; i++) {
              indexes.push(i)
            }

            return indexes
          }
