import React from "react"

import PageWrapper from "../PageWrapper/PageWrapper"
import Film from "../../components/Film/Film"
import s from "./Films.module.css"
import Carousel from "../../components/Carousel/Carousel"
import lowerWave from "../../res/pics/lowerWave.png"
import useFilmsContext from "../../hooks/useFilmsContext"
import Button from "../../components/Button/Button"
import { useNavigate } from "react-router-dom"

const Films = () => {
  const { films } = useFilmsContext()
  const navigator = useNavigate()

  const renderedFilms = films.map((film) => (
    <Film title={film.title} id={film.id} key={film.id} />
  ))

  return (
    <>
      <div className={s.Films}>
        <div className={s.filmsTitle}>Rate films</div>
        <Carousel>
          {renderedFilms}
          {renderedFilms}
          {renderedFilms}
          {renderedFilms}
        </Carousel>
        <div className={s.showAllButton}>
          <Button
            onClick={() => {
              navigator("/unrated-films")
            }}
          >
            Show all unrated films
          </Button>
        </div>
        <div className={s.filmsTitle}>Your rates</div>
        <Carousel>{renderedFilms}</Carousel>
        <div className={s.showAllButton}>
          <Button
            onClick={() => {
              navigator("/rated-films")
            }}
          >
            Show all rated films
          </Button>
        </div>
      </div>
      <div className={s.lowerWave}>
        <img src={lowerWave} alt='Wave' />
      </div>
    </>
  )
}

const FilmsContainer = () => (
  <PageWrapper>
    <Films />
  </PageWrapper>
)

export default FilmsContainer
