// src/components/Awards.js
import React, { useEffect, useState } from 'react';
import { getAwards } from '../services/api';
import './Awards.css';

const Awards = () => {
    const [awards, setAwards] = useState([]);

    useEffect(() => {
        const fetchAwards = async () => {
            try {
                const response = await getAwards();
                setAwards(response.data);
            } catch (error) {
                console.error('Error fetching awards data:', error);
            }
        };

        fetchAwards();
    }, []);

    return (
        <div className="awards-container">
            <h1>Awards</h1>
            <ul className="awards-list">
                {awards.map((award) => (
                    <li key={award.id} className="award-item">
                        <h3>{award.title}</h3>
                        <p><strong>Organization:</strong> {award.organization}</p>
                        <p><strong>Date Awarded:</strong> {award.date_awarded}</p>
                        <p><strong>Description:</strong> {award.description}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Awards;
