from datasets import load_metric

def evaluate_summary(reference, prediction):
    rouge = load_metric("rouge")
    result = rouge.compute(predictions=[prediction], references=[reference])
    return result
