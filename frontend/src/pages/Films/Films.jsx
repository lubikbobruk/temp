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
        <Film
          title="The Hunger Games"
          id={101}
          image="https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg"
        />
        <Film
          title="Harry Potter and the Philosopher's Stone"
          id={102}
          image="https://m.media-amazon.com/images/I/51UoqRAxwEL._SY445_SX342_.jpg"
        />
        <Film
          title="Pride and Prejudice"
          id={103}
          image="https://m.media-amazon.com/images/I/51Z0nLAfLmL.jpg"
        />
        <Film
          title="The Hobbit"
          id={104}
          image="https://m.media-amazon.com/images/I/41aQPTCmeVL._SY445_SX342_.jpg"
        />
        <Film
          title="The Great Gatsby"
          id={105}
          image="https://upload.wikimedia.org/wikipedia/commons/7/7a/The_Great_Gatsby_Cover_1925_Retouched.jpg"
        />
        <Film
          title="To Kill a Mockingbird"
          id={106}
          image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1553383690i/2657.jpg"
        />
        <Film
          title="The Catcher in the Rye"
          id={107}
          image="https://cdn.knihcentrum.cz/98805129_the-catcher-in-the-rye-1.jpg"
        />
        <Film
          title="1984"
          id={108}
          image="https://data.knizniklub.cz/book/015/858/0158581/large.jpg"
        />
        <Film
          title="The Lord of the Rings"
          id={109}
          image="https://m.media-amazon.com/images/I/51EstVXM1UL._SY445_SX342_.jpg"
        />
        <Film
          title="The Design of Everyday Things"
          id={110}
          image="https://m.media-amazon.com/images/I/81zpLhP1gWL.jpg"
  />

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
