// src/components/Contact.js
import React, { useState } from 'react';
import './Contact.css';

const Contact = () => {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        message: '',
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Handle form submission logic here
        console.log('Form data submitted:', formData);
    };

    return (
        <div className="contact-container">
            <h1>Contact</h1>
            <form onSubmit={handleSubmit} className="contact-form">
                <div className="form-group">
                    <label htmlFor="name">Name:</label>
                    <input
                        type="text"
                        id="name"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="email">Email:</label>
                    <input
                        type="email"
                        id="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="message">Message:</label>
                    <textarea
                        id="message"
                        name="message"
                        value={formData.message}
                        onChange={handleChange}
                        required
                    />
                </div>
                <button type="submit" className="submit-button">Submit</button>
            </form>
            <div className="contact-info">
                <h2>Contact Information</h2>
                <p>Email: tipu0003@gmail.com</p>
                <p>Phone: +91-8802281783</p>
                <h2>Social Links</h2>
                <ul className="social-links">
                    <li>
                        <a href="https://orcid.org/0000-0001-8476-8364" target="_blank" rel="noopener noreferrer">
                            ORCID
                        </a>
                    </li>
                    <li>
                        <a href="https://www.researchgate.net/profile/Rupesh-Kumar-Tipu?ev=hdr_xprf" target="_blank" rel="noopener noreferrer">
                            ResearchGate
                        </a>
                    </li>
                    <li>
                        <a href="https://scholar.google.com/citations?user=uZzLU8IAAAAJ&hl=en&oi=ao" target="_blank" rel="noopener noreferrer">
                            Google Scholar
                        </a>
                    </li>
                    <li>
                        <a href="https://www.webofscience.com/wos/author/record/AFC-1290-2022" target="_blank" rel="noopener noreferrer">
                            WoS
                        </a>
                    </li>
                    <li>
                        <a href="https://www.linkedin.com/in/rupesh-kumar-tipu" target="_blank" rel="noopener noreferrer">
                            LinkedIn
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    );
};

export default Contact;
