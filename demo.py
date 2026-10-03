from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys
import pandas


from us_visa.pipline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()

