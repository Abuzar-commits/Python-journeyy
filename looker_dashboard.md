# Looker Studio Dashboard Plan (KRAs, KPIs, 1:1 Feedback, Team Goals)

This guide describes how to integrate key results areas (KRAs), key performance indicators (KPIs), 1:1 feedback parameters, and team goals into a single Looker Studio dashboard. It includes a lightweight data model, sample sheet layout, and the core steps to publish the dashboard.

## Quick Start

1. Upload `data/kra_kpi_sample.csv` to Google Sheets (or BigQuery).
2. Connect the sheet/table as a data source in Looker Studio and add the calculated fields listed below.
3. Build scorecards, time series, and tables using the suggested visuals, then publish the report to your team.

## Data Model

Use a single table (Google Sheet or BigQuery table) with the following columns:

| Column | Description |
| --- | --- |
| `Person` | Teammate name. |
| `Role` | Job title/track. |
| `TeamGoal` | The team or company goal the metric rolls up to. |
| `KRA` | Key result area (e.g., Delivery, Quality, Growth). |
| `KPI` | The measurable indicator tied to the KRA. |
| `Target` | Numeric target for the KPI during the period. |
| `Actual` | Actual numeric result achieved. |
| `PeriodStart` | Start date of the measurement period. |
| `PeriodEnd` | End date of the measurement period. |
| `FeedbackScore` | Quantified 1:1 feedback (e.g., 1–5 or 1–10). |
| `FeedbackNotes` | Qualitative notes from 1:1s. |
| `Manager` | Manager/mentor responsible. |
| `UpdatedAt` | Timestamp for last data refresh. |

### Recommended Calculated Fields

Create the following calculated fields inside Looker Studio:

- **Attainment %**: `Actual / Target`
- **Goal Status**: `CASE WHEN Actual >= Target THEN "On Track" ELSE "At Risk" END`
- **Feedback Avg**: `AVG(FeedbackScore)` aggregated by Person/Manager/Period
- **Health Index** (optional): `(0.6 * Attainment %) + (0.4 * (FeedbackScore / 10))`

## Sample Google Sheet Layout

You can load the sample CSV in `data/kra_kpi_sample.csv` into a Google Sheet and use it as your Looker Studio data source. Keep all columns as plain text/number/date; avoid merged cells.

## Building the Dashboard in Looker Studio

1. **Prepare the data source**
   - Import `data/kra_kpi_sample.csv` into Google Sheets (File → Import → Upload) or upload directly to BigQuery as a table.
   - Ensure date columns (`PeriodStart`, `PeriodEnd`, `UpdatedAt`) are typed as Date/DateTime.
2. **Create data source**
   - In Looker Studio, click **Create → Data source** and choose Google Sheets (or BigQuery) pointing to the table.
   - Add calculated fields for **Attainment %**, **Goal Status**, and **Health Index**.
3. **Build core visuals**
   - **Scorecards**: Attainment %, Feedback Avg, Health Index (overall and per team).
   - **Time series**: Attainment % over time by TeamGoal or KRA.
   - **Tables**: Person, Role, KRA, KPI, Target, Actual, Attainment %, FeedbackScore, FeedbackNotes, Manager, Period.
   - **Bullet/Bar charts**: Target vs Actual by KPI and by Person.
   - **Heatmap**: Attainment % by KRA vs Person to quickly spot risk areas.
4. **Filters and controls**
   - Date range control (PeriodStart/PeriodEnd).
   - Drop-down filters for TeamGoal, KRA, KPI, Role, Manager.
   - Optional: “At Risk” quick filter based on Goal Status.
5. **Drilldowns**
   - Enable table drilldown Person → KRA → KPI for layered analysis.
   - Add a detail page that shows recent FeedbackNotes for the selected person.
6. **Delivery and governance**
   - Set data refresh for Sheets (hourly) or BigQuery (scheduled loads).
   - Share with view-only access for the team, edit access for data stewards.
   - Add a banner noting the last `UpdatedAt` from the dataset.

## 1:1 Feedback Integration

- Keep FeedbackScore numeric to allow aggregation; map common parameters such as **Growth**, **Blockers**, **Engagement** inside `FeedbackNotes`.
- Use conditional formatting on FeedbackScore to flag scores below threshold (e.g., < 3 out of 5).
- In the detail page, surface the latest FeedbackNotes alongside the person’s KPI trend.

## Team Goals Alignment

- Use the `TeamGoal` column to group KRAs/KPIs by strategic objectives.
- Add a stacked bar or treemap by TeamGoal → KRA to visualize contribution.
- Include a narrative text box on the dashboard summarizing current on-track vs at-risk counts using the **Goal Status** field.

## How to Extend

- If multiple periods are needed, append rows per period; Attainment % and Feedback Avg will aggregate correctly by period.
- If you later migrate to a warehouse, keep the same column names to avoid rebuilding the dashboard—just swap the data source to BigQuery.
- To blend multiple sources (e.g., Jira throughput + Survey tool), use Person/Period as the key in Looker Studio’s blend and maintain the Attainment % field in each source.
