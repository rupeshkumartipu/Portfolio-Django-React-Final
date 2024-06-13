// src/services/api.js
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/';

const getToken = () => {
    return localStorage.getItem('access_token');
};

const api = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

api.interceptors.request.use((config) => {
    const token = getToken();
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

export const obtainToken = (username, password) => {
    return api.post('token/', { username, password });
};

export const getEducations = () => api.get('educations/');
export const getSkills = () => api.get('skills/');
export const getExperiences = () => api.get('experiences/');
export const getPublications = () => api.get('publications/');
export const getPatents = () => api.get('patents/');
export const getProjects = () => api.get('projects/');
export const getAwards = () => api.get('awards/');
export const getConferences = () => api.get('conferences/');
export const getBooks = () => api.get('books/');
export const getSocialLinks = () => api.get('sociallinks/');
export const getAreasOfInterest = () => api.get('areasofinterest/');
export const getResearchPublicationSummaries = () => api.get('researchpublicationsummaries/');
export const getWorkshops = () => api.get('workshops/');
export const getSeminars = () => api.get('seminars/');
export const getSTTPs = () => api.get('sttps/');
export const getDissertationsGuided = () => api.get('dissertationsguided/');
export const getPersonalDetails = () => api.get('personaldetails/');

// Add the missing functions here
export const getRecentProjects = () => api.get('projects/?limit=3');
export const getProfessionalHeadline = () => api.get('headline/');
export const getLastExperience = () => api.get('experiences/?ordering=-to_date&limit=1');
export const getBiography = () => api.get('biography/');
export const getPublicationsSummary = () => api.get('publications/summary/');
export const getPatentsSummary = () => api.get('patents/summary/');
export const getBooksSummary = () => api.get('books/summary/');
export const getConferencesSummary = () => api.get('conferences/summary/');
export const getSkillsSummary = () => api.get('skills/summary/');
export const getEducationsSummary = () => api.get('educations/summary/');
export const getAwardsSummary = () => api.get('awards/summary/');
