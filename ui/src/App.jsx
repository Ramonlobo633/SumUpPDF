import { useState } from "react";

export default function App() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [summary, setSummary] = useState("");
  const [audioUrl, setAudioUrl] = useState(null);

  const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000";

  async function handleUpload() {
    if (!file) return;

    setLoading(true);
    setSummary("");
    setAudioUrl(null);

    const formData = new FormData();
    formData.append("file", file);

    const uploadRes = await fetch(`${API_BASE}/documents/upload`, {
      method: "POST",
      body: formData,
    });

    const { id } = await uploadRes.json();

    const summaryRes = await fetch(`${API_BASE}/documents/${id}/summary`);
    const summaryData = await summaryRes.json();

    setSummary(summaryData.summary || "No summary returned");
    setAudioUrl(`${API_BASE}/documents/${id}/audio`);
    setLoading(false);
  }

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>SumUpPDF</h1>

      <div style={styles.card}>
        <input
          type="file"
          accept="application/pdf"
          onChange={(e) => setFile(e.target.files[0])}
        />

        <button onClick={handleUpload} style={styles.button} disabled={loading}>
          Upload PDF
        </button>

        {loading && <p style={styles.loading}>Processing document...</p>}

        {summary && (
          <div style={styles.resultBox}>
            <h3>Summary</h3>
            <p>{summary}</p>

            {audioUrl && (
              <audio controls style={{ marginTop: "12px" }}>
                <source src={audioUrl} type="audio/mpeg" />
              </audio>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

const styles = {
  container: {
    minHeight: "100vh",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    background: "linear-gradient(135deg, #667eea, #764ba2)",
    color: "#fff",
    fontFamily: "sans-serif",
  },
  title: {
    marginBottom: "24px",
  },
  card: {
    background: "#fff",
    color: "#333",
    padding: "24px",
    borderRadius: "12px",
    width: "100%",
    maxWidth: "480px",
    boxShadow: "0 10px 30px rgba(0,0,0,0.2)",
    display: "flex",
    flexDirection: "column",
    gap: "12px",
  },
  button: {
    padding: "10px",
    borderRadius: "8px",
    border: "none",
    background: "#667eea",
    color: "#fff",
    cursor: "pointer",
  },
  loading: {
    marginTop: "12px",
    fontStyle: "italic",
  },
  resultBox: {
    marginTop: "16px",
    background: "#f7f7f7",
    padding: "16px",
    borderRadius: "8px",
  },
};
