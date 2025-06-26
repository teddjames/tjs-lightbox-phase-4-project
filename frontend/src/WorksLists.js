import WorkCard from "./WorkCard";

export default function WorksList({ works, setWorks }) {
  return (
    <div style={{ display: "grid", gap: "1rem" }}>
      {works.map((w) => (
        <WorkCard key={w.id} work={w} setWorks={setWorks} />
      ))}
    </div>
  );
}
