import { FormEvent, useState } from "react";

type FeedbackInputProps = {
  isSubmitting: boolean;
  onSubmit: (text: string) => Promise<void>;
};

export function FeedbackInput({ isSubmitting, onSubmit }: FeedbackInputProps) {
  const [text, setText] = useState("");

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const trimmedText = text.trim();

    if (!trimmedText) {
      return;
    }

    await onSubmit(trimmedText);
    setText("");
  }

  return (
    <form className="panel feedback-input" onSubmit={handleSubmit}>
      <div>
        <h2>Submit feedback</h2>
        <p>Paste one customer note or a batch of entries. The backend will split and extract insights.</p>
      </div>
      <textarea
        aria-label="Customer feedback"
        value={text}
        onChange={(event) => setText(event.target.value)}
        placeholder="Example: The setup was easy, but reporting needs CSV export."
        rows={8}
      />
      <div className="form-row">
        <span>{text.trim() ? `${text.trim().split(/\n\s*\n|^\s*[-*]\s+/m).filter(Boolean).length} pasted section(s)` : "No feedback entered"}</span>
        <button type="submit" disabled={isSubmitting || !text.trim()}>
          {isSubmitting ? "Submitting..." : "Submit feedback"}
        </button>
      </div>
    </form>
  );
}
