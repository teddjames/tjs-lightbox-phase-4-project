export default function Filter({ value, onChange }) {
  return (
    <input
      placeholder="Filter works…"
      value={value}
      onChange={(e) => onChange(e.target.value)}
      style={{ width: "100%", padding: "0.5rem", margin: "1rem 0" }}
    />
  );
}
