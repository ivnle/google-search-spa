import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000'

export function getSet(jwt) {
  return axios.get(`${API_URL}/sets/`, { headers: { Authorization: `Bearer: ${jwt}` } })
}

export function saveSet(set, jwt) {
  return axios.post(`${API_URL}/sets/`, set, { headers: { Authorization: `Bearer: ${jwt}` } })
}

export function authenticate (userData) {
  return axios.post(`${API_URL}/login/`, userData)
}

export function register (userData) {
  return axios.post(`${API_URL}/register/`, userData)
}
