/* timesheet-frontend (Next.js + React) */

import { useState, useEffect } from 'react';
import axios from 'axios';

export default function Home() {
  const [entries, setEntries] = useState([]);
  const [formData, setFormData] = useState({
    employee_id: '',
    date: '',
    hours_spent: '',
  });

  useEffect(() => {
    axios
      .get('http://localhost:8000/get-entries')
      .then((res) => setEntries(res.data))
      .catch((err) => console.error(err));
  }, []);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post('http://localhost:8000/log-time/', formData);
    alert('Time logged successfully');
    setFormData({ employee_id: '', date: '', hours_spent: '' });
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h2>Employee Timesheet</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="employee_id"
          placeholder="Employee ID"
          value={formData.employee_id}
          onChange={handleChange}
          required
        />
        <input
          type="date"
          name="date"
          value={formData.date}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="hours_spent"
          placeholder="Hours"
          value={formData.hours_spent}
          onChange={handleChange}
          required
        />
        <button type="submit">Submit</button>
      </form>
      <h3>Timesheet Entries</h3>
      <ul>
        {entries.map((entry, index) => (
          <li key={index}>
            {entry.employee_id} - {entry.date} - {entry.hours_spent} hrs
          </li>
        ))}
      </ul>
    </div>
  );
}
