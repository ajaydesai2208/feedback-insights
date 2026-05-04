export type Sentiment = "positive" | "neutral" | "negative";

export type FeedbackRecord = {
  id: number;
  feedback_text: string;
  sentiment: Sentiment;
  themes: string[];
  action_items: string[];
  created_at: string;
};

export type ThemeFrequencyItem = {
  theme: string;
  count: number;
};

export type SentimentDistribution = Record<Sentiment, number>;

export type SentimentTrendItem = {
  date: string;
  positive: number;
  neutral: number;
  negative: number;
};

export type DashboardSummary = {
  total_feedback: number;
  theme_frequencies: ThemeFrequencyItem[];
  sentiment_distribution: SentimentDistribution;
  sentiment_trend: SentimentTrendItem[];
  feedback: FeedbackRecord[];
};

export type SubmitFeedbackRequest = {
  text: string;
};

export type SubmitFeedbackResponse = {
  records: FeedbackRecord[];
};

export type HealthResponse = {
  status: string;
};

export type StatusKind = "idle" | "loading" | "success" | "error";
