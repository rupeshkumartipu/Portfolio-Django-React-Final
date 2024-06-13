// src/components/Projects.js
import React, { useEffect, useState } from 'react';
import { getProjects } from '../services/api';
import './Projects.css';

const Projects = () => {
    const [projects, setProjects] = useState([]);

    useEffect(() => {
        const fetchProjects = async () => {
            try {
                const response = await getProjects();
                setProjects(response.data);
            } catch (error) {
                console.error('Error fetching projects data:', error);
            }
        };

        fetchProjects();
    }, []);

    return (
        <div className="projects-container">
            <h1>Projects</h1>
            <ul className="projects-list">
                {projects.map((project) => (
                    <li key={project.id} className="project-item">
                        <h3>{project.project_name}</h3>
                        <p><strong>Description:</strong> {project.description}</p>
                        <p><strong>Granting Agency:</strong> {project.granting_agency}</p>
                        <p><strong>Amount:</strong> {project.amount}</p>
                        <p><strong>Start Date:</strong> {project.start_date}</p>
                        <p><strong>End Date:</strong> {project.end_date}</p>
                        <p><strong>Status:</strong> {project.status}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Projects;
