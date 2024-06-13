// src/components/Skills.js
import React, { useEffect, useState } from 'react';
import { getSkills } from '../services/api';
import './Skills.css';

const Skills = () => {
    const [skills, setSkills] = useState([]);

    useEffect(() => {
        const fetchSkills = async () => {
            try {
                const response = await getSkills();
                setSkills(response.data);
            } catch (error) {
                console.error('Error fetching skills data:', error);
            }
        };

        fetchSkills();
    }, []);

    return (
        <div className="skills-container">
            <h1>Skills</h1>
            <ul className="skills-list">
                {skills.map((skill) => (
                    <li key={skill.id} className="skill-item">
                        <h3>{skill.name}</h3>
                        <p><strong>Level:</strong> {skill.level}</p>
                        <p><strong>Project:</strong> {skill.project_for_which_used}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Skills;
