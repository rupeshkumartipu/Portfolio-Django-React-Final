// src/redux/rootReducer.js
import { combineReducers } from '@reduxjs/toolkit';
import exampleReducer from './exampleSlice'; // Make sure this path is correct

// Combine all individual reducers into a root reducer
const rootReducer = combineReducers({
    example: exampleReducer,
    // Add other reducers here
});

export default rootReducer;
