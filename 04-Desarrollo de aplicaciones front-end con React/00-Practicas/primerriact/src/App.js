function App(props) {
  const currDate = new Date();
  return (
    <div>
      <h1>FUNCIONOOOOOOO!</h1>
      <h2>Hoy es {currDate.toLocaleDateString()} y son las {currDate.toLocaleTimeString()}.</h2>
    </div>
  );
}
export default App;