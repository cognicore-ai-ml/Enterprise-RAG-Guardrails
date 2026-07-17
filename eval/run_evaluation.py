from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision
from datasets import Dataset

# 1. Load your test dataset 
# Replace this with your actual test questions and ground truth answers
data = {
    "question": ["What is the company policy on remote work?", "How do I request time off?"],
    "answer": ["Remote work is allowed 3 days a week.", "Submit a form in the HR portal."],
    "contexts": [["Policy document about remote work...", "Company handbook..."], ["HR portal documentation...", "Time off policy..."]],
    "ground_truth": ["Employees can work remotely 3 days a week.", "You must submit a request via the HR portal."]
}

test_dataset = Dataset.from_dict(data)

# 2. Run the evaluation
print("Running RAGAS evaluation...")
results = evaluate(
    dataset=test_dataset,
    metrics=[faithfulness, answer_relevancy, context_precision]
)

# 3. Save results to a file for your portfolio
results.to_pandas().to_csv("eval/results.csv")

print("\n--- Evaluation Results ---")
print(results)

