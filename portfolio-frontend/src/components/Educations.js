// src/components/Education.js
import React, { useEffect, useState } from 'react';
import { getEducations } from '../services/api';
import './Educations.css';

const Education = () => {
    const [educations, setEducations] = useState([]);

    useEffect(() => {
        const fetchEducations = async () => {
            try {
                const response = await getEducations();
                setEducations(response.data);
            } catch (error) {
                console.error('Error fetching education data:', error);
            }
        };

        fetchEducations();
    }, []);

    return (
        <div className="education-container">
            <h1>Education</h1>
            <ul className="education-list">
                {educations.map((education) => (
                    <li key={education.id} className="education-item">
                        <h3>{education.degree}</h3>
                        <p className="education-university">{education.university} - {education.year_of_passing}</p>
                        <p className="education-specialization">{education.specialization}</p>
                        <p className="education-description">{education.description}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Education;
