import React, { useState } from 'react';
import './App.css';

function App() {
  const [dados, setDados] = useState(null);
  const [selecao, setSelecao] = useState('');

  const buscarDados = (tipo) => {
    fetch(`http://127.0.0.1:8000/${tipo}/`)
      .then(response => response.json())
      .then(data => setDados(data))
      .catch(error => console.error(error));

    setSelecao(tipo);
  };

  return (
    <div className="App">
      <button onClick={() => buscarDados('legislator_votes')}>Votes for Legislator</button>
      <button onClick={() => buscarDados('bill_votes')}>Votes for Bills</button>
      <TabelaDados dados={dados} tipo={selecao} />
    </div>
  );
}

function TabelaDados({ dados, tipo }) {
  if (!dados) return null;

  //init
  return (
    <table>
      <thead>
        <tr>
          {tipo === 'legislator_votes' && <th>Legislator</th>}
          {tipo === 'bill_votes' && <th>Bill</th>}
          <th>Yes Votes</th>
          <th>No Votes</th>
        </tr>
      </thead>
      <tbody>
        {Object.entries(dados).map(([key, value]) => (
          <tr key={key}>
            <td>{key}</td>
            <td>{value.yes}</td>
            <td>{value.no}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default App;
