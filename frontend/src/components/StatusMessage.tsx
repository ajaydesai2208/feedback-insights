import type { StatusKind } from "../types";

type StatusMessageProps = {
  kind: StatusKind;
  message: string;
};

export function StatusMessage({ kind, message }: StatusMessageProps) {
  if (!message || kind === "idle") {
    return null;
  }

  return (
    <div className={`status status-${kind}`} role={kind === "error" ? "alert" : "status"}>
      {message}
    </div>
  );
}
