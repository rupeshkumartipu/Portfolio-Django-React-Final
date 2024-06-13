// src/components/Home.js
import React, { useEffect, useState } from 'react';
import {
    getProjects,
    getEducations,
    getExperiences,
    getPublications,
    getPatents,
    getBooks,
    getConferences,
    getSocialLinks,
} from '../services/api';
import './Home.css';

const Home = () => {
    const [projects, setProjects] = useState([]);
    const [headline, setHeadline] = useState('Assistant Professor & Structural Engineering Expert Specializing in AI-driven Predictive Modelling and Optimization Strategies'); // Static for now
    const [biography, setBiography] = useState('Dr. Rupesh Kumar Tipu is an accomplished Assistant Professor at K. R. Mangalam University, with over a decade of teaching experience and a strong background in structural engineering and computational optimization. He holds a Ph.D. from CHARUSAT University, where he developed AI-based predictive models and computational optimization techniques for concrete properties.\n' +
        '\n' +
        'Dr. Tipu\'s academic journey is complemented by substantial industrial experience, including roles as a structural designer and internships with prominent companies. His expertise spans a diverse array of subjects, from machine learning and deep learning to structural design and concrete technology.\n' +
        '\n' +
        'In addition to his teaching and research duties, Dr. Tipu is actively involved in curriculum development, mentoring, and several key administrative roles at K. R. Mangalam University. His contributions to the academic community include 15 research papers published in SCIE and Scopus-indexed journals, numerous conference presentations, and several book chapters. He has also authored multiple books on advanced engineering topics and holds several published patents.\n' +
        '\n' +
        'A dedicated educator and researcher, Dr. Tipu is passionate about leveraging AI and machine learning to solve complex engineering problems, with a keen interest in enhancing the predictive accuracy and optimization of concrete properties. His work continues to inspire and shape the future of structural engineering and AI integration.'); // Static for now
    const [publicationsSummary, setPublicationsSummary] = useState('');
    const [patentsSummary, setPatentsSummary] = useState('');
    const [booksSummary, setBooksSummary] = useState('');
    const [conferencesSummary, setConferencesSummary] = useState('');
    const [experienceSummary, setExperienceSummary] = useState('');
    const [socialLinks, setSocialLinks] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const projectsResponse = await getProjects();
                setProjects(projectsResponse.data);

                const experiencesResponse = await getExperiences();
                if (experiencesResponse.data.length > 0) {
                    const totalYears = experiencesResponse.data.reduce((total, exp) => {
                        const fromDate = new Date(exp.from_date);
                        const toDate = new Date(exp.to_date);
                        const years = (toDate - fromDate) / (1000 * 60 * 60 * 24 * 365.25);
                        return total + years;
                    }, 0);
                    setExperienceSummary(`Total Years of Experience: ${totalYears.toFixed(1)}`);
                }

                const publicationsResponse = await getPublications();
                setPublicationsSummary(`Total Publications: ${publicationsResponse.data.length}`);

                const patentsResponse = await getPatents();
                setPatentsSummary(`Total Patents: ${patentsResponse.data.length}`);

                const booksResponse = await getBooks();
                setBooksSummary(`Total Books: ${booksResponse.data.length}`);

                const conferencesResponse = await getConferences();
                setConferencesSummary(`Total Conferences: ${conferencesResponse.data.length}`);

                const socialLinksResponse = await getSocialLinks();
                setSocialLinks(socialLinksResponse.data);
            } catch (error) {
                console.error('Error fetching home page data:', error);
            }
        };

        fetchData();
    }, []);

    return (
        <div className="home-container">
            <div className="home-header">
                <img src="/images/image.jpg" alt="Rupesh Kumar" />
                <h1>Dr. Rupesh Kumar Tipu</h1>
                <h2>{headline}</h2>
                <p style={{ textAlign: 'justify' }}>{biography}</p>
            </div>

            <div className="home-section">
                <h3>Recent Projects</h3>
                <ul>
                    {projects.map((project) => (
                        <li key={project.id}>
                            <h4>{project.project_name}</h4>
                            <p>{project.description}</p>
                        </li>
                    ))}
                </ul>
            </div>

            <div className="home-section">
                <h3>Summary</h3>
                <p><strong>{publicationsSummary}</strong></p>
                <p><strong>{patentsSummary}</strong></p>
                <p><strong>{booksSummary}</strong></p>
                <p><strong>{conferencesSummary}</strong></p>
                <p><strong>{experienceSummary}</strong></p>
            </div>

            <div className="social-links">
                <ul>
                    {socialLinks.map((link) => (
                        <li key={link.platform_name}>
                            <a href={link.url} target="_blank" rel="noopener noreferrer">
                                <img src={`/images/${link.platform_name}.png`} alt={link.platform_name} />
                            </a>
                        </li>
                    ))}
                </ul>
            </div>

            <div className="download-cv">
                <a href="/docs/CV.pdf" download>
                    <button>Download CV</button>
                </a>
            </div>
        </div>
    );
};

export default Home;
