// src/components/Publications.js
import React, { useEffect, useState } from 'react';
import { getPublications } from '../services/api';
import './Publications.css';

const Publications = () => {
    const [publications, setPublications] = useState([]);

    useEffect(() => {
        const fetchPublications = async () => {
            try {
                const response = await getPublications();
                setPublications(response.data);
            } catch (error) {
                console.error('Error fetching publications data:', error);
            }
        };

        fetchPublications();
    }, []);

    return (
        <div className="publications-container">
            <h1>Publications</h1>
            <ul className="publications-list">
                {publications.map((publication) => (
                    <li key={publication.id} className="publication-item">
                        <h3>{publication.title}</h3>
                        <p><strong>Authors:</strong> {publication.authors}</p>
                        <p><strong>Journal:</strong> {publication.journal}</p>
                        <p><strong>Year:</strong> {publication.year}</p>
                        <p><strong>Publisher:</strong> {publication.publisher}</p>
                        <p><strong>Indexing:</strong> {publication.indexing}</p>
                        <p><strong>Impact Factor:</strong> {publication.impact_factor}</p>
                        <p><strong>DOI:</strong> {publication.doi}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Publications;
