// src/components/Books.js
import React, { useEffect, useState } from 'react';
import { getBooks } from '../services/api';
import './Books.css';

const Books = () => {
    const [books, setBooks] = useState([]);

    useEffect(() => {
        const fetchBooks = async () => {
            try {
                const response = await getBooks();
                setBooks(response.data);
            } catch (error) {
                console.error('Error fetching books data:', error);
            }
        };

        fetchBooks();
    }, []);

    return (
        <div className="books-container">
            <h1>Books</h1>
            <ul className="books-list">
                {books.map((book) => (
                    <li key={book.id} className="book-item">
                        <h3>{book.title}</h3>
                        <p><strong>Publisher:</strong> {book.publisher}</p>
                        <p><strong>Publication Date:</strong> {book.publication_date}</p>
                        <p><strong>Summary:</strong> {book.summary}</p>
                        <p><strong>ISBN/ISSN:</strong> {book.isbn_issn}</p>
                        {book.link && (
                            <p>
                                <a href={book.link} target="_blank" rel="noopener noreferrer">
                                    More Info
                                </a>
                            </p>
                        )}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Books;
