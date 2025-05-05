import PageWrapper from "../PageWrapper/PageWrapper"
import s from "./AllFilms.module.css"
import lowerWave from "../../res/pics/lowerWave.png"
import useFilmsContext from "../../hooks/useFilmsContext"
import Film from "../../components/Film/Film"

const AllFilms = () => {
  const { films } = useFilmsContext()

  const renderedFilms = films.map((film) => (
    <Film title={film.title} id={film.id} key={film.id} />
  ))

  return (
    <>
      <div className={s.AllFilms}>
        <div className={s.title}></div>
        <div className={s.filmContainer}>{renderedFilms}</div>
      </div>
      <div className={s.lowerWave}>
        <img src={lowerWave} alt='Wave' />
      </div>
    </>
  )
}

const AllFilmsContainer = () => (
  <PageWrapper>
    <AllFilms />
  </PageWrapper>
)

export default AllFilmsContainer
