# Frontend

React + TypeScript + Vite frontend for Feedback Insights.

## Features

- Paste one feedback entry or a batch of entries.
- Submit feedback to the local backend for extraction.
- Show loading, success, error, and empty states.
- Display ranked themes, sentiment distribution, sentiment trend, and searchable feedback records.

## Configuration

The API client reads `VITE_API_BASE_URL` and falls back to `http://localhost:8000`.

```powershell
$env:VITE_API_BASE_URL="http://localhost:8000"
```

## Commands

Install dependencies once:

```powershell
npm install
```

Run the dev server:

```powershell
npm run dev
```

Build for verification:

```powershell
npm run build
```
