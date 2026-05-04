import type { DashboardSummary } from "../types";
import { SentimentDistribution } from "./SentimentDistribution";
import { SentimentTrend } from "./SentimentTrend";
import { ThemeFrequency } from "./ThemeFrequency";

type DashboardProps = {
  dashboard: DashboardSummary | null;
};

export function Dashboard({ dashboard }: DashboardProps) {
  const emptyDashboard: DashboardSummary = {
    total_feedback: 0,
    theme_frequencies: [],
    sentiment_distribution: {
      positive: 0,
      neutral: 0,
      negative: 0,
    },
    sentiment_trend: [],
    feedback: [],
  };
  const data = dashboard ?? emptyDashboard;

  return (
    <section className="dashboard-grid" aria-label="Dashboard">
      <article className="panel">
        <h2>Themes</h2>
        <ThemeFrequency themes={data.theme_frequencies} />
      </article>
      <article className="panel">
        <h2>Sentiment</h2>
        <SentimentDistribution distribution={data.sentiment_distribution} />
      </article>
      <article className="panel panel-wide">
        <h2>Trend over time</h2>
        <SentimentTrend trend={data.sentiment_trend} />
      </article>
    </section>
  );
}
