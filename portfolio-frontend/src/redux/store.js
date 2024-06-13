// src/redux/store.js
import { configureStore } from '@reduxjs/toolkit';
import rootReducer from './rootReducer';

// Create and configure the Redux store with the root reducer
const store = configureStore({
    reducer: rootReducer,
});

export default store;
