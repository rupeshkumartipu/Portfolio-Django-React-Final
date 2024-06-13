// src/components/Navbar.js
import React from 'react';
import { NavLink } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
        return (
            <nav className="navbar">
                    <ul>
                            <li><NavLink exact to="/" activeClassName="active">Home</NavLink></li>
                            {/*<li><NavLink to="/awards" activeClassName="active">Awards</NavLink></li>*/}
                            <li><NavLink to="/books" activeClassName="active">Books</NavLink></li>
                            <li><NavLink to="/conferences" activeClassName="active">Conferences</NavLink></li>
                            <li><NavLink to="/education" activeClassName="active">Education</NavLink></li>
                            <li><NavLink to="/experience" activeClassName="active">Experience</NavLink></li>
                            <li><NavLink to="/patents" activeClassName="active">Patents</NavLink></li>
                            <li><NavLink to="/projects" activeClassName="active">Projects</NavLink></li>
                            <li><NavLink to="/publications" activeClassName="active">Publications</NavLink></li>
                            <li><NavLink to="/skills" activeClassName="active">Skills</NavLink></li>
                            <li><NavLink to="/contact" activeClassName="active">Contact</NavLink></li>
                            <li><NavLink to="/login" activeClassName="active">Login</NavLink></li>
                    </ul>
            </nav>
        );
};

export default Navbar;
