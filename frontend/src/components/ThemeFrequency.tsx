import type { ThemeFrequencyItem } from "../types";

type ThemeFrequencyProps = {
  themes: ThemeFrequencyItem[];
};

export function ThemeFrequency({ themes }: ThemeFrequencyProps) {
  if (themes.length === 0) {
    return <p className="empty-state">No themes yet.</p>;
  }

  const maxCount = Math.max(...themes.map((item) => item.count), 1);

  return (
    <ol className="ranked-list">
      {themes.map((item) => (
        <li key={item.theme}>
          <div className="ranked-label">
            <span>{item.theme}</span>
            <strong>{item.count}</strong>
          </div>
          <div className="bar-track" aria-hidden="true">
            <span style={{ width: `${(item.count / maxCount) * 100}%` }} />
          </div>
        </li>
      ))}
    </ol>
  );
}
