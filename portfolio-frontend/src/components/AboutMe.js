// src/components/AboutMe.js
import React, { useEffect, useState } from 'react';
import { getPersonalDetails } from '../services/api';
import './AboutMe.css';

const AboutMe = () => {
    const [details, setDetails] = useState(null);

    useEffect(() => {
        const fetchPersonalDetails = async () => {
            try {
                const response = await getPersonalDetails();
                setDetails(response.data);
            } catch (error) {
                console.error('Error fetching personal details:', error);
            }
        };

        fetchPersonalDetails();
    }, []);

    if (!details) {
        return <div>Loading...</div>;
    }

    return (
        <div className="about-container">
            <h1>About Me</h1>
            <div className="about-header">
                <img src={details.photo} alt="Professional" className="profile-photo" />
                <h2>Biography</h2>
                <p>{details.biography}</p>
            </div>
            <div className="about-section">
                <h2>Professional Background</h2>
                <p>{details.professional_background}</p>
            </div>
            <div className="about-section">
                <h2>Interests and Hobbies</h2>
                <p>{details.interests_hobbies}</p>
            </div>
        </div>
    );
};

export default AboutMe;
