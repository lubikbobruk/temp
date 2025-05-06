import React, { useState } from "react"
import s from "./Film.module.css"
import Rate from "../Rate/Rate"
import { useNavigate } from "react-router-dom"

const Film = ({ title, id, image }) => {
  const [rating, setRating] = useState(0)
  const navigate = useNavigate()

  const getNormalName = (title) => {
    if (title.length >= 70) {
      return title.slice(0, 67) + "..."
    }
    return title
  }

  return (
    <div className={s.Film}>
      <div className={s.filmImg}>
      <img src={image} alt={title} />
      </div>
      <div className={s.filmTitle} onClick={() => navigate(`/films/${id}`)}>
        {getNormalName(title)}
      </div>
      <div className={s.filmRating}>
        <Rate rating={rating} count={5} onRating={(rate) => setRating(rate)} />
      </div>
    </div>
  )
}

export default Film
