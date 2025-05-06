import React from "react"

import PageWrapper from "../PageWrapper/PageWrapper"
import Film from "../../components/Film/Film"
import s from "./Films.module.css"
import Carousel from "../../components/Carousel/Carousel"
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
      <div
        style={{
          backgroundImage: "url('/assets/back.jpg')",
          backgroundRepeat: "repeat-y",
          backgroundSize: "100% auto",
          backgroundPosition: "top center",
          minHeight: "100vh",
        }}
      >
        <div className={s.filmsTitle}>Books to rate</div>
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
    </div>  
    </>
  )
}

const FilmsContainer = () => (
    <Films />
)

export default FilmsContainer
