import { Routes, Route } from "react-router-dom"

import g from "./App.module.css"
import Login from "./pages/Login/Login"
import Films from "./pages/Films/Films"
import FilmDetail from "./pages/FilmDetail/FilmDetail"
import AllFilms from "./pages/AllFilms/AllFilms"
import ScrollToTop from "./components/ScrollToTop/ScrollToTop"

function App() {

  // useEffect(() => {
  //   fetchFilms()
  // }, [])

  return (
    <div className={g.App}>
      <ScrollToTop />
      <Routes>
        <Route exact path='/' element={<Login />} />
        <Route exact path='/films' element={<Films />} />
        <Route exact path='/films/:id' element={<FilmDetail />} />
        <Route exact path='/rated-films' element={<AllFilms />} />
        <Route exact path='/unrated-films' element={<AllFilms />} />
      </Routes>
    </div>
  )
}

export default App
