import axios from "axios"
import { createContext, useState, useCallback } from "react"
import api from "../api/axios"
import FilmsService from "../services/FilmsService"

const FilmsContext = createContext()

function FilmsProvider({ children }) {
  const [films, setFilms] = useState([
    { id: 0, title: "Silence of the Lambs" },
    { id: 1, title: "The Shawshank Redemption" },
  ])

  const fetchFilms = async () => {
    try {
      const response = await FilmsService.fetchFilms()
      setFilms(response.data)
    } catch (e) {
      console.log(e)
    }
  }

  const valueToShare = {
    films,
    fetchFilms,
  }

  return (
    <FilmsContext.Provider value={valueToShare}>
      {children}
    </FilmsContext.Provider>
  )
}

export { FilmsProvider }
export default FilmsContext
