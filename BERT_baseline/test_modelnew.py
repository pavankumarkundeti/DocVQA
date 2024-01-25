from simpletransformers.question_answering import QuestionAnsweringModel
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

# Model arguments
model_args = {
    "eval_batch_size": 256,
    'output_dir': "./output/",
    'doc_stride': 128,
    'do_lower_case': True,
    'max_seq_length': 384
}

# Path to the model directory
model_dir = './output/best_model/'

# Ensure this directory contains 'config.json', 'pytorch_model.bin', and 'vocab.txt'
model = QuestionAnsweringModel('bert', model_dir, args=model_args)

print(model.args)

# Load the test data
with open('./data_in_squad_format/docvqa_test_squad_format.json') as f:
    json_data = json.load(f)

# Evaluate the model and get predictions
result, model_outputs, wrong_predictions = model.eval_model(json_data)

# Save predictions to a file
with open('./output/predictions_testdata.json', 'w') as f:
    json.dump(model_outputs, f, indent=4)

print("Predictions saved to ./output/predictions_testdata.json")

