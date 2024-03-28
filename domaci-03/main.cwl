#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: Workflow

inputs:
  data: File
  target_col: string
  training_ratio: float

outputs:
  out:
    type: File
    outputSource: train/test_performance

steps:
  prepare:
    run: prep.cwl
    in:
      data: data
    out: [cleaned_data]
  train:
    run: train.cwl
    in:
      data:
        source: prepare/cleaned_data
      training_ratio: training_ratio
      target_col: target_col
    out: [test_performance]