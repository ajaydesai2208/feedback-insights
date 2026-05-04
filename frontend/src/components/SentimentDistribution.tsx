import type { Sentiment, SentimentDistribution as SentimentDistributionData } from "../types";

type SentimentDistributionProps = {
  distribution: SentimentDistributionData;
};

const SENTIMENTS: Sentiment[] = ["positive", "neutral", "negative"];

export function SentimentDistribution({ distribution }: SentimentDistributionProps) {
  const total = SENTIMENTS.reduce((sum, sentiment) => sum + distribution[sentiment], 0);

  if (total === 0) {
    return <p className="empty-state">No sentiment data yet.</p>;
  }

  return (
    <div className="distribution-list">
      {SENTIMENTS.map((sentiment) => {
        const count = distribution[sentiment];
        const percent = Math.round((count / total) * 100);

        return (
          <div className="distribution-row" key={sentiment}>
            <div className="ranked-label">
              <span className={`sentiment sentiment-${sentiment}`}>{sentiment}</span>
              <strong>{count}</strong>
            </div>
            <div className="bar-track" aria-label={`${sentiment} ${percent}%`}>
              <span className={`fill-${sentiment}`} style={{ width: `${percent}%` }} />
            </div>
          </div>
        );
      })}
    </div>
  );
}
