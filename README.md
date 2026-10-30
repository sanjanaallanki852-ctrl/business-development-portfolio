# Project 3 — CRM Pipeline & Sales Funnel Management

## Business problem
Sales teams need a consistent way to track opportunities, understand where leads are in the sales process and avoid missing follow-ups.

## Objective
Build a simple CRM-style tracker and dashboard to monitor pipeline stages, estimated deal values and next actions.

## Dataset
`data/sample_pipeline.csv` contains 50 **synthetic** opportunities. Names, owners, deal values, dates and stages are invented for practice.

## Pipeline stages
1. New Lead
2. Contacted
3. Qualified
4. Meeting Booked
5. Proposal Sent
6. Negotiation
7. Won
8. Lost

## Illustrative probability assumptions
The sample data uses stage probabilities (5%, 10%, 25%, 40%, 60%, 80%, 100%, 0%). These are examples only. A real team should estimate probabilities from its historical conversion data.

`Weighted pipeline = Estimated deal value × stage probability`

## How to use
1. Open the CSV in Excel or Google Sheets.
2. Review stage names and probability assumptions.
3. Calculate weighted pipeline value for each opportunity.
4. Flag follow-ups where the next follow-up date is before the reporting date.
5. Summarize opportunity count by stage, total pipeline, weighted pipeline and overdue follow-ups.
6. Run the Python script:

```bash
pip install -r requirements.txt
python src/pipeline_report.py --input data/sample_pipeline.csv --as-of 2026-10-30 --output reports/pipeline_summary.txt
```

## Suggested dashboard KPIs
- Total open opportunities
- Total estimated pipeline value
- Weighted pipeline value
- Opportunity count by stage
- Won and lost opportunity counts
- Overdue follow-ups

## Deliverables
- Opportunity tracker
- Sales-stage definitions
- Follow-up monitoring
- Pipeline KPI summary

## Limitations and integrity
This is a simulated exercise. It does not represent actual CRM usage, customer contact, meetings, revenue or sales conversion. Keep real customer data confidential and use only authorized information.

## Resume-ready description
Built a simulated CRM pipeline tracker for 50 opportunities across eight sales stages and defined weighted pipeline, stage-distribution and follow-up metrics for a sales dashboard.
