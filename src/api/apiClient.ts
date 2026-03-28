// apiClient.ts
import axios from 'axios';
import { encryptData, decryptData } from './encryption';

const apiClient = axios.create({
    baseURL: 'https://api.example.com',
    headers: {
        'Content-Type': 'application/json',
    },
});

apiClient.interceptors.request.use((config) => {
    if (config.data) {
        config.data = encryptData(config.data);
    }
    return config;
});

apiClient.interceptors.response.use((response) => {
    if (response.data) {
        response.data = decryptData(response.data);
    }
    return response;
});

export default apiClient;