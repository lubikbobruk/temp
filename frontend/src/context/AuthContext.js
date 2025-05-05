import axios from "axios"
import { createContext, useState, useCallback } from "react"
import AuthService from "../services/AuthService"

const AuthContext = createContext()

function AuthProvider({ children }) {
  const [user, setUser] = useState({})

  const login = async (email, password) => {
    try {
      const response = await AuthService.login(email, password)
      localStorage.setItem('token', response.data.access_token)
      setUser(response.data.user)
    } catch (e) {
      console.log(e)
    }
  }

  const logout = async () => {
    try {
      const response = await AuthService.logout()
      localStorage.removeItem('token', response.data.access_token)
      setUser({})
    } catch (e) {
      console.log(e)
    }
  }

  const valueToShare = {
    user,
    login,
    logout
  }

  return <AuthContext.Provider value={valueToShare}>{children}</AuthContext.Provider>
}

export { AuthProvider }
export default AuthContext
