from summarize import generate_summary
from evaluate import evaluate_summary

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        text = f.read()

    print("\nGenerating summary...\n")
    summary = generate_summary(text)
    print("🔹 Summary:\n", summary)

    reference = input("\nEnter a human-written reference summary for comparison:\n")
    scores = evaluate_summary(reference, summary)

    print("\n📊 Evaluation Results:")
    for k, v in scores.items():
        print(f"{k}: {v}")
