import argparse
from pathlib import Path
import pandas as pd

PROBABILITIES = {
    "New Lead": 5, "Contacted": 10, "Qualified": 25, "Meeting Booked": 40,
    "Proposal Sent": 60, "Negotiation": 80, "Won": 100, "Lost": 0
}

def main():
    parser = argparse.ArgumentParser(description="Summarize a CRM-style sales pipeline.")
    parser.add_argument("--input", default="data/sample_pipeline.csv")
    parser.add_argument("--as-of", default=pd.Timestamp.today().date().isoformat())
    parser.add_argument("--output", default="reports/pipeline_summary.txt")
    args = parser.parse_args()

    df = pd.read_csv(args.input, parse_dates=["last_contact_date", "next_follow_up_date"])
    df["estimated_deal_value_inr"] = pd.to_numeric(df["estimated_deal_value_inr"], errors="raise")
    df["stage_probability_percent"] = pd.to_numeric(df["stage_probability_percent"], errors="raise")
    df["weighted_pipeline_inr"] = df["estimated_deal_value_inr"] * df["stage_probability_percent"] / 100
    as_of = pd.Timestamp(args.as_of)
    df["follow_up_status"] = df["next_follow_up_date"].apply(
        lambda d: "Overdue" if d < as_of else ("Due today" if d == as_of else "Upcoming")
    )

    open_df = df[~df["stage"].isin(["Won", "Lost"])]
    lines = [
        "CRM PIPELINE SUMMARY",
        f"As of: {as_of.date()}",
        f"Total opportunities: {len(df)}",
        f"Open opportunities: {len(open_df)}",
        f"Total estimated pipeline (INR): {df['estimated_deal_value_inr'].sum():,.0f}",
        f"Weighted pipeline (INR): {df['weighted_pipeline_inr'].sum():,.0f}",
        f"Won opportunities: {(df['stage'] == 'Won').sum()}",
        f"Lost opportunities: {(df['stage'] == 'Lost').sum()}",
        f"Overdue follow-ups: {(df['follow_up_status'] == 'Overdue').sum()}",
        "",
        "OPPORTUNITIES BY STAGE",
    ]
    lines += [f"{stage}: {count}" for stage, count in df["stage"].value_counts().reindex(PROBABILITIES.keys(), fill_value=0).items()]
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    print(f"\nSaved summary to {output}")

if __name__ == "__main__":
    main()
