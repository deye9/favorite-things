import axios from 'axios'
const API_URL = 'http://localhost:8000'

export class APIService {
  getData (endpoint) {
    const url = `${API_URL}/api/${endpoint}`
    return axios.get(url).then(response => response.data)
  }

  getSpecificData (endpoint, pk) {
    const url = `${API_URL}/api/${endpoint}/${pk}`
    return axios.get(url).then(response => response.data)
  }

  createData (endpoint, data) {
    const url = `${API_URL}/api/${endpoint}`
    return axios.post(url, data)
  }

  updateData (endpoint, data) {
    const url = `${API_URL}/api/${endpoint}/${data.id}`
    return axios.put(url, data)
  }

  deleteData (endpoint, pk) {
    const url = `${API_URL}/api/${endpoint}/${pk}`
    return axios.delete(url)
  }
}
