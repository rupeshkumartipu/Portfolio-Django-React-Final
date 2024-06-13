// src/components/Conferences.js
import React, { useEffect, useState } from 'react';
import { getConferences } from '../services/api';
import './Conferences.css';

const Conferences = () => {
    const [conferences, setConferences] = useState([]);

    useEffect(() => {
        const fetchConferences = async () => {
            try {
                const response = await getConferences();
                setConferences(response.data);
            } catch (error) {
                console.error('Error fetching conferences data:', error);
            }
        };

        fetchConferences();
    }, []);

    return (
        <div className="conferences-container">
            <h1>Conferences</h1>
            <ul className="conferences-list">
                {conferences.map((conference) => (
                    <li key={conference.id} className="conference-item">
                        <h3>{conference.title_of_paper}</h3>
                        <p><strong>Title of Conference:</strong> {conference.title_of_conference}</p>
                        <p><strong>Type:</strong> {conference.type}</p>
                        <p><strong>Date of Conference:</strong> {conference.date_of_conference}</p>
                        <p><strong>Organizing Institute:</strong> {conference.organizing_institute}</p>
                        <p><strong>Authors:</strong> {conference.authors}</p>
                        <p><strong>Location of Conference:</strong> {conference.location_of_conference}</p>
                        {conference.link_of_conference && (
                            <p>
                                <a href={conference.link_of_conference} target="_blank" rel="noopener noreferrer">
                                    More Info
                                </a>
                            </p>
                        )}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Conferences;
