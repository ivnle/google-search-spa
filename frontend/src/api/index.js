import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000'

export function getSet() {
  return axios.get(`${API_URL}/sets/`)
}

export function saveSet(set) {
  return axios.post(`${API_URL}/sets/`, set)
}

// export function fetchSurvey(surveyId) {
//   return axios.get(`${API_URL}/surveys/${surveyId}/`)
// }
//
export function saveSurveyResponse(surveyResponse) {
  return axios.put(`${API_URL}/surveys/${surveyResponse.id}/`, surveyResponse)
}
//
// export function postNewSurvey(survey) {
//   return axios.post(`${API_URL}/surveys/`, survey)
// }
