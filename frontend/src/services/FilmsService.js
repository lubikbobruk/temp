import api from "../api/axios";

export default class FilmsService {
  static async fetchFilms () {
    return api.post('/films')
  }
}