// src/Router.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import AboutMe from './components/AboutMe';
import Awards from './components/Awards';
import Books from './components/Books';
import Conferences from './components/Conferences';
import Contact from './components/Contact';
import Education from './components/Educations';
import Experience from './components/Experiences';
import Patents from './components/Patents';
import Projects from './components/Projects';
import Publications from './components/Publications';
import Skills from './components/Skills';
import Navbar from './components/Navbar';
import Login from './components/Login'; // Import Login component

const AppRouter = () => (
    <Router>
        <Navbar />
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<AboutMe />} />
            <Route path="/awards" element={<Awards />} />
            <Route path="/books" element={<Books />} />
            <Route path="/conferences" element={<Conferences />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="/education" element={<Education />} />
            <Route path="/experience" element={<Experience />} />
            <Route path="/patents" element={<Patents />} />
            <Route path="/projects" element={<Projects />} />
            <Route path="/publications" element={<Publications />} />
            <Route path="/skills" element={<Skills />} />
            <Route path="/login" element={<Login />} />
        </Routes>
    </Router>
);

export default AppRouter;
