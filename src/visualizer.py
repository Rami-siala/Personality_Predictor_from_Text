import matplotlib.pyplot as plt


def show_chart(scores):
    """Display a horizontal bar chart of the Big Five personality profile."""
    traits = list(scores.keys())
    values = list(scores.values())
    colors = ["#4C9BE8", "#5CB85C", "#F0AD4E", "#D9534F", "#9B59B6"]

    fig, ax = plt.subplots(figsize=(8, 4))
    bars = ax.barh(traits, values, color=colors)

    ax.set_xlim(0, 100)
    ax.set_xlabel("Confidence (%)")
    ax.set_title("Big Five Personality Profile")

    for bar, val in zip(bars, values):
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
                f"{val}%", va="center")

    plt.tight_layout()
    plt.show()


def print_summary(dominant):
    """Print the dominant trait and its confidence score."""
    trait, confidence = dominant
    print(f"\nDominant trait: {trait.capitalize()} ({confidence}% confidence)")


def print_breakdown(contributions):
    """Print which words contributed to each trait score."""
    print("\nTrait Breakdown:")
    for trait, words in contributions.items():
        label = trait.capitalize().ljust(20)
        if words:
            parts = [f"{w}({'+' if s > 0 else ''}{s})" for w, s in words]
            print(f"  {label} {', '.join(parts)}")
        else:
            print(f"  {label} —")
