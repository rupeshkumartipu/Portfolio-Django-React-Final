// src/components/Patents.js
import React, { useEffect, useState } from 'react';
import { getPatents } from '../services/api';
import './Patents.css';

const Patents = () => {
    const [patents, setPatents] = useState([]);

    useEffect(() => {
        const fetchPatents = async () => {
            try {
                const response = await getPatents();
                setPatents(response.data);
            } catch (error) {
                console.error('Error fetching patents data:', error);
            }
        };

        fetchPatents();
    }, []);

    return (
        <div className="patents-container">
            <h1>Patents</h1>
            <ul className="patents-list">
                {patents.map((patent) => (
                    <li key={patent.id} className="patent-item">
                        <h3>{patent.patent_title}</h3>
                        <p><strong>Inventors:</strong> {patent.inventors}</p>
                        <p><strong>Country:</strong> {patent.country}</p>
                        <p><strong>Application Number:</strong> {patent.application_number}</p>
                        <p><strong>Publication Date:</strong> {patent.publication_date}</p>
                        <p><strong>Status:</strong> {patent.status}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Patents;
