import { useEffect, useState } from "react"
import { useParams } from "react-router-dom"
import PageWrapper from "../PageWrapper/PageWrapper"
import s from "./FilmDetail.module.css"
import useFilmsContext from "../../hooks/useFilmsContext"
import StableRate from "../../components/Rate/StableRate"
import CommentField from "../../components/Comments/CommentField.jsx"
import Comment from "../../components/Comments/Comment"

const FilmDetail = () => {
  const { films } = useFilmsContext()
  const [film, setFilm] = useState({})
  const param = useParams()

  useEffect(() => {
    const filmIndex = films.findIndex((film) => film.id == +param.id)
    setFilm(films[filmIndex])
  }, [param])

  return (
    <div className={s.FilmDetail}>
      <div className={s.title}>{film?.title}</div>
      <div className={s.filmInfoRow}>
        <div className={s.filmCardColumn}>
          <div className={s.Film}>
            <div className={s.filmImg}>
              <img src='https://m.media-amazon.com/images/M/MV5BNjNhZTk0ZmEtNjJhMi00YzFlLWE1MmEtYzM1M2ZmMGMwMTU4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg' />
            </div>
            <div className={s.filmTitle}>{film.title}</div>
            <div className={s.filmRating}>
              <StableRate rating={3} count={5} />
            </div>
          </div>
        </div>
        <div className={s.filmStatsColumn}>
          <div className={s.stat}>Year: 2002</div>
          <div className={s.stat}>Year: 2002</div>
          <div className={s.stat}>Year: 2002</div>
          <div className={s.stat}>Year: 2002</div>
        </div>
      </div>
      <div className={s.comments}>
        <CommentField />
        <Comment />
      </div>
    </div>
  )
}

const FilmDetailContainer = () => (
  <PageWrapper>
    <FilmDetail />
  </PageWrapper>
)

export default FilmDetailContainer
