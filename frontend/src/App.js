import React, { useState } from 'react';
import './App.css';

function App() {
  const [data, setData] = useState(null);
  const [selection, setSelection] = useState('');

  const fetchData = (type) => {
    fetch(`http://127.0.0.1:8000/${type}/`)
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error(error));

    setSelection(type);
  };

  return (
    <div className="App">
      <button className="button" onClick={() => fetchData('legislator_votes')}>Votes for Legislator</button>
      <button className="button" onClick={() => fetchData('bill_votes')}>Votes for Bills</button>
      <DataTable data={data} type={selection} />
    </div>
  );
}

function DataTable({ data, type }) {
  if (!data) return null;

  return (
    <div className="table-container">
      <table className="styled-table"> 
        <thead>
        <tr className="active-row">
            {type === 'legislator_votes' && (
              <>
                <th>Legislator</th>
                <th>Supported Bills</th>
                <th>Opposed Bills</th>
              </>
            )}
            {type === 'bill_votes' && (
              <>
                <th>Bill</th>
                <th>Supporters</th>
                <th>Opposers</th>
                <th>Primary Sponsor</th>
              </>
            )}
          </tr>
        </thead>
        <tbody>
          {Object.entries(data).map(([key, value]) => (
            <tr key={key}>
              {type === 'legislator_votes' && <td>{value.name}</td>}
              {type === 'bill_votes' && (
                <>
                  <td>{value.bill_name}</td>
                  <td>{value.supporters}</td>
                  <td>{value.opposers}</td>
                  <td>{value.primary_sponsor}</td>
                </>
              )}
              {type === 'legislator_votes' && (
                <>
                  <td>{value.yes}</td>
                  <td>{value.no}</td>
                </>
              )}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
