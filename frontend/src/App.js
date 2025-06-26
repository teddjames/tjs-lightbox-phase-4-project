import { useEffect, useState } from "react";
import WorksList from "./WorksLists";
import Filter from "./Filter";

function App() {
  const [works, setWorks] = useState([]);
  const [filterText, setFilterText] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:5000/works")
      .then((r) => r.json())
      .then(setWorks)
      .catch(console.error);
  }, []);

  const filtered = works.filter((w) =>
    w.title.toLowerCase().includes(filterText.toLowerCase())
  );

  return (
    <div style={{ padding: "1rem" }}>
      <h1>My Photography Works</h1>
      <Filter value={filterText} onChange={setFilterText} />
      <WorksList works={filtered} setWorks={setWorks} />
    </div>
  );
}

export default App;
