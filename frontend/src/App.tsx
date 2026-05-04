import { useCallback, useEffect, useState } from "react";
import { API_BASE_URL, getDashboard, getFeedback, getHealth, submitFeedback } from "./api";
import { Dashboard } from "./components/Dashboard";
import { FeedbackInput } from "./components/FeedbackInput";
import { FeedbackTable } from "./components/FeedbackTable";
import { StatusMessage } from "./components/StatusMessage";
import type { DashboardSummary, FeedbackRecord, StatusKind } from "./types";

type StatusState = {
  kind: StatusKind;
  message: string;
};

export default function App() {
  const [dashboard, setDashboard] = useState<DashboardSummary | null>(null);
  const [records, setRecords] = useState<FeedbackRecord[]>([]);
  const [status, setStatus] = useState<StatusState>({ kind: "idle", message: "" });
  const [isLoading, setIsLoading] = useState(true);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [healthStatus, setHealthStatus] = useState("checking");

  const loadData = useCallback(async () => {
    const [dashboardData, feedbackRecords] = await Promise.all([getDashboard(), getFeedback()]);
    setDashboard(dashboardData);
    setRecords(feedbackRecords);
  }, []);

  useEffect(() => {
    let isMounted = true;

    async function initialize() {
      try {
        const health = await getHealth();
        if (!isMounted) {
          return;
        }
        setHealthStatus(health.status);
        await loadData();
      } catch (error) {
        if (!isMounted) {
          return;
        }
        setHealthStatus("unavailable");
        setStatus({ kind: "error", message: error instanceof Error ? error.message : "Unable to load dashboard data." });
      } finally {
        if (isMounted) {
          setIsLoading(false);
        }
      }
    }

    void initialize();

    return () => {
      isMounted = false;
    };
  }, [loadData]);

  async function handleSubmit(text: string) {
    setIsSubmitting(true);
    setStatus({ kind: "loading", message: "Submitting feedback for extraction..." });

    try {
      const response = await submitFeedback(text);
      await loadData();
      const count = response.records.length;
      setStatus({ kind: "success", message: `Created ${count} feedback ${count === 1 ? "record" : "records"}.` });
    } catch (error) {
      setStatus({ kind: "error", message: error instanceof Error ? error.message : "Unable to submit feedback." });
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <main className="app-shell">
      <header className="app-header">
        <div>
          <p className="eyebrow">Feedback Insights</p>
          <h1>Customer feedback dashboard</h1>
        </div>
        <div className="backend-pill">
          <span className={`health-dot health-${healthStatus === "ok" ? "ok" : "warn"}`} />
          <span>{API_BASE_URL}</span>
        </div>
      </header>

      <FeedbackInput isSubmitting={isSubmitting} onSubmit={handleSubmit} />
      <StatusMessage kind={isLoading ? "loading" : status.kind} message={isLoading ? "Loading dashboard..." : status.message} />
      <Dashboard dashboard={dashboard} />
      <FeedbackTable records={records} />
    </main>
  );
}
