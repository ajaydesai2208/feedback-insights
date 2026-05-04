import type {
  DashboardSummary,
  FeedbackRecord,
  HealthResponse,
  SubmitFeedbackRequest,
  SubmitFeedbackResponse,
} from "./types";

const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL?.replace(/\/$/, "") ?? "http://localhost:8000";

async function request<T>(path: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: {
      "Content-Type": "application/json",
      ...options?.headers,
    },
    ...options,
  });

  if (!response.ok) {
    throw new Error(await readError(response));
  }

  return (await response.json()) as T;
}

async function readError(response: Response): Promise<string> {
  try {
    const body = (await response.json()) as { detail?: string; message?: string };
    return body.detail ?? body.message ?? `Request failed with ${response.status}`;
  } catch {
    return `Request failed with ${response.status}`;
  }
}

export function getHealth(): Promise<HealthResponse> {
  return request<HealthResponse>("/health");
}

export function submitFeedback(text: string): Promise<SubmitFeedbackResponse> {
  const body: SubmitFeedbackRequest = { text };

  return request<SubmitFeedbackResponse>("/feedback", {
    method: "POST",
    body: JSON.stringify(body),
  });
}

export function getFeedback(): Promise<FeedbackRecord[]> {
  return request<FeedbackRecord[]>("/feedback");
}

export function getDashboard(): Promise<DashboardSummary> {
  return request<DashboardSummary>("/dashboard");
}

export { API_BASE_URL };
