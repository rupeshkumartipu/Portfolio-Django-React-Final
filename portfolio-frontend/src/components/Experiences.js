// src/components/Experiences.js
import React, { useEffect, useState } from 'react';
import { getExperiences } from '../services/api';
import './Experiences.css';

const Experiences = () => {
    const [experiences, setExperiences] = useState([]);

    useEffect(() => {
        const fetchExperiences = async () => {
            try {
                const response = await getExperiences();
                setExperiences(response.data);
            } catch (error) {
                console.error('Error fetching experience data:', error);
            }
        };

        fetchExperiences();
    }, []);

    return (
        <div className="experience-container">
            <h1>Experience</h1>
            <ul className="experience-list">
                {experiences.map((experience) => (
                    <li key={experience.id} className="experience-item">
                        <h3>{experience.positions_held}</h3>
                        <p><strong>Organization:</strong> {experience.organization}</p>
                        <p><strong>From:</strong> {experience.from_date} - <strong>To:</strong> {experience.to_date}</p>
                        <p><strong>Duration:</strong> {experience.duration}</p>
                        <p><strong>Key Responsibilities:</strong> {experience.key_responsibilities}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Experiences;
