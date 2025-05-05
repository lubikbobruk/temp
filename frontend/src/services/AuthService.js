import api from "../api/axios"

export default class AuthService {
  static async login(username, password) {
    return api.post('/auth/login', {username, password})
  }

  static async logout() {
    return api.post('/auth/logout')
  }
}
