#!/usr/bin/env cwl-runner

cwlVersion: v1.2
class: Workflow

requirements:
  ScatterFeatureRequirement: {}
  SubworkflowFeatureRequirement: {}
  InlineJavascriptRequirement: {}

inputs:
  csv_file: File
  target_col: string
  k: int

outputs:
  rez: 
    type: File
    outputSource: collect/kfold_performance

steps:
  idx_gen:
    in:
      k: k
    out: [indexes]
    run: idx-gen.cwl

  subworkflow:
    in:
      index: idx_gen/indexes
      data_file: csv_file
      target_col: target_col
      k: k
      training_ratio: {default: 0.8}
    out: [metrics]
    scatter: index
    run:
      class: Workflow
      inputs:
        index: int
        data_file: File
        target_col: string
        k: int
        training_ratio: float
      outputs: 
        metrics:
          type: File
          outputSource: train/test_performance
      steps:
        generate_indexes:
          in:
            k: k 
          out: [indexes]
          run: idx-gen.cwl

        split:
          run: split.cwl
          in:
            data_file: data_file
            index: index
            k: k
          out: [slice_file]

        prepare:
          run: prep.cwl
          in:
            data: split/slice_file
          out: [cleaned_data]

        train:
          run: train.cwl
          in:
            data:
              source: prepare/cleaned_data
            training_ratio: training_ratio
            target_col: target_col
          out: [test_performance]
  
  collect:
    in:
      training_out: 
        source: subworkflow/metrics
    out: [kfold_performance]
    run: collect.cwl