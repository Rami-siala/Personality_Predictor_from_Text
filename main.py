from src.preprocessor import preprocess
from src.scorer import load_lexicon, score
from src.visualizer import show_chart, print_summary, print_breakdown


def main():
    print("=" * 45)
    print("  Personality Predictor from Text")
    print("=" * 45)

    lexicon = load_lexicon()

    while True:
        print("\nDescribe yourself in a few sentences (or type 'quit' to exit):")
        text = input("> ").strip()

        if text.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break

        if not text:
            print("Please enter some text.")
            continue

        stems, originals = preprocess(text)

        if not stems:
            print("No meaningful words found. Try writing more.")
            continue

        results = score(stems, originals, lexicon)

        print_summary(results["dominant"])
        print_breakdown(results["contributions"])
        show_chart(results["scores"])


if __name__ == "__main__":
    main()
