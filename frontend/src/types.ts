export type Sentiment = "positive" | "neutral" | "negative";

export type FeedbackRecord = {
  id: string;
  original_feedback: string;
  sentiment: Sentiment;
  themes: string[];
  action_items: string[];
  created_at: string;
};

export type ThemeFrequencyItem = {
  theme: string;
  count: number;
};

export type SentimentDistributionItem = {
  sentiment: Sentiment;
  count: number;
};

export type SentimentTrendItem = {
  date: string;
  positive: number;
  neutral: number;
  negative: number;
};

export type DashboardSummary = {
  theme_frequencies: ThemeFrequencyItem[];
  sentiment_distribution: SentimentDistributionItem[];
  sentiment_trend: SentimentTrendItem[];
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
