import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

elements = ['a', 'b', 'c', 'd']
pcoll = beam.Create(elements)